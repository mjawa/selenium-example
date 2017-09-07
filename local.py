from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import firefox_binary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver



desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0' }

desired_cap['browserstack.local'] = True

driver = webdriver.Chrome("/Users/manishjawa/Downloads/chromedriver")
#driver = webdriver.Firefox(executable_path="/Users/manishjawa/Downloads/geckodriver")
#driver = webdriver.Safari()

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()