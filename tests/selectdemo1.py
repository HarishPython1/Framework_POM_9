import pytest

from pages.selectdemopage import SelectDemoPage


@pytest.mark.usefixtures("test_setup")
class TestSelectDemo1:
    def test_selctdemo(self):
        driver = self.driver
        fb=SelectDemoPage(driver)
        fb.select_day()
        fb.select_month()
        fb.select_year()