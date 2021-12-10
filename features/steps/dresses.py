from behave import given, when, then 
from selenium import webdriver
from nose.tools import assert_equal, assert_true
from Pages.index import *
from Pages.dresses import *
from Pages.items import *



@given('the user is in the main page')
def step_impl(context): 
     context.browser = webdriver.Chrome('./drivers/chromedriver.exe')
     context.browser.implicitly_wait(10)
     context.browser.get('http://automationpractice.com/index.php')

@when('the user clicks on Dresses button') 
def step_impl(context):
    index = Index(context.browser)
    index.click_dresses()


@then('the user should see dresses page')   
def step_impl(context):
    dresses = Dresses(context.browser)
    assert_equal(dresses.get_category_name(), 'DRESSES ')





@when('the user searches by"{item}"')   
def step_impl(context,item):
    index = Index(context.browser)
    index.search(item)

  


@then('the user should sees "{item}" banner in the results') 
def step_impl(context,item):
    items = Items(context.browser)
    assert_true(item.upper() in items.get_banner_text())
