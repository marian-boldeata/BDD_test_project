from pages.home_page import Home_Page
from pages.login_page import Login_Page
from pages.myaccount_page import Myaccount_Page
from pages.signup_page import Signup_Page


def before_all(context):
    context.home_page = Home_Page()
    context.login_page = Login_Page()
    context.myaccount_page = Myaccount_Page()
    context.signup_page = Signup_Page()