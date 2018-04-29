from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


class SeleniumTest():
    @classmethod
    def setUpClass(cls):
        """Use Chromedriver from google repo and not pip. It's newer ad wont break!! Current ver 2.34"""
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome('/home/danw32/Documents/chromedriver', chrome_options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    # TODO: this needs to save in different directories for each line of excel sheet/every pass. It just overwrites the same png atm.
    @classmethod
    def take_screenshot_now(cls, filename):
        try:
            print "Taking screenshot..."
            cls.driver.get_screenshot_as_file(filename + '_' + now + '.png')
            cls.driver.implicitly_wait(10)

        except Exception as e:
            print e
            cls.driver.get_screenshot_as_file('error-taking-screenshot.png')