from playwright.sync_api import Page

class recruitment:
    def __init__(self, page:Page):
        self.page = page
        self.vacancy_link = page.get_by_role("link", name = "Vacancies")
        self.vacancy_dropdown = page.get_by_text("-- Select --").nth(1)
              
        self.vacancy_search = page.get_by_role("button", name="Search")
        self.no_record = page.locator("text = No Records Found")

        self.record = page.locator("div[role='row']")

    def click_vacancies(self):
        self.vacancy_link.click()

    def vacancy_dd(self, vacancy:str):
        self.vacancy_dropdown.click()
        self.page.get_by_role("option", name=vacancy).click()

    
    def vacancy_sear(self):
        self.vacancy_search.click()

    def get_record_count(self):
        self.page.wait_for_timeout(2000)
        return self.record.count()
    
    def is_no_record_displayed(self):
        return self.no_record.is_visible()

    def has_records(self):
        return self.get_record_count() > 0
    