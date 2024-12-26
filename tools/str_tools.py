import re


def chapter_info(chapter_string):
    # 正则表达式匹配章节序号和章节名称
    pattern = r'第(\d+)章[^\S\r\n]*[、，。！？；：]?[^\S\r\n]*(.*)'
    match = re.match(pattern, chapter_string)

    if match:
        # 提取章节序号和章节名称
        chapter_number = match.group(1)
        chapter_name = match.group(2).strip()
        return {
            'index': chapter_number,
            'name': chapter_name
        }
    else:
        return None
