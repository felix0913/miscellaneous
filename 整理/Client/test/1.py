import requests

host_data = {
    'status': True,
    'data':{
        'hostname':'c1.com',
        'disk': {'status':True, 'data': 'xxx'},
        'mem': {'status': True, 'data': 'xxx'}
    }
}

requests.post(
    url='http://127.0.0.1:8000/api/asset/', 
    data = host_data
)

# requests.get('http://127.0.0.1:8000/api/asset/?key1=123')
# requests.get('http://127.0.0.1:8000/api/asset/', params={'k1':'v1'})
