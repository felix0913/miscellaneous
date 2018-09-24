import paramiko
import requests

# 获取今天未采集的主机名
# 依赖api
result = requests.get('api_url')

# 通过paramiko链接远程服务器，执行命令
# 创建ssh对象
ssh = paramiko.SSHClient()
# 允许链接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 连接服务器
ssh.connect(hostname='c1.salt.com', 
                    port=22, 
                    username='abc',
                     password='abc')
# 执行命令
stdin,stdout,stderr = ssh.exec.command('df')
# stdin.write()

# 获取命令结果
result = stdout.read()
# 关闭连接
ssh.close()

data_dict = {result}

# 发送数据
requests.post('url_api', data=data_dict)