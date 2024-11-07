import requests as rq
from lxml import etree
from copy import copy
import os

class Crawler:
    def __init__(self, txtpath:str, logpath:str, catalog_url:str, init=True) -> None:
        self.txtio = open(txtpath, mode='w' if init else 'a', encoding='gbk')
        self.catalog_url = catalog_url
        self.logpath = logpath
        self.init = init

        if not init:
            with open(logpath, 'r', encoding='utf-8') as f:
                self.alread_log = f.read().split('\n')
        else:
            self.alread_log = copy([])

    def __del__(self):
        if not self.txtio.closed:
            self.txtio.close()

    def get_catalog(self):
        res = copy([])

        response = rq.get(self.catalog_url)
        response.encoding = 'gbk'

        html = etree.HTML(response.text)
        lis = html.xpath('//ul[@id="section-list" and @class="section-list fix"]/li')

        for li in lis:
            title = li.xpath('.//a/text()')[0]
            link = li.xpath('.//a/@href')[0]
            
            if title and link:
                res.append({'title': title, 'link': link})

        return res

    def get_chapter_content(self, chapter_url:str):
        res = ''
        url = self.catalog_url + chapter_url

        response = rq.get(url)
        response.encoding = 'gbk'

        html = etree.HTML(response.text)
        res = html.xpath('//div[@class="content" and @id="content"]/text()')
        res = [i.strip() for i in res if any(char.isprintable() for char in i)]
        res = '\n'.join(res)

        return res

    def get_novel(self):
        try:
            catalog = self.get_catalog()
            for chapter in catalog:
                if chapter['title'] in self.alread_log:
                    continue
                print(chapter['title'] + '\n', file=self.txtio)
                print(self.get_chapter_content(chapter['link']) + '\n\n', file=self.txtio)
                print(chapter['title'])
                self.alread_log.append(chapter['title'])
            print('顺利完成')

        except Exception as e:
            print('中断', e)
            
        finally:
            with open(self.logpath, 'w', encoding='utf-8') as f:
                for i in self.alread_log:
                    print(i, file=f)


if __name__ == '__main__':
    output_path = '练气十万年.txt'
    init = False if os.path.exists(output_path) else True

    cler = Crawler(output_path, 'already_log.txt', 'https://www.novel91.com/book/12969/', init=init)
    cler.get_novel()
    del cler