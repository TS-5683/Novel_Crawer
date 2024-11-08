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
        selection = html.xpath('//select[@id="indexselect"]')[0]
        pages = selection.xpath('./option/@value')

        for page_link in pages:
            rq.get(self.home_url + page_link, headers=get())
            response.encoding = 'utf-8'
            html = etree.HTML(response.text)
            links = html.xpath('//div[@id="content_1"]/a')

            for link in links:
                title = link.xpath('.//text()')[0]
                href = link.xpath('./@href')[0]
                if title and href:
                    res.append({'title': title, 'link': href})

        return res

    def get_chapter_content(self, chapter_url:str):
        res = []
        chapter_urls = [f'{chapter_url[:-5]}_1.html', f'{chapter_url[:-5]}_2.html']

        for i, curl in enumerate(chapter_urls):
            url = self.home_url + curl
            response = rq.get(url, headers=get())
            response.encoding = 'utf-8'
            html = etree.HTML(response.text)
            res_ = html.xpath('//div[@id="booktxt"]//text()')
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
    novel_name = '人在大唐已被退学'
    catalog_url = 'https://www.qiluwx.com/wx/2353_1.html'
    home_url = 'https://www.qiluwx.com'

    cler = Crawler(novel_name, home_url, catalog_url)
    with open('textFile.txt', 'w', encoding='utf-8') as f:
        print(cler.get_chapter_content('/wx/2353/2190629.html'), file=f)
    del cler