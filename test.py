from get_novel.plameny_crawler import Crawler

if __name__ == '__main__':
    novel_name = '我不会武功'
    home_url = 'https://www.plameny.com'
    catacolg_url = 'https://www.plameny.com/plabook/hgyyj/'

    cler = Crawler(novel_name, home_url, catacolg_url)
    cler.get_novel()
    del cler