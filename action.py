# -*- coding: utf-8 -*-


from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time as t


class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        return 'webDdriver'

    def find_element(self, *loc):
        # 定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
        # 例如:
        # find_element(*self.native_caixun)
        #
        # :param loc: 元组类型,结构必须是(By.NAME, u'财讯')
        # :return: element
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            return element
        except NoSuchElementException as e:
            print('Error details:%s') % (e.args[0])

    def find_elements(self, *loc):

        # 定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
        # 例如:
        # find_elements(*self.native_caixun)
        #
        # :param loc: 元组类型,结构必须是(By.NAME, u'财讯')
        # :return: elements

        try:
            # return self.driver.find_elements(*loc)
            elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
            return elements
        except NoSuchElementException as e:
            print('Error details :%s') % (e.args[0])

    def get_title(self):
        """
        获取页面的标题
        :return: str, 页面的标题
        """
        title = self.find_elements(*config.COMMON['view_title'])[0].text
        return title

    @property
    def wait(self):
        t.sleep(5)

    def getScreenshot(self, name, url, form='png'):
        t.sleep(2)
        self.driver.get_screenshot_as_file(url + name + "." + form)

    def sysback(self):
        """
        系统的返回按钮
        :return: None
        """
        self.driver.keyevent(4)

    def get_size(self):
        """
        获取当前屏幕的分辨率
        :return: int, x*y
        """
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        """
        从下往上滑动
        :return: None
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        """
        从上往下滑动
        :return: None
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        """
        从右往左滑动
        :return: None
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        """
        从左往右滑动
        :return: None
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def getLocation(self, *loc):
        """
        获取元素的定位信息,外部调用传入元组参数必须有*,
        例如:
        (*self.native_caixun)
        :param loc: 元素的定位方式
        :return: list, [x, y]
        """
        locaX = self.find_element(*loc).location.get('x')
        locaY = self.find_element(*loc).location.get('y')
        rst = [locaX, locaY]
        return rst

    def imp_wait(self, time):
        self.driver.implicitly_wait(time)

