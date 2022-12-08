from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.base_url = base_url
        self.open_home_page()
        self.session = SessionHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # if not (wd.current_url.endswith('/addressbook/') and len(wd.find_elements("text", "Last name")) > 0):
        wd.get(self.base_url)
        # wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()