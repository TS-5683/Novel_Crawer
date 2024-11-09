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
    chapter_urls = [chapter_url, f'{chapter_url[:-5]}_2.html']

    for i, curl in enumerate(chapter_urls):
        url = self.home_url + curl
        response = rq.get(url, headers=get())
        response.encoding = 'utf-8'

        html = etree.HTML(response.text)
        if i == 0:
            res_ = html.xpath('//div[@class="content" and @id="content"]//text()')[2:]
        else:
            res_ = html.xpath('//div[@class="content" and @id="content"]//text()')[1:]
        res += [i.strip() for i in res_ if any(char.isprintable() for char in i)]

    res = list(filter(lambda x: x, res))
    res = '\n'.join(res)
    return res