from get_novel._22biqu_crawler import Crawler as _22biquCrawler
from get_novel.bxwxa_crawler import Crawler as bxwxaCrawler
from get_novel.plameny_crawler import Crawler as plamenyCrawler
from get_novel.novel91_crawler import Crawler as novel91Crawler
import sys

def main():
    try:
        cler = eval(f'{sys.argv[1]}Crawler{(sys.argv[2], sys.argv[3], sys.argv[4])}')
    except Exception as e:
        print('输入参数错误\n', e)
        return
    cler.get_novel()
    del cler

if __name__ == '__main__':
    main()