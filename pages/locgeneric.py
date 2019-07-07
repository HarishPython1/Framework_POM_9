import moment
import allure
import os
import xlrd
from selenium.webdriver import ActionChains

from testdata import data as data


class LocGeneric:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_element_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_element_by_xpath(locator_val)
            elif loc_type == "tagname":
                ele = self.driver.find_element_by_tag_name(locator_val)
            return ele
        except AssertionError as e:
            self.report_fail
        except:
            self.report_fail()

    def get_screenshot(self):
        cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        test_name = data.whoami()
        screenshot_name = test_name + "_" + cur_time

        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file(
            os.getcwd().replace("\\", "/") + "/screenshots/" + screenshot_name + ".png")
        print(os.getcwd().replace("\\", "/").replace("tests", "screenshots") + "/" + screenshot_name + ".png")

    def report_pass_fail(self, actual_val, expected_val):
        self.get_screenshot()
        assert actual_val == expected_val

    def report_fail(self):
        self.get_screenshot()

    def switch_to_frame_custom(self,loc_type,locator_val):
        frame = self.locator(loc_type,locator_val)
        self.driver.switch_to.frame(frame)

    def move_src_dest(self,src_loc_type,src_loc_val,dest_loc_type,dest_loc_val):
        a = ActionChains(self.driver)
        src_element = self.locator(src_loc_type,src_loc_val)
        des_element=self.locator(dest_loc_type,dest_loc_val)
        a.drag_and_drop(src_element, des_element).perform()

    #Utility methods
    def read_data(work_book_path, Sheet_name, col_name):
        wb = xlrd.open_workbook(work_book_path)
        ws = wb.sheet_by_name(Sheet_name)
        row_count = ws.nrows
        col_count = ws.ncols
        for i in range(row_count):
            for j in range(col_count):
                if (ws.cell_value(i, j) == col_name):
                    print(ws.cell_value(i + 1, j))
            break
