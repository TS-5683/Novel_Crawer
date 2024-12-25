import requests as rq
from lxml import etree
from copy import copy
from tools.random_agent import get


def get_catalog1(self):
    # 分页目录爬取
    res = copy([])

    response = rq.get(self.catalog_url, headers=get(), timeout=(5, 10))
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    pages = html.xpath('//select[@id="indexselect"]//option/@value')

    for page_link in pages:
        response = rq.get(self.home_url + page_link, headers=get(), timeout=(5, 10))
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        box = html.xpath('//div[@class="section-box"]')[1]
        lis = box.xpath('.//ul[@class="section-list fix"]//li')

        for li in lis:
            title = li.xpath('.//a/text()')[0]
            link = li.xpath('.//a/@href')[0]
            if title and link:
                res.append({'title': title, 'link': link})

    return res


def get_catalog2(self):
    # 不分页目录爬取
    res = copy([])

    response = rq.get(self.catalog_url, headers=get(), timeout=(5, 10))
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    box = html.xpath('//dl[@class="zjlist"]')[0]
    links = box.xpath('.//a')

    for link in links:
        title = link.xpath('./text()')[0]
        href = link.xpath('./@href')[0]
        if title and href:
            res.append({'title': title, 'link': href})

    return res
