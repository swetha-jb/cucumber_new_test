from behave import given, when, then
from features.pages.login_page import LoginPage

@given("the user navigates to the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when("the user enters valid username and password")
def step_enter_credentials(context):
    context.login_page.login("admin", "password123")

@then("the user should be redirected to the dashboard")
def step_verify_login(context):
    assert context.login_page.is_dashboard_displayed(), "Dashboard not displayed"