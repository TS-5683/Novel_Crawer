from get_novel._22biquCrawler import Crawler as _22biquCrawler
from get_novel.bxwxaCrawler import Crawler as bxwxaCrawler
from get_novel.novel91Crawler import Crawler as novel91Crawler
from get_novel.biquge345Crawler import Crawler as biquge345Crawler
from get_novel.tianxiCrawler import Crawler as tianxiCrawler
from get_novel.qushuCrawler import Crawler as qushuCrawler
from get_novel.bqgwxCrawler import Crawler as bqgCrawler
from get_novel.beqegeCrawler import Crawler as beqegeCrawler
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
        cler = beqegeCrawler('史上第一祖师爷', 'https://www.beqege.cc/44701/', 'utf-8')

    cler.get_novel()
    del cler


if __name__ == '__main__':
    main()
