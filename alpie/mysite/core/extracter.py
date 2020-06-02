

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver.chrome.options import Options
import os

def fetch():
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")

	driver = webdriver.Chrome(r"./chromedriver")

	driver.get("https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml")

	elem = driver.find_element_by_name("regn_no1_exact")
	elem.clear()
	elem.send_keys("HR51BL4690")


	a = driver.find_element_by_xpath('/html/body/form/div[1]/div[4]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/label').text

	if('greater' in a ):
		x = re.findall('\d+',a)
		if(int(x[0])<int(x[1])):
			val = x[1]
		else:
			val = x[0]

	elif('lesser' in a):
		x = re.findall('\d+',a)
		if(int(x[0])<int(x[1])):
			val = x[0]
		else:
			val = x[1]

	elif('*' in a):
		x = re.findall('\d+',a)
		val = int(x[0]) * int(x[1])

	elif('-' in a):
		x = re.findall('\d+',a)
		val = int(x[0]) - int(x[1])
	elif('+' in a):
		x = re.findall('\d+',a)
		val = int(x[0]) + int(x[1])


	elem1 = driver.find_element_by_name("txt_ALPHA_NUMERIC")
	elem1.clear()
	elem1.send_keys(val)


	driver.find_element_by_xpath('/html/body/form/div[1]/div[4]/div/div[2]/div/div/div[2]/div[4]/div/button').click();

	sleep(5.0)

	a=driver.find_element_by_xpath('/html/body/form/div[1]/div[4]/div/div[2]/div/div/div[2]/div[5]/div/div/div')
	print(a.text)
	driver.close()
