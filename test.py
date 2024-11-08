from get_novel.novel91_crawler import Crawler

if __name__ == '__main__':
    novel_name = '民调局异闻录终结季系列（全7册）'
    home_url = 'https://novel91.com'
    catacolg_url = 'https://novel91.com/book/48152/'

    cler = Crawler(novel_name, home_url, catacolg_url)
    cler.get_chapter_content('17828323.html')
    del cler