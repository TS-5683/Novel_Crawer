from get_novel._22biqu_crawler import Crawler as _22biquCrawler
from get_novel.bxwxa_crawler import Crawler as bxwxaCrawler
from get_novel.plameny_crawler import Crawler as plamenyCrawler
from get_novel.novel91_crawler import Crawler as novel91Crawler
from get_novel.biquge345_crawler import Crawler as biquge345Crawler
from get_novel.tianxi_crawler import Crawler as tianxiCrawler
import sys


def main():
    args = sys.argv
    if len(args) > 1:
        try:
            cler = eval(f'{args[1]}Crawler{(args[2], args[3])}')
        except Exception as e:
            print('输入参数错误\n', e)
            return
    else:
        cler = tianxiCrawler('谁说我是来退婚的',
                             'https://www.tianxibook.com/xiaoshuo/94331913/')

    cler.get_novel()
    del cler


if __name__ == '__main__':
    main()
