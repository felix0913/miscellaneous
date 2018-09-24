#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# 远程服务器配置
Params = {
    # 'server': '192.168.1.100',
    'server': '127.0.0.1',
    'port': 8000,
    'url': '/assets/report',
    'request_timeout': 30,
}

# 日志文件配置
PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')

ALLOWED_HOSTS = ["*"]