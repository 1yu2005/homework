"""
Python爬虫自学任务：BeautifulSoup抓取政府网新闻
技术栈：requests + BeautifulSoup4 + lxml + SQLite
目标网址：https://www.gov.cn/toutiao/liebiao/
"""

import requests
import time
import random
import re
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

# ==================== 1. 数据库部分 ====================
engine = create_engine("sqlite:///gov_news.db", echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class GovNews(Base):
    """政府新闻数据表模型"""
    __tablename__ = "gov_news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500))
    publish_time = Column(String(30))
    link = Column(String(800), unique=True)


Base.metadata.create_all(bind=engine)
print("数据库初始化完成：gov_news.db")


# ==================== 2. 请求头配置 ====================
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0",
    "Referer": "https://www.gov.cn/toutiao/liebiao/"
}


# ==================== 3. 构建分页URL ====================
def build_url(page_num: int) -> str:
    """
    构建分页URL
    第1页: index.htm (或 home.htm)
    第2页起: home_2.htm, home_3.htm ...
    """
    if page_num == 1:
        return "https://www.gov.cn/toutiao/liebiao/index.htm"
    else:
        return f"https://www.gov.cn/toutiao/liebiao/home_{page_num}.htm"


# ==================== 4. 解析函数 ====================
def parse_news_item(item):
    """解析单个新闻条目，返回 (title, publish_time, full_link) 或 None"""
    try:
        # 提取标题和链接
        title_elem = item.select_one("h4 a")
        if not title_elem:
            return None
        
        title = title_elem.get_text(strip=True)
        if not title:
            return None
        
        href = title_elem.get("href", "")
        if not href:
            return None
        
        # 拼接完整链接
        if href.startswith("/"):
            full_link = "https://www.gov.cn" + href
        elif href.startswith("http"):
            full_link = href
        else:
            full_link = "https://www.gov.cn/" + href
        
        # 提取发布时间
        time_elem = item.select_one("span.date")
        if time_elem:
            publish_time = time_elem.get_text(strip=True)
        else:
            # 尝试从文本中提取日期
            item_text = item.get_text()
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', item_text)
            publish_time = date_match.group(1) if date_match else "未知时间"
        
        if not title:
            return None
            
        return (title, publish_time, full_link)
    except Exception:
        return None


# ==================== 5. 带重试的请求函数 ====================
def fetch_with_retry(url, max_retries=3):
    """带重试机制的请求"""
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            return resp
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            if attempt < max_retries - 1:
                wait_time = random.uniform(2, 5)
                print(f"  [重试] 第{attempt + 1}次请求失败，{wait_time:.1f}秒后重试...")
                time.sleep(wait_time)
            else:
                raise e
    return None


