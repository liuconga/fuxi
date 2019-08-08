import allure
import pytest

import lx


def get_data():
    return [("小米", 18, 172.80), ("小狗", 10, 173.22)]


class TestLogin(object):
    driver=None
    def setup(self):
        self.lx1=lx.PageLogin()
    def teardown(self):
        self.lx1.quitdirver()

    @allure.step(title='正在进行登录测试用例')
    @pytest.mark.parametrize('name,age,height', get_data())
    def test_login(self, name, age, height):
        allure.attach("打印参数：", "姓名：{}年龄：{}身高：{}".format(name, age, height))
        print("name：%s age:%s height:%s" % (name, age, height))
        try:
            self.driver=self.lx1.get_driver()
            assert 1 == 2
        except Exception as e:
            if self.driver is not None:
                self.driver.get_screenshot_as_file('./a.png')
            with open('./a.png','rb') as f:
                allure.attach("错误截图为：",f.read(),allure.attach_type.PNG)
            raise e


