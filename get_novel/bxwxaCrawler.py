from tools.random_agent import get
from lxml import etree
from get_novel.templateCrawler import Crawler as crawler


class Crawler(crawler):
    def __init__(self, novel_name: str, catalog_url: str, charset) -> None:
        super.__init__(novel_name, catalog_url, charset)

    def get_catalog(self):
        res = []

        response = get(self.catalog_url, self.charset)
        html = etree.HTML(response)
        box = html.xpath('//dl[@class="zjlist"]')[0]
        links = box.xpath('.//a')

        for link in links:
            title = link.xpath('./text()')[0]
            href = link.xpath('./@href')[0]
            if title and href:
                res.append({'title': title, 'link': href})

        return res

    def get_chapter_content(self, chapter_url: str):
        url = self.catalog_url + chapter_url
        response = get(url, self.charset)
        html = etree.HTML(response)
        res_ = html.xpath('//div[@id="content"]//text()')[3:]
        res = [i.strip() for i in res_ if any(char.isprintable() for char in i)]

        res = list(filter(lambda x: x, res))
        res = '\n'.join(res).replace('\xa0', '')
        return res
