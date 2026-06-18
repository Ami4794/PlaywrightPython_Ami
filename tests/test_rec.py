import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.locator("body").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()