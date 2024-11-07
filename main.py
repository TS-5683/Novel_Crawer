from get_novel._22biqu_crawler import Crawler
import os

output_path = '顶级气运，悄悄修炼千年/顶级气运，悄悄修炼千年.txt'
logpath = '顶级气运，悄悄修炼千年/already_log.txt'
catalog_url = 'https://www.22biqu.com/biqu42190/'
home_url = 'https://www.22biqu.com'
init = False if os.path.exists(output_path) and os.path.exists(logpath) else True

cler = Crawler(output_path, logpath, home_url, catalog_url, init=init)
print(cler.get_novel())
del cler