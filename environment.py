from locators.home_page_locators import Home_page_locators
from locators.item_details_page_locators import Item_details_page_locators
from locators.login_page_locators import Login_page_locators
from locators.myaccount_page_locators import Myaccount_page_locators
from locators.search_page_locators import Search_page_locators
from locators.signup_page_locators import Signup_page_locators
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

    context.base = Base()
    context.search_results_page = Search_Results_Page()
    context.show_details_page = Show_Details_Page()

    context.login_page_locators = Login_page_locators()
    context.myaccount_page_locators = Myaccount_page_locators()
    context.search_page_locators = Search_page_locators()
    context.signup_page_locators = Signup_page_locators()
    context.home_page_locators = Home_page_locators()
    context.item_details_page_locators = Item_details_page_locators()


def before_tag(context, tag):
    if tag == "registered_user":
        context.login_page.login_user()
    else:
        pass
