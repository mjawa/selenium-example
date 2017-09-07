from lettuce import *

from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import AssertContextManager
from lettuce import step
from selenium import webdriver
import lettuce_webdriver.webdriver



@step(u'The title of the page should contain "([^"]*)"')
def the_title_of_the_page_should_become(step, result):
    title = world.browser.title
    try:
        assert_true(step, result in title)
    except AssertionError as e:
        world.browser.quit()

@step(u'the browser should close')
def browser_should_close(step):
    world.browser.quit()

@before.all
def setUp():
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    world.browser = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

def tearDown():
    world.browser.quit()