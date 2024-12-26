from lxml import etree
import os
import pandas as pd
from tools.random_agent import get
from tools.error_here import print_cwd_traceback
from tools.str_tools import chapter_info


class Crawler:
    def __init__(self, novel_name, catalog_url: str) -> None:
        txtpath = f'novels/{novel_name}/{novel_name}.txt'
        logpath = f'novels/{novel_name}/already_log.csv'
        if not os.path.exists(f'novels/{novel_name}'):
            os.mkdir(f'novels/{novel_name}')
        init = False if os.path.exists(txtpath) and os.path.exists(logpath) else True

        self.txtio = open(txtpath, mode='w' if init else 'a', encoding='utf-8')
        self.home_url = 'https://www.biquge345.com'
        self.catalog_url = catalog_url
        self.logpath = logpath

        if not init:
            with open(logpath, 'r', encoding='utf-8') as f:
                df = pd.read_csv(f)
                self.already_log = {'index': df['index'].tolist(), 'name': df['name'].tolist()}
        else:
            self.already_log = {'index': [], 'name': []}

    def __del__(self):
        if not self.txtio.closed:
            self.txtio.close()

    def get_catalog(self):
        res = []

        response = get(self.catalog_url, 'utf-8')
        html = etree.HTML(response)
        box = html.xpath('//ul[@class="info"]')[0]
        links = box.xpath('.//a')
        print()

        for link in links:
            title = link.xpath('./text()')[0]
            href = link.xpath('./@href')[0]
            if title and href:
                res.append({'title': title, 'link': href})

        return res

    def get_chapter_content(self, chapter_url: str):
        url = self.home_url + chapter_url
        response = get(url, 'utf-8')
        html = etree.HTML(response)

        res_ = html.xpath('//div[@class="txt" and @id="txt"]//text()')
        res = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
        res = list(filter(lambda x: x, res))[1:]

        res = '\n'.join(res)
        return res

    def get_novel(self):
        try:
            catalog = self.get_catalog()
            for chapter in catalog:
                info = chapter_info(chapter['title'])
                if info['index'] in self.already_log['index']:
                    continue
                print(chapter['title'] + '\n\n' + self.get_chapter_content(chapter['link'])
                      + '\n\n', file=self.txtio)
                print(chapter['title'])
                self.already_log['index'].append(info['index'])
                self.already_log['name'].append(info['name'])
            print('顺利完成')
        except Exception as e:
            print_cwd_traceback(e.__traceback__)
            print('中断', e)
        finally:
            with open(self.logpath, 'w', encoding='utf-8') as f:
                pd.DataFrame(self.already_log).to_csv(f, index=False)
