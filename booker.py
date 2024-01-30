from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EXPECTED
import time

rooms = {
	"1": 136158,
	"2": 136167,
	"3": 136168,
	"4": 136169,
	"5": 136170,
	"6": 136171,
	"7": 136172,
	"8": 136173
}

driver = webdriver.Chrome(service = webdriver.chrome.service.Service(ChromeDriverManager().install()))
driver.get("https://wit.libcal.com/r/accessible")
driver.implicitly_wait(3)

def submit():
	print("Submitting form")
	driver.find_element(By.XPATH, "//input[@type='submit']").click()

def login(email, password):
	time.sleep(4)
	email_box = driver.find_element(By.XPATH, "//input[@type='email']")
	email_box.send_keys(email)
	submit()
	pass_box = driver.find_element(By.XPATH, "//input[@type='password']")
	pass_box.send_keys(password)
	time.sleep(1)
	submit()
	time.sleep(5)
	driver.find_element(By.TAG_NAME, "button").click()

driver = webdriver.Chrome(service = webdriver.chrome.service.Service(ChromeDriverManager().install()))
driver.get("https://wit.libcal.com/r/accessible")

#navigate to find bookings page
driver.find_element(By.ID, 's-lc-go').click()

#access dropdown of dates
dropDown = driver.find_element(By.NAME, 'date')

#returns list of options
options = dropDown.find_elements(By.TAG_NAME, 'option')

print("Available dates:")
for date in options:
	print(date.get_attribute('value'))

r = driver.find_elements(By.XPATH, "//input[@data-eid=136173]")

print("Available times:")
for t in r:
	print(t.get_attribute('data-start'))
	t.click()
#HOLY SHIT THAT WORKED
driver.find_element(By.ID, 's-lc-submit-times').click()

login("email@wit.edu", "password")

driver.find_element(By.ID, 'terms_accept').click()

submit()

while True:
	pass

def fillForm(time, room):
	r = driver.find_elements(By.XPATH, "//input[@data-eid=136173]")
	for avail in r:
		if (avail.get_attribute('data-start') != "2"):
			print("yes")