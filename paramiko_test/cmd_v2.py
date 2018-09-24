import paramiko

def get_host_info(file):
    f = open(file, 'r')
    ip_info_dict = {}
    for line in f:
        ip = line.split()[0]
        user = line.split()[1]
        passwd = line.split()[2]
        ip_info_dict[ip] = [user, passwd]
    return ip_info_dict

def get_cmd_output(ip, user, passwd,cmd):
    global client
    client.connect(hostname= ip, port=22, username= user,password=passwd, timeout=10)
    stdin, stdout, stderr = client.exec_command(cmd)
    result= '%s 执行%s的输出为: %s' %(ip, cmd, stdout.read())   
    client.close()
    return result

if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip_info = get_host_info('ip_list')
    for key in ip_info:
        ip = key
        user = ip_info[key][0]
        passwd = ip_info[key][1]
        result = get_cmd_output(ip, user, passwd,'date')
        print(result)