import os
import pandas as pd
from lxml import etree
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
        self.home_url = 'https://www.22biqu.com'
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
        pages = html.xpath('//select[@id="indexselect"]//option/@value')

        for page_link in pages:
            response = get(self.home_url + page_link, 'utf-8')
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

            response = get(url, 'utf-8')
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
