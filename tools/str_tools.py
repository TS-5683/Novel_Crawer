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
            'index': int(chapter_number),
            'name': chapter_name
        }
    else:
        return None


def str_between(string, start, end):
    """
    从字符串中提取两个字符串之间的内容。

    :param string: 待处理的字符串
    :param start: 起始字符串
    :param end: 结束字符串
    :return: 提取出的内容
    """
    start_index = string.find(start)
    if start_index == -1:
        return None
    start_index += len(start)
    end_index = string.find(end, start_index)
    if end_index == -1:
        return None
    return string[start_index:end_index]
