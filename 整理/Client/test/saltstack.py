# 安装saltstack
# master准备
# 配置文件： etc/salt/master准备
# slave准备：

# 远程服务器执行命令
import subprocess
subprocess.getoutput("salt 'c1.com' cmd.run ifconfig")
# or
import salt.client
local = salt.client.localClient()
result = local.cmd('hostname', 'cmd.run', {'ifconfig'})