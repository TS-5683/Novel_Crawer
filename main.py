from get_novel.plameny_crawler import Crawler as PlameCrawler
from get_novel.biquge77_crawler import Crawler as BiqugeCrawler
import os

if __name__ == '__main__':
    novel_name = '我，签到万年，被美女徒弟曝光了'
    catalog_url = 'http://www.biquge77.net/32_32850/'
    home_url = 'http://www.biquge77.net'

    cler = BiqugeCrawler(novel_name, home_url, catalog_url)
    cler.get_novel()
    del cler

    # novel_name = '我不会武功'
    # output_path = f'Novels/{novel_name}/{novel_name}.txt'
    # logpath = f'Novels/{novel_name}/already_log.txt'
    # catalog_url = 'https://www.plameny.com/plabook/hgyyj/'
    # home_url = 'https://www.plameny.com'

    # if not os.path.exists(f'Novels/{novel_name}'):
    #     os.mkdir(f'Novels/{novel_name}')
    # init = False if os.path.exists(output_path) and os.path.exists(logpath) else True

    # cler = PlameCrawler(output_path, logpath, home_url, catalog_url, init=init)
    # cler.get_novel()
    # del cler