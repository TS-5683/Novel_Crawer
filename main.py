from get_novel.plameny_crawler import Crawler as PlameCrawler
from get_novel.biquge77_crawler import Crawler as BiqugeCrawler

if __name__ == '__main__':
    novel_name = '我，签到万年，被美女徒弟曝光了'
    catalog_url = 'http://www.biquge77.net/32_32850/'
    home_url = 'http://www.biquge77.net'

    cler = BiqugeCrawler(novel_name, home_url, catalog_url)
    cler.get_novel()
    del cler