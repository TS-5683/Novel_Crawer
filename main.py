from get_novel._22biqu_crawler import Crawler as _22biquCrawler
from get_novel.bxwxa_crawler import Crawler as bxwxaCrawler
from get_novel.beqege_crawler import Crawler as beqegeCrawler
from get_novel.biquge77_crawler import Crawler as biquge77Crawler
from get_novel.plameny_crawler import Crawler as plamenyCrawler
import sys

def main():
    cler = eval(f'{sys.argv[1]}Crawler{(sys.argv[2], sys.argv[3], sys.argv[4])}')
    cler.get_catalog()

if __name__ == '__main__':
    main()