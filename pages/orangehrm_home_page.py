
from playwright.sync_api import Page, expect

class homepage:
    def __init__(self, page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name = "Upgrade")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name = "Dashboard")
        self.recruitment_link = page.get_by_role("link", name = "Recruitment")
        

    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible(timeout=2000)    
    
    def click_performance(self):
        self.performance_link.click()

    def click_dashboard(self):
        self.dashboard_link.click()

    def click_recruitment(self):
        self.recruitment_link.click()

    
