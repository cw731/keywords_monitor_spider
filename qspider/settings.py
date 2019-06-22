#
#
#
import os

BASE_DIR = os.getcwd()

# SPIDER 基础配置
SPIDER_NAME = 'spider001'
SPIDER_ID = 'spider001'



# 错误配置
# 遇到错误等待控制信号
ERROR_WAIT_CTL = True

# 监控服务器配置
VSERVER_URL = '127.0.0.1:8889'


# 模式设置:local(本地), online(在线)
MODE = 'local'
TASK_FILE_DIR = os.path.join(BASE_DIR, 'loacltask')

# REDIS 配置
REDIS_URL = ''
REDIS_USER = ''
REDIS_PASSWORD = ''
