from lxml import etree
from tools.str_tools import str_between
from tools.random_agent import get
from get_novel.templateCrawler import Crawler as crawler


class Crawler(crawler):
    def __init__(self, novel_name, catalog_url: str, charset) -> None:
        super.__init__(novel_name, catalog_url, charset)
        self.home_url = 'https://www.qushucheng.com/'

    def get_catalog(self):
        res = []

        response = get(self.catalog_url, 'utf-8')
        html = etree.HTML(response)
        select = html.xpath('//select[@id="indexselect"]')[0]
        pages = select.xpath('.//option/@value')

        for page_link in pages:
            response = get(self.home_url + page_link, 'utf-8')
            html = etree.HTML(response)
            box = html.xpath('//ul[@class="section-list fix"]')[1]
            lis = box.xpath('.//a')

            for li in lis:
                title = li.xpath('.//text()')[0]
                link = li.xpath('.//@href')[0]
                if title and link:
                    res.append({'title': title, 'link': link})

        return res

    def get_chapter_content(self, chapter_url: str):
        url = self.home_url + chapter_url
        response = get(url, 'utf-8')
        res = str_between(response, '<div class="content" id="content">', '</div>')
        res = res.replace('<p>', '').split('</p>')
        res = [i.strip() for i in res if any(char.isprintable() for char in i)]
        res = '\n'.join(res)
        return res
