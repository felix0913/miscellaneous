# agent形式
# 1. 采集资产
# 2. 将资产数据发送到api（POST）

# ssh形式/salt形式
# 获取今日未采集的主机列表
# 采集资产
# 将资产
# 数据发送的api（post） 


class BaseClient(object):

    def send_data(self):
        pass
    
    def get_host(self):
        pass
    
    def process(self):
        '''
        派生类需要继承此方法，用于处理请求的入口
        '''
        raise NotImplementedError('You must implement process method.')

class SBaseClient(BaseClient):
    def get_host(self):
        pass

class Agent(BaseClient):
    def file_host(self):
        f = open('nid')
        f.read()
        f.close()
        if data:
            return data

    def process(self):
        # 采集资产
        from .plugins import pack
        data_dict = pack()
        hostname = self.file_host()
        if hostname:
            data_dict['hostname'] = hostname
        else:
            # 获取当前主机名，写入nid文件
            data_dict['hostnme'] = 'abcdefg'

        # 发送至api
        self.send_data(data_dict)


class SSh(SBaseClient):
    def process(self):
        host_list = self.get_host()
        for host in host_list:
            # 采集资产
            data_dict = {}
            # 发送至api
            self.send_data(data_dict)

class Salt(SBaseClient):
    def process(self):
        host_list = self.get_host()
        for host in host_list:
            # 采集资产
            data_dict = {}
            # 发送至api
            self.send_data(data_dict)