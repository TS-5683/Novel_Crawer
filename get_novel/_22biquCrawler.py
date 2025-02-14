from get_novel.templateCrawler import Crawler as crawler
from lxml import etree
from tools.random_agent import get


class Crawler(crawler):
    def __init__(self, novel_name, catalog_url: str, charset) -> None:
        super().__init__(novel_name, catalog_url, charset)
        self.home_url = 'https://www.22biqu.com'

    def get_catalog(self):
        res = []

        response = get(self.catalog_url, self.charset)
        html = etree.HTML(response)
        pages = html.xpath('//select[@id="indexselect"]//option/@value')

        for page_link in pages:
            response = get(self.home_url + page_link, self.charset)
            html = etree.HTML(response)
            box = html.xpath('//div[@class="section-box"]')[1]
            lis = box.xpath('.//ul[@class="section-list fix"]//li')

            for li in lis:
                title = li.xpath('.//a/text()')[0]
                link = li.xpath('.//a/@href')[0]
                if title and link:
                    res.append({'title': title, 'link': link})

        return res

    def get_chapter_content(self, chapter_url: str):
        res = []

        i = 0
        pre_res_ = []
        while True:
            i += 1
            curl = chapter_url if i == 1 else f'{chapter_url[:-5]}_{i}.html'
            url = self.home_url + curl

            response = get(url, self.charset)
            html = etree.HTML(response)
            res_ = html.xpath('//div[@class="content" and @id="content"]//text()')
            res_ = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
            res_ = list(filter(lambda x: x, res_))

            if pre_res_ and pre_res_[0] == res_[0]:
                break
            pre_res_ = res_
            res += res_

        res = '\n'.join(res)
        return res
