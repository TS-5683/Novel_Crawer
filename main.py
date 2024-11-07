from get_novel.novel_crawler import Crawler

cler = Crawler('练气十万年.txt', 'https://www.novel91.com/book/12969/')
print(cler.get_chapter_content('5498328.html'))
del cler