from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usernameStr = 'cryptojagath@gmail.com'
passwordStr = 'Jagan@1986'

#identifierId
startTime = time.time()
browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

username = browser.find_element_by_name('identifier')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
nextButton.click()
time.sleep(2)

password = browser.find_element_by_name('password')
password.send_keys(passwordStr)

# wait for transition then continue to fill items
#password = WebDriverWait(browser, 10).until(
#    EC.presence_of_element_located((By.name, 'password')))
#password.send_keys(passwordStr)

signInButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
signInButton.click()

time.sleep(2)
browser.get("http://www.google.com")
input_element = browser.find_element_by_name("q")
input_element.send_keys("bigg boss telugu vote")
input_element.submit()
time.sleep(2)
voteButton = browser.find_element_by_xpath('')
voteButton.click()

input_element.submit()
endTime = time.time()
print('Total time: ',endTime-startTime)
