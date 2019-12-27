from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'https://www.infoq.com/news/'

# 取得网页完整内容


def craw(url):
    response = requests.get(url, headers=headers)
    print(response.text)

# craw(url)

# 取得新闻标题


def craw2(url):
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    for title_href in soup.find_all('div', class_='items__content'):
        print([title.get('title')
               for title in title_href.find_all('a') if title.get('title')])

# craw2(url)


# 翻页
for i in range(15, 46, 15):
    url = 'http://www.infoq.com/news/' + str(i)
    # print(url)
    craw2(url)
