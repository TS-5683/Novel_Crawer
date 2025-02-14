from get_novel._22biquCrawler import Crawler as _22biquCrawler
from get_novel.bxwxaCrawler import Crawler as bxwxaCrawler
from get_novel.novel91Crawler import Crawler as novel91Crawler
from get_novel.biquge345Crawler import Crawler as biquge345Crawler
from get_novel.tianxiCrawler import Crawler as tianxiCrawler
from get_novel.qushuCrawler import Crawler as qushuCrawler
from get_novel.bqgwxCrawler import Crawler as bqgCrawler
import sys


def main():
    args = sys.argv
    if len(args) > 1:
        try:
            cler = eval(f'{args[1]}Crawler{(args[2], args[3], args[4])}')
        except Exception as e:
            print('输入参数错误\n', e)
            return
    else:
        cler = bqgCrawler('云边复仇', 'https://www.xbgqw.com/167_167972/', 'utf-8')

    cler.get_novel()
    del cler


if __name__ == '__main__':
    main()
