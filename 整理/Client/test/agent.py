import subprocess
import requests

# 采集数据
result = subprocess.getoutput('ifconfig')
# 对result进行处理

data_dict = {
    'nic': [],
    'disk': {}
    'mem': {}
}

# 发送数据
requests.post('url', data = data_dict)