from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element("name", "username").click()
        wd.find_element("name", "username").clear()
        wd.find_element("name", "username").send_keys(username)
        wd.find_element("name", "password").clear()
        wd.find_element("name", "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements("link text", "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "td.login-info-left span").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)



# import pytest
# import json
# import os.path
# # import ftputil
# from fixture.application import Application
#
#
# fixture = None
# target = None
#
#
# def load_config(file):
#     global target
#     if target is None:
#         config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
#         with open(config_file) as f:
#             target = json.load(f)
#     return target
#
#
# @pytest.fixture(scope="session")
# def config(request):
#     return load_config(request.config.getoption('--target'))
#
#
# @pytest.fixture
# def app(request, config):
#     global fixture
#     browser = request.config.getoption("--browser")
#     if fixture is None or not fixture.is_valid():
#         fixture = Application(browser=browser, config=config)
#         fixture.session.ensure_login(username=config["webadmin"]["username"],
#                                  password=config["webadmin"]["password"])
#     return fixture
#
#
# @pytest.fixture(scope="session", autouse=True)
# def configure_server(request, config):
#     install_server_congiguration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
#     def fin():
#         restore_server_congiguration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
#     request.addfinalizer(fin)
#
#
# def install_server_congiguration(host, username, password):
#     with ftputil.FTPHost(host, username, password) as remote:
#         if remote.path.isfile("config_inc.php.bak"):
#             remote.remove("config_inc.php.bak")
#         if remote.path.isfile("config_inc.php"):
#             remote.rename("config_inc.php", "config_inc.php.bak")
#         remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")
#
#
# # def restore_server_congiguration(host, username, password):
# #     with ftputil.FTPHost(host, username, password) as remote:
# #         if remote.path.isfile("config_inc.php.bak"):
# #             if remote.path.isfile("config_inc.php"):
# #                 remote.remove("config_inc.php")
# #             remote.rename("config_inc.php.bak", "config_inc.php")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def stop(request):
#     def fin():
#         fixture.session.ensure_logout()
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--target", action="store", default="target.json")
#
