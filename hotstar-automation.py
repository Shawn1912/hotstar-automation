from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
##options.add_argument('--disable-notifications')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])


driver = webdriver.Chrome("D:\chromedriver.exe", options = options)
action = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.hotstar.com/ca")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[5]/div").click()
time.sleep(2)
driver.find_element_by_id("email").send_keys("<your username>")
driver.find_element_by_id("password").send_keys("<your password>")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/form/button").click()
time.sleep(5)
driver.find_element_by_id("searchField").send_keys("Starplus")
 
time.sleep(5)
driver.get("https://www.hotstar.com/in/channels/starplus")
time.sleep(3)
#serial hover
serial = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[7]/div/article/a")
action.move_to_element(serial).perform()
#click on tile
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[7]/div/article/a/div[2]/span").click()
time.sleep(2)
#click play
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/a").click()                             
#fullscreen
ActionChains(driver).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
