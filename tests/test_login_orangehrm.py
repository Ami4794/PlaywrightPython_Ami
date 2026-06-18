import re
from playwright.sync_api import Page
from pages.orangehrm_login_page import loginpage
from pages.orangehrm_home_page import homepage
from pages.orangehrm_recruitment_page import recruitment
import pytest

@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),
        ("user1", "password1")
    ],
)

def test_example(page: Page, username, password) -> None:
    

    login_page = loginpage(page)
    home_page = homepage(page)
    recruitment_page = recruitment(page)
   

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
    home_page.click_recruitment()
    
    recruitment_page.click_vacancies()
    recruitment_page.vacancy_dd("Junior Account Assistant")
       
    recruitment_page.vacancy_sear()

   
    if recruitment_page.has_records():
        print("Records found")
        print("Total Records:", recruitment_page.get_record_count())

    elif recruitment_page.is_no_record_displayed():
        print("No Records Found")

    else:
        print("Unexpected UI State")
        assert False

    

