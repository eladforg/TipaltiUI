import time


from webbrowser import Chrome

from _pytest.fixtures import fixture

from pages.login_page import LoginPage



class TestBase:
    # usually for initializing the creation of pages to the tests:

    @fixture
    def login(self):
        p_login = LoginPage(self.driver)
        p_login.login("standard_user", "secret_sauce")
        time.sleep(1)



