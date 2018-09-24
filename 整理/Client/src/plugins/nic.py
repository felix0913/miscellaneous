from .base import BasePlugin

class NicPlugin(BasePlugin):
    
    def windows(self):
        pass

    def linux(self):
        return '硬盘'