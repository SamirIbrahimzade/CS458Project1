from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#path of chrome driver
DRIVER_PATH = 'chromedriver_win32/chromedriver.exe'

#options of driver
options = Options()
#options.headless = True
options.add_argument("--window-size=1400,700")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#get url to driver
URL = "http://localhost/netflix/login.php"
driver.get(URL)

#mail, password inputs and login button defined
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")


#test case 1 ==> testing to left some of the fields blank
# 1.1 both fields are blank
time.sleep(1)
loginButton.click()
time.sleep(1)
print("test 1.1 is done")

# 1.2 email field is blank
time.sleep(1)
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 1.2 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 1.3 password field is blank  
mailInput.send_keys("test@gmail.com")
loginButton.click()
time.sleep(2)
print("test 1.3 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

#test case 2 ==> invalid field fillings testing
# 2.1 email field is invalid
# 2.1.1 email does not contain @
time.sleep(5)
mailInput.send_keys("testgmail.com")
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 2.1.1 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 2.1.2 email ends with @
time.sleep(1)
mailInput.send_keys("test@")
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 2.1.2 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 2.1.3 email does not contain .
time.sleep(1)
mailInput.send_keys("test@gmailcom")
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 2.1.3 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 2.1.4 email ends with .
time.sleep(1)
mailInput.send_keys("test@gmailcom.")
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 2.1.4 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 2.1.5 email does not contain character before @
time.sleep(1)
mailInput.send_keys("@gmailcom.")
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 2.1.5 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 2.2 password field is invalid
# 2.2.1 password length is less than 4
time.sleep(1)
mailInput.send_keys("test@gmail.com")
passwordInput.send_keys("123")
loginButton.click()
time.sleep(1)
print("test 2.2.1 is done")

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)

# 2.2.2 password length is more than 60 
time.sleep(1)
mailInput.send_keys("test@gmail.com")
passwordInput.send_keys("123456789012345678901234567890123456789012345678901234567890123")
loginButton.click()
time.sleep(1)
print("test 2.2.2 is done")