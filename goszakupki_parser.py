import time

from playwright.sync_api import sync_playwright

class GoszakupkiParse:
    def __init__(self):
        self.list = []

    def get_info(self):
        self.page.wait_for_selector('table[class="table table-striped table-bordered"]')
        table = self.page.query_selector('table[class="table table-striped table-bordered"]')
        rows = table.query_selector_all('tr')[1:]

        for row in rows:
            td = row.query_selector_all('td')
            num = td[0].text_content()
            organization = td[1].text_content()
            type_of = td[2].text_content()
            price = td[4].text_content()
            self.list.append({
                'num': num,
                'organization': organization,
                'type_of': type_of,
                'price': price
            })
        time.sleep(2)
        self.page.keyboard.press("Escape")
        self.show_info()
        # self.get_file()

    # self.page.wait_for_selector('table[class="table table-striped"]')
    # table_files = self.page.query_selector('table[class="table table-striped"]')
    # def get_file(self):
    #     table_files = self.page.locator(
    #         'xpath=//*[contains(text(),"Документы")]/following::table[1]'
    #     )
    #
    #     rows_files = table_files.locator('tr')
    #     for i in range(rows_files.count()):
    #         row = rows_files.nth(i)
    #         link = row.locator('a')
    #
    #         if link.count() > 0:
    #             link.nth(1).click()

    def parse(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            self.context = browser.new_context()
            self.page = self.context.new_page()
            self.page.goto('https://goszakupki.by/etrade/1710312')
            self.page.query_selector('button[class="btn btn-primary btn-block col-md-6"]').click()
            self.get_info()
            time.sleep(5)



    def show_info(self):
        for item in self.list:
            print(f'№ Закупки: {item["num"]}\nОрганизация: {item["organization"]}\nВид процедуры закупки: {item["type_of"]}\nСтоимость: {item["price"]}\n\n')

if __name__ == "__main__":
    GoszakupkiParse().parse()
