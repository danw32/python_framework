import driver_global


class selenium_class(driver_global.SeleniumTest):
    """**Basic selenium test as an example**"""

    def setUp(self):
        self.setUpClass()

    """more arguments can be added after 'url' like password and username and called in the run module"""
    def go_to_url(self, url):
        self.driver.get(url)
        self.take_screenshot_now("URL-screenshot")

    def teardown(self):
        self.tearDownClass()
