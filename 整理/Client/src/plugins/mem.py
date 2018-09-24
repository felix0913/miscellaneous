from .base import BasePlugin

class MemPlugin(BasePlugin):
    
    def windows(self):
        pass

    def linux(self):
        return '硬盘'