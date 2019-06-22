#
#
#

from qspider.settings import MODE
from qspider.status.status_data_ctl import StatusAndData


def main():
    qq = StatusAndData()
    if MODE == 'loacl':
        qq.code = '0100'
        pass

    while True:
        qq.code = '0200'
        pass


if __name__ == '__main__':
    main()