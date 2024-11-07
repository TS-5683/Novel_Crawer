import requests as rq
from lxml import etree
from copy import copy
import os
from tools.random_agent import get

class Crawler:
    def __init__(self, novel_name, home_url:str, catalog_url:str) -> None:
        txtpath = f'Novels/{novel_name}/{novel_name}.txt'
        logpath = f'Novels/{novel_name}/already_log.txt'
        if not os.path.exists(f'Novels/{novel_name}'):
            os.mkdir(f'Novels/{novel_name}')
        init = False if os.path.exists(txtpath) and os.path.exists(logpath) else True

        self.txtio = open(txtpath, mode='w' if init else 'a', encoding='utf-8')
        self.home_url = home_url
        self.catalog_url = catalog_url
        self.logpath = logpath

        if not init:
            with open(logpath, 'r', encoding='utf-8') as f:
                self.already_log = f.read().split('\n')
        else:
            self.already_log = copy([])

    def __del__(self):
        if not self.txtio.closed:
            self.txtio.close()

    def get_catalog(self):
        res = copy([])

        response = rq.get(self.catalog_url, headers=get())
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

    def get_chapter_content(self, chapter_url:str):
        res = []
        chapter_urls = [chapter_url, f'{chapter_url[:-5]}_2.html']

        for i, curl in enumerate(chapter_urls):
            url = self.home_url + curl
            response = rq.get(url, get())
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

    def get_novel(self):
        try:
            catalog = self.get_catalog()
            for chapter in catalog:
                if chapter['title'] in self.already_log:
                    continue
                print(chapter['title'] + '\n\n' + self.get_chapter_content(chapter['link']) + '\n\n', file=self.txtio)
                print(chapter['title'])
                self.already_log.append(chapter['title'])
            print('顺利完成')

        except Exception as e:
            print('中断', e)
            
        finally:
            with open(self.logpath, 'w', encoding='utf-8') as f:
                for i in self.already_log:
                    print(i, file=f)


if __name__ == '__main__':
    novel_name = '我，签到万年，被美女徒弟曝光了'
    catalog_url = 'http://www.biquge77.net/32_32850/'
    home_url = 'http://www.biquge77.net'

    cler = Crawler(novel_name, home_url, catalog_url)
    cler.get_novel()
    del cler