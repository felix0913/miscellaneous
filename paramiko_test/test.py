def get_host_info(file):
    f = open(file, 'r')
    ip_info_dict = {}
    for line in f:
        ip = line.split()[0]
        user = line.split()[1]
        passwd = line.split()[2]
        ip_info_dict[ip] = [user, passwd]
    return ip_info_dict
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip_info = get_host_info('ip_list')
print(ip_info)
for k in ip_info:
    print(k)