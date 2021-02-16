from selenium import webdriver

# Windows:
driver = webdriver.Chrome(executable_path="C:\\Users\motioz\Downloads\ChromeDriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_name/4")
print(driver.find_element_by_xpath('/html/body/h1').text)

driver.close()
