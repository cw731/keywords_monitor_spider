#
#
# 状态码和数据控制
#
# todo 向监控服务器上传数据
# TODO 需要包装 self.code 在每次改变值时 就自动上传数据 seter geter
# todo 日志分级最后一位变动本地打印 时间
from qspider.settings import SPIDER_ID, SPIDER_NAME, BASE_DIR


class StatusAndData:

    def __init__(self):

        self.code = ''
        self.data = ''
        self.code_info = self._get_code_info

        self._code_list = None
        self._name = ''
        self._id = ''
        self._get_code_list()
        self._get_id_name()

    def json(self):
        return {
            'code': self.code,
            'code_info': self.code_info(),
            'data': self.data
        }

    def up_data(self):
        # 向监控服务器上传数据
        data = {
            'id': self._id,
            'name': self._name,
            'code': self.code,
            'code_info': self.code_info(),
            # 'data': self.data
        }

    def _get_code_list(self):
        with open(BASE_DIR + '/status/status_codes.txt', 'r')as f:
            self._code_list = f.read().split('\n')

    def _get_code_info(self):

        for code in self._code_list:
            if self.code in code:
                return code[5:]

    def _get_id_name(self):
        self._name = SPIDER_NAME
        self._id = SPIDER_ID


if __name__ == '__main__':
    a = StatusAndData()
    a.code = '2000'
    print(a.code_info())
    print(a.json())
