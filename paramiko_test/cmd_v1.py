import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
f = open('ip_list', 'r')

for line in f:
    ip = line.split()[0]
    user = line.split()[1]
    passwd = line.split()[2]
    client.connect(hostname= ip, port=22, username= user,password=passwd, timeout=10)
    stdin, stdout, stderr = client.exec_command('date')
    print('%s output:\n %s ' %(ip, stdout.read()))