#
#
#
#
#

# 获取任务目录
import json
import os


from qspider.settings import TASK_FILE_DIR
from qspider.status.status_data_ctl import StatusAndData


def get_file_path(qq, code):
    qq.code = code
    qq.data = os.listdir(TASK_FILE_DIR)
    if not qq.data:
        qq.code = '4' + code[1:]

    return None


# 读任务配置
def get_file2json(qq, code):
    qq.code = code

    data = []
    for path in qq.data:
        try:
            # print(os.path.join(TASK_FILE_DIR, path))
            with open(os.path.join(TASK_FILE_DIR, path), 'r')as f:
                temp = ''.join(f.read().split())
                data.append(json.loads(temp))
        except:
            qq.code = '4' + code[1:]
    qq.data = data
    return None


# 拆解任务
def mince_task(qq, code):
    qq.code = code
    pass


# 任务准备控制
def task_perpare(qq):
    qq.code = '0110'

    get_file_path(qq, '0111')
    print(qq.json())

    get_file2json(qq, '0112')
    print(qq.json())

    mince_task(qq, '0113')
    print(qq.json())
    return None


if __name__ == '__main__':
    qq = StatusAndData()
    task_perpare(qq)


# ['test_task2.txt', 'test_task1.txt']