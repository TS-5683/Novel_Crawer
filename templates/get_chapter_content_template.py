from tools.random_agent import get
from xml import etree


def get_chapter_content1(self, chapter_url: str):
    # 不分页章节正文爬取
    url = self.catalog_url + chapter_url
    response = get(url, 'gbk')
    html = etree.HTML(response)

    res_ = html.xpath('//div[@class="content" and @id="content"]//text()')
    res = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
    res = list(filter(lambda x: x, res))

    res = '\n'.join(res)
    return res


def get_chapter_content2(self, chapter_url: str):
    # 分页章节正文爬取
    res = []
    i = 0

    while True:
        i += 1

        curl = chapter_url if i == 1 else f'{chapter_url[:-5]}_{i}.html'
        url = self.home_url + curl
        response = get(url, 'utf-8')
        html = etree.HTML(response)

        if i == 1:
            limit = int(html.xpath('//h1[@class="bookname"]/text()')[0][-2])

        res_ = html.xpath('//article[@class="content" and @id="article"]//text()')
        res_ = [i.strip() for i in res_ if any(char.isprintable() for char in i)]
        res_ = list(filter(lambda x: x, res_))
        res += res_

        if i == limit:
            break

    res = '\n'.join(res)
    return res
