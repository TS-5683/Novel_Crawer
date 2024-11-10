import requests as rq
from tools.random_agent import get
from xml import etree

# 不分页章节正文爬取
def get_chapter_content1(self, chapter_url:str):
    res = []

    url = self.catalog_url + chapter_url
    response = rq.get(url, headers=get())
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
        
    res_ = html.xpath('//div[@class="content" and @id="content"]//text()')
    res += [i.strip() for i in res_ if any(char.isprintable() for char in i)]

    res = list(filter(lambda x: x, res))
    res = '\n'.join(res)
    return res

# 分页章节正文爬取
def get_chapter_content2(self, chapter_url:str):
    res = []
    
    i = -1
    while True:
        i += 1
        if i == 1:
            continue

        curl = chapter_url if i == 0 else f'{chapter_url[:-5]}_{i}.html'
        url = self.catalog_url + curl
        response = rq.get(url, headers=get())
        response.encoding = 'gbk'

        if response.status_code != 200:
            break

        html = etree.HTML(response.text)
        res_ = html.xpath('//div[@id="content"]//text()')[3:]
        res += [i.strip() for i in res_ if any(char.isprintable() for char in i)]

    res = list(filter(lambda x: x, res))
    res = '\n'.join(res)
    return res