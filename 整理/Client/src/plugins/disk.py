from .base import BasePlugin

class DiskPlugin(BasePlugin):
    
    def windows(self):
        pass

    def linux(self):
        return '硬盘'