# ==================== 6. 抓取函数 ====================
def crawl_page(page_num: int) -> bool:
    """
    抓取单页新闻数据并存入数据库
    """
    url = build_url(page_num)
    print(f"[开始] 正在抓取第 {page_num} 页: {url}")

    try:
        # 发送请求（带重试）
        resp = fetch_with_retry(url)
        
        if resp is None:
            print(f"[错误] 第 {page_num} 页请求失败")
            return False
        
        # 检测状态码
        if resp.status_code == 403:
            print(f"[警告] 第 {page_num} 页访问受限(403)，终止抓取")
            return False
        
        if resp.status_code != 200:
            print(f"[错误] 第 {page_num} 页请求失败，状态码: {resp.status_code}")
            return False

        resp.encoding = "utf-8"
        html_content = resp.text

        # BeautifulSoup 解析
        soup = BeautifulSoup(html_content, "lxml")
        
        # 【修复】使用正确的选择器 .news_box li
        news_items = soup.select(".news_box li")
        
        if not news_items:
            # 首页(index.htm)结构可能不同，尝试其他选择器
            news_items = soup.select(".list_2 li") or soup.select(".news-list li")
        
        if not news_items:
            print(f"[警告] 第 {page_num} 页未找到新闻条目")
            return False

        print(f"[信息] 第 {page_num} 页找到 {len(news_items)} 条新闻")

        # 解析所有新闻条目
        parsed_data = []
        for item in news_items:
            result = parse_news_item(item)
            if result:
                parsed_data.append(result)
        
        if not parsed_data:
            print(f"[警告] 第 {page_num} 页没有有效数据")
            return False

        # 逐条插入数据库
        inserted_count = 0
        skipped_count = 0
        
        for title, publish_time, full_link in parsed_data:
            db = SessionLocal()
            try:
                existing = db.query(GovNews).filter(GovNews.link == full_link).first()
                if existing:
                    print(f"  [跳过] 链接已存在: {title[:30]}...")
                    skipped_count += 1
                    continue
                
                news = GovNews(
                    title=title,
                    publish_time=publish_time,
                    link=full_link
                )
                db.add(news)
                db.commit()
                inserted_count += 1
                print(f"  [入库] {title[:30]}... | {publish_time}")
                
            except IntegrityError:
                db.rollback()
                skipped_count += 1
                print(f"  [跳过] 重复数据: {title[:30]}...")
            except SQLAlchemyError as e:
                db.rollback()
                skipped_count += 1
                print(f"  [错误] 数据库操作失败: {e}")
            finally:
                db.close()
        
        print(f"[完成] 第 {page_num} 页: 新增 {inserted_count} 条，跳过 {skipped_count} 条")
        return True

    except requests.exceptions.RequestException as e:
        print(f"[错误] 第 {page_num} 页网络请求异常: {e}")
        return False
    except Exception as e:
        print(f"[错误] 第 {page_num} 页未知异常: {e}")
        return False


# ==================== 7. 查看数据 ====================
def show_news(limit: int = 20) -> None:
    """查看数据库中已存储的新闻"""
    db = SessionLocal()
    try:
        total_count = db.query(GovNews).count()
        news_list = db.query(GovNews).order_by(GovNews.id.desc()).limit(limit).all()
        if not news_list:
            print("数据库中暂无数据")
            return
        
        print("\n" + "=" * 70)
        print(f"数据库总条数: {total_count}，显示最新 {len(news_list)} 条：")
        print("-" * 70)
        for i, news in enumerate(news_list, 1):
            print(f"{i}. {news.title}")
            print(f"   时间: {news.publish_time}")
            print(f"   链接: {news.link}")
            print("-" * 70)
    except SQLAlchemyError as e:
        print(f"查询数据库失败: {e}")
    finally:
        db.close()


# ==================== 8. 主程序 ====================
def main():
    """主程序入口"""
    print("\n" + "=" * 50)
    print("政府网新闻爬虫 (BeautifulSoup版)")
    print("=" * 50)
    print("技术栈: requests + BeautifulSoup4 + lxml + SQLite")
    print("目标: https://www.gov.cn/toutiao/liebiao/")
    print("=" * 50)

    while True:
        print("\n请选择操作:")
        print("  1. 开始批量抓取 (1-10页)")
        print("  2. 抓取指定页")
        print("  3. 查看已存储数据")
        print("  0. 退出程序")
        choice = input("请输入您的选择: ").strip()

        if choice == "0":
            print("程序已退出")
            break

        elif choice == "1":
            print("\n[开始] 批量抓取第 1-10 页...")
            success_count = 0
            for page in range(1, 11):
                print("-" * 50)
                if crawl_page(page):
                    success_count += 1
                # 每页抓取后随机休眠3~6秒，降低被封风险
                sleep_time = random.uniform(3, 6)
                print(f"[休眠] 等待 {sleep_time:.2f} 秒...")
                time.sleep(sleep_time)
            print("-" * 50)
            print(f"[全部完成] 成功抓取 {success_count}/10 页")

        elif choice == "2":
            try:
                page_num = int(input("请输入要抓取的页码 (1-10): ").strip())
                if 1 <= page_num <= 10:
                    crawl_page(page_num)
                else:
                    print("页码应在 1-10 之间")
            except ValueError:
                print("请输入有效数字")

        elif choice == "3":
            show_news(limit=20)

        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()