from selenium import webdriver
from time import sleep


class InstaBot:
	def __init__(self, username, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		sleep(1)
		self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()
		sleep(5)
		
		self.driver.find_element_by_xpath("//button[contains(text() , 'Not Now')]").click()
		print("hello")
		try :
			self.driver.find_element_by_xpath("//button[contains(text() , 'Not Now')]").click()
			print("hello2")
			while True:
				sleep(1)
				try :
					self.driver.find_element_by_xpath("//button/div/span/*[name()='svg'][@aria-label='Like']").click()
					self.driver.execute_script("window.scrollBy(0,100)")	
				except:
					self.driver.execute_script("window.scrollBy(0,100)")
		except: 
			print("hello2 e")
		
		
InstaBot("itsrobel.schwarz@gmail.com", "ras17073")
