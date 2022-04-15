import time

from selenium.webdriver.common.by import By


class Chose:
    def chose_chine(driver, element, chanle):
        # driver  浏览器对象
        # element 元素对象
        # chanle  选择的文本内容
        element.click()
        time.sleep(3)
        # xpth = '//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[3]/div/div/div/input'
        xpath = "//*[@class='el-select-dropdown el-popper']//*[text()='{}']".format(chanle)
        driver.find_element(By.XPATH, xpath).click()