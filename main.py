from get_novel.biquge77_crawler import Crawler
import os

novel_name = '我，签到万年，被美女徒弟曝光了'
output_path = f'{novel_name}/{novel_name}.txt'
logpath = f'{novel_name}/already_log.txt'
catalog_url = 'http://www.biquge77.net/32_32850/'
home_url = 'http://www.biquge77.net'

if not os.path.exists(novel_name):
    os.mkdir(novel_name)
init = False if os.path.exists(output_path) and os.path.exists(logpath) else True

cler = Crawler(output_path, logpath, home_url, catalog_url, init=init)
cler.get_novel()
del cler