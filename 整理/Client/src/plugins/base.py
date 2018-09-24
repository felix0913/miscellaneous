from conf import settings
# 以三种不同形式来采集资产
class BasePlugin(object):
    def __init__(self):
        mode_list = ['SSH', 'Salt', 'Agent']
        if settings.MODE in mode_list:
            self.mode = settings.MODE
        else:
            raise Exception('配置文件错误')

    def ssh(self,cmd):
        pass
    
    def agent(self):
        pass
    
    def salt(self,cmd):
        pass

    def shell_cmd(self, cmd):
        if self.mode == 'SSH':
            ret = self.ssh('cmd')
        elif self.mode == 'Salt':
            ret = self.salt('cmd')
        else:
            ret = self.agent('cmd')
        return ret
    def execute(self):
        
        ## 提前判断平台
        # agent 模式  ssh模式或saltstack模式
        # 在配置文件中定义
        ret = self.shell_cmd('查看平台命令')
        if ret == 'win':
            return self.windows()
        elif ret == 'linux':
            return self.linux()
        else:
            raise Exception('只支持windows及linux')
        self.linux()

    def linux(self):
        raise Exception("....")