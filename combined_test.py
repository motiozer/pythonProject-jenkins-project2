import requests,pymysql
from selenium import webdriver

user_id=10
res = requests.post('http://127.0.0.1:5000/us/11', json={"user_name":"Yair Ozer"})
print(res.json())
print(res.status_code)

res = requests.get('http://127.0.0.1:5000/us/11')
print(res.json())
print(res.status_code)

conn = pymysql.connect(host='remotemysql.com', port=3306, user='QzlEesltcX', passwd='wuNwg4KL7Y', db='QzlEesltcX')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
sql = "SELECT user_name,user_id FROM QzlEesltcX.users1 WHERE user_id=%s"

try:
    cursor.execute(sql, 11)
    user_name, user_id = cursor.fetchone()
    cursor.close()
    conn.close()
    print(user_name+ "  yes")
except:
    print('userID does not exist')
    cursor.close()
    conn.close()
    print(False)



# Windows:
driver = webdriver.Chrome(executable_path="C:\\Users\motioz\Downloads\ChromeDriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_name/11")
print(driver.find_element_by_xpath('/html/body/h1').text)

driver.close()
