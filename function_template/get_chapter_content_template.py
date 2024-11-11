import requests as rq
from tools.random_agent import get
from xml import etree

# 不分页章节正文爬取
def get_chapter_content1(self, chapter_url:str):
    url = self.catalog_url + chapter_url
    response = rq.get(url, headers=get())
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
        
    res_ = html.xpath('//div[@class="content" and @id="content"]//text()')
    res = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
    res = list(filter(lambda x: x, res))
    
    res = '\n'.join(res)
    return res

# 分页章节正文爬取
def get_chapter_content2(self, chapter_url:str):
    res = []

    i = 0
    while True:
        i += 1

        curl = chapter_url if i == 1 else f'{chapter_url[:-5]}_{i}.html'
        url = self.home_url + curl
        response = rq.get(url, headers=get())
        if response.status_code != 200:
            break
        response.encoding = 'utf-8'

        html = etree.HTML(response.text)

        res_ = html.xpath('//article[@class="content" and @id="article"]//text()')
        res_ = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
        res_ = list(filter(lambda x: x, res_))
        res += res_
            
        page = html.xpath('//h1/small')
        if not page:
            break
        
    res = '\n'.join(res)
    return res