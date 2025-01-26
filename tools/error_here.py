import traceback
import os


def print_cwd_traceback(tb):
    """
    打印异常堆栈跟踪，但只包括当前工作目录中的文件。

    :param tb: traceback对象
    """

    frames = traceback.extract_tb(tb)
    cwd = os.getcwd()
    for frame in frames:
        filename = frame.filename
        if filename.startswith(cwd):
            traceback.print_tb(tb, limit=None)
