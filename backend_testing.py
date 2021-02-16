import requests

#get test
res = requests.get('http://127.0.0.1:5000/us/201')
print(res.json())
print(res.status_code)

#put test
res = requests.put('http://127.0.0.1:5000/us/202', json={"user_name":"SHay"})
print(res.json())
print(res.status_code)

#post test
res = requests.post('http://127.0.0.1:5000/us/50', json={"user_name":"dan"})
print(res.json())
print(res.status_code)

#delete test
res = requests.delete('http://127.0.0.1:5000/us/50')
print(res.json())
print(res.status_code)
