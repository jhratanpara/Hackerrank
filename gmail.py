from selenium import webdriver

url = "https://www.gmail.com"
chrome_driver_location = "d:\python\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
gmail_username='abbccc0520'

driver.get(url)

driver.implicitly_wait(600)
driver.find_element_by_id('identifierId').send_keys(gmail_username)
driver.find_element_by_id('identifierNext').click()
driver.implicitly_wait(60)
driver.find_element_by_name('password').send_keys('ABCD.1234')
driver.find_element_by_id('passwordNext').click()
driver.implicitly_wait(300)

# def unreademail(email):
   
#     if driver.
driver.find_elements_by_id("").send_keys('label:unread')
    
