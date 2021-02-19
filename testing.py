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
URL = "https://cs458proj1.herokuapp.com/login.php"
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

#refreshing state
driver.get(URL)
time.sleep(3)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(3)



# test case 3 ==> unmatching email and password testing
# the users we are testing on:
# 
# email:'samir@gmail.com'   password:'2]zW}%'
# email:'subhan@gmail.com'   password:'zV6>-"'
# email:'kaan@gmail.com'   password:'HXw?4('
# email:'bilal@gmail.com'   password:'J@,4f~'

#3.1 wrong emails
#3.1.1 wrong email 1
time.sleep(1)
mailInput.send_keys("samir123@gmail.com")
passwordInput.send_keys("2]zW}%")
loginButton.click()
time.sleep(1)
print("test 3.1.1 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#3.1.2 wrong email 2
time.sleep(1)
mailInput.send_keys("subhan.ibrahimli@gmail.com")
passwordInput.send_keys("zV6>-\"")
loginButton.click()
time.sleep(1)
print("test 3.1.2 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#3.1.3 wrong email 3
time.sleep(1)
mailInput.send_keys("kaan17@ug.bilkent.edu.tr")
passwordInput.send_keys("HXw?4(")
loginButton.click()
time.sleep(1)
print("test 3.1.3 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#3.2 wrong passwords
#3.2.1 wrong password 1
time.sleep(1)
mailInput.send_keys("bilal@gmail.com")
passwordInput.send_keys("J@,44f~")
loginButton.click()
time.sleep(1)
print("test 3.2.1 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#3.2.2 wrong password 2
time.sleep(1)
mailInput.send_keys("subhan.ibrahimli@gmail.com")
passwordInput.send_keys("zzv76>-\"")
loginButton.click()
time.sleep(1)
print("test 3.2.2 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#3.2.3 wrong password 3
time.sleep(1)
mailInput.send_keys("kaan17@ug.bilkent.edu.tr")
passwordInput.send_keys("HXw123321")
loginButton.click()
time.sleep(1)
print("test 3.2.3 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)



# test case 4 ==> unexisting users testing
#4.1 unexisting user 1
time.sleep(1)
mailInput.send_keys("gamer2334@outlook.com")
passwordInput.send_keys("bEsTgAmEr")
loginButton.click()
time.sleep(1)
print("test 4.1 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#4.2 unexisting user 2
time.sleep(1)
mailInput.send_keys("frank@yahoo.com")
passwordInput.send_keys("qwerty123")
loginButton.click()
time.sleep(1)
print("test 4.2 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#4.3 unexisting user 3
time.sleep(1)
mailInput.send_keys("john@gmail.com")
passwordInput.send_keys("123456")
loginButton.click()
time.sleep(1)
print("test 4.3 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)


# test case 5 ==> correct email and correct password testing
#                 logout testing

# the users we are testing on:
# 
# email:'samir@gmail.com'   password:'2]zW}%'
# email:'subhan@gmail.com'   password:'zV6>-"'
# email:'kaan@gmail.com'   password:'HXw?4('
# email:'bilal@gmail.com'   password:'J@,4f~'

#test5
#5.1 existing user 1
time.sleep(1)
mailInput.send_keys("samir@gmail.com")
passwordInput.send_keys("2]zW}%")
loginButton.click()
time.sleep(2)
logoutButton = driver.find_element_by_id("homeBtn")
logoutButton.click()
print("test 5.1 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)


#test5
#5.2 existing user 2
time.sleep(1)
mailInput.send_keys("subhan@gmail.com")
passwordInput.send_keys("zV6>-\"")
loginButton.click()
time.sleep(2)
logoutButton = driver.find_element_by_id("homeBtn")
logoutButton.click()
print("test 5.2 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#test5
#5.3 existing user 3
time.sleep(3)
mailInput.send_keys("kaan@gmail.com")
passwordInput.send_keys("HXw?4(")
loginButton.click()
time.sleep(2)
logoutButton = driver.find_element_by_id("homeBtn")
logoutButton.click()
print("test 5.3 is done")

#refreshing state
time.sleep(2)
mailInput = driver.find_element_by_id("email")
passwordInput = driver.find_element_by_id("password")
loginButton = driver.find_element_by_id("loginBtn")
time.sleep(2)

#test5
#5.4 existing user 4
time.sleep(1)
mailInput.send_keys("bilal@gmail.com")
passwordInput.send_keys("J@,4f~")
loginButton.click()
time.sleep(2)
logoutButton = driver.find_element_by_id("homeBtn")
logoutButton.click()
print("test 5.4 is done")

