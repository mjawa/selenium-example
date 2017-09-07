from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0' }

desired_cap['browserstack.local'] = True

driver = webdriver.Remote(
    command_executor='http://manishjawa2:k18vcNSZm24ryBbzsw1E@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://localhost:8000")
if not "localhost" in driver.title:
    driver.quit()
    print driver.title
    raise Exception("Unable to load google page!")
#elem = driver.find_element_by_name("q")
#elem.send_keys("BrowserStack")
#elem.submit()
print driver.title
driver.quit()