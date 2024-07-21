from locators import Locators
from pages.home_page import Home_Page
from pages.login_page import Login_Page
from pages.myaccount_page import Myaccount_Page
from pages.search_results_page import Search_Results_Page
from pages.show_details_page import Show_Details_Page
from pages.signup_page import Signup_Page
from base import Base


def before_all(context):
    context.home_page = Home_Page()
    context.login_page = Login_Page()
    context.myaccount_page = Myaccount_Page()
    context.signup_page = Signup_Page()
    context.locators = Locators()
    context.base = Base()
    context.search_results_page = Search_Results_Page()
    context.show_details_page = Show_Details_Page()


def before_tag(context, tag):
    if tag == "registered_user":
        context.login_page.login_user()
    else:
        pass
