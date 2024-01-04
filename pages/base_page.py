import os
import time
import calendar

class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def take_screenshot(self):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        timestamp = calendar.timegm(time.gmtime())
        self.driver.save_screenshot(f"results/{test_name}_{timestamp}.png")

