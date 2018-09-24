import requests
import webbrowser
param = {'wd': '莫烦python'}
r = requests.get('http://www.baidu.com/s' , params=param)
print(r.url)


data = {'firstname': 'felix', 'lastname': 'du'}
r = requests.post(
    'http://pythonscraping.com/pages/files/processing.php', data = data
)
print(r.text)


url2 = 'http://pythonscraping.com/pages/files/processing2.php'


payload = {'username': 'felix', 'password':'password'}
r = requests.post(
    'http://pythonscraping.com/pages/cookies/welcome.php', 
    data = payload
)
print(r.cookies.get_dict())
r = requests.get(
    'http://pythonscraping.com/pages/cookies/profile.php', 
    cookies = r.cookies
)
print(r.text)