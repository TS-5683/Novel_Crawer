from tools.random_agent import get
from lxml import etree
from get_novel.templateCrawler import Crawler as crawler


class Crawler(crawler):
    def __init__(self, novel_name: str, catalog_url: str, charset) -> None:
        super().__init__(novel_name, catalog_url, charset)
        self.home_url = 'https://www.bxwxa.com'

    def get_catalog(self):
        res = []

        response = get(self.catalog_url + 'mulu_999.html', self.charset)
        html = etree.HTML(response)
        select = html.xpath('//select')[0]
        cata_urls = select.xpath('.//option/@value')
        first = True

        for cata_url in cata_urls:
            response = get(self.home_url + cata_url)
            html = etree.HTML(response)
            if first:
                lis = html.xpath('//ul[@class="fix section-list"]/li')
                first = False
            else:
                lis = html.xpath('//ul[@class="section-list fix ycxsid"]/li')
            for li in lis:
                res.append({'title': li.xpath('.//text()')[0], 'link': li.xpath('.//@href')[0]})

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
