from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

def isInSpan(start, end, slot):
	startHour = int(start.split(":")[0])
	endHour = int(end.split(":")[0])
	startMin = int(start.split(":")[1])
	endMin = int(end.split(":")[1])




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

slotMap = {
	"08:00:00": 0, "08:30:00": 1, "09:00:00": 2,
	"09:30:00": 3, "10:00:00": 4, "10:30:00": 5,
	"11:00:00": 6, "11:30:00": 7, "12:00:00": 8,
	"12:30:00": 9, "13:00:00": 10, "13:30:00": 11,
	"14:00:00": 12, "14:30:00": 13, "15:00:00": 14,
	"15:30:00": 15, "16:00:00": 16, "16:30:00": 17,
	"17:00:00": 18, "17:30:00": 19, "18:00:00": 20,
	"18:30:00": 21, "19:00:00": 22, "19:30:00": 23,
	"20:00:00": 24, "20:30:00": 25, "21:00:00": 26,
	"21:30:00": 27
}

for slot in list(slotMap.items()):
	print(slot[0])

driver = webdriver.Chrome(service = webdriver.chrome.service.Service(ChromeDriverManager().install()))
driver.get("https://wit.libcal.com/r/accessible")
driver.implicitly_wait(3)
driver.find_element(By.ID, 's-lc-go').click()
dropDown = driver.find_element(By.NAME, 'date')
options = dropDown.find_elements(By.TAG_NAME, 'option')
print("Available dates:")
for date in options:
	print(date.get_attribute('value'))

def attemptBook(room, start):
	print(f"Booking room {room}")
	startFrame = slotMap.items
	roomSlots = driver.find_elements(By.XPATH, f"//input[@data-eid={rooms.get(room)}]")
	for slot in roomSlots:
		print(slot.get_attribute('data-start').split(" ")[1])
		if slot.get_attribute('data-start').split(" ")[1] == start:
			slot.click()

def offlineWork(room, start):
	print(f"Booking room {room}")
	roomSlots = driver.find_elements(By.XPATH, f"//input[@data-eid={rooms.get(room)}]")
	for slot in list(slotMap.items())
		print(slot)
offlineWork("7", "19:00:00")

attemptBook("6", "20:00:00")

while True:
	time.sleep(10)
	pass
