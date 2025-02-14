import os
import pandas as pd
from tools.str_tools import chapter_info
from tools.random_agent import get
from tools.error_here import print_cwd_traceback
from lxml import etree
from get_novel.templateCrawler import Crawler as crawler


class Crawler(crawler):
    def __init__(self, novel_name, catalog_url: str, charset) -> None:
        super.__init__(novel_name, catalog_url, charset)
        self.home_url = 'https://novel91.com'

    def get_catalog(self):
        res = []

        response = get(self.catalog_url, self.charset)
        html = etree.HTML(response)
        lis = html.xpath('//ul[@id="section-list"]/li')

        for li in lis:
            title = li.xpath('.//a/text()')[0]
            link = li.xpath('.//a/@href')[0]
            if title and link:
                res.append({'title': title, 'link': link})

        return res

    def get_chapter_content(self, chapter_url: str):
        url = self.catalog_url + chapter_url
        response = get(url, self.charset)
        html = etree.HTML(response)

        res_ = html.xpath('//div[@class="content" and @id="content"]//text()')
        res = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
        res = list(filter(lambda x: x, res))

        res = '\n'.join(res)
        return res
