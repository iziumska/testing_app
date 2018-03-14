from selenium.webdriver.chrome.webdriver import WebDriver as chrome
from selenium.webdriver.firefox.webdriver import WebDriver as firefox


class Aplication:

    def __init__(self):
        self.driver = chrome(executable_path="../resource/chromedriver.exe")
        # self.driver = firefox(executable_path="../resource/geckodriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net/")

    def new_button(self):
        # check and click button 'New'
        new_comment = self.driver.find_element_by_id("newbutton")
        new_comment.is_enabled()
        new_comment.click()

    def save_button(self):
        self.driver.find_element_by_css_selector("input.buttonAsLink").click()

    def refresh_button(self):
        self.driver.find_element_by_link_text("Refresh").click()

    def return_button(self):
        self.driver.find_element_by_link_text("Return").click()

    def save_return(self):
        self.driver.find_element_by_css_selector("input.buttonAsLink").click()
        self.driver.find_element_by_link_text("Return").click()

    def duplicate_button(self):
        self.driver.find_element_by_xpath("//input[@value = 'Duplicate...']").click()

    def edit_button(self):
        self.driver.find_element_by_xpath("//input[@value = 'Edit..']").click()

    def delete_button(self):
        driver = self.driver
        # button delete and confirm
        driver.find_element_by_xpath("//input[@value = 'Delete']").click()
        driver.find_element_by_xpath("//div[2]/div[3]/"
                                     "div/button[1]/span").click()

    def select_first_comment(self):
        first_comment = \
            self.driver.find_element_by_css_selector("tbody td")
        first_comment.find_element_by_name("SelectedId").click()

    def select_second_comment(self):
        second_comment = \
            self.driver.find_element_by_css_selector(".webgrid-alternating-row")
        second_comment.find_element_by_name("SelectedId").click()

    def adding_data(self, Arguments):
        driver = self.driver
        driver.find_element_by_id("Text").click()
        driver.find_element_by_id("Text").send_keys(Arguments.commit_text)
        driver.find_element_by_id("Number").click()
        driver.find_element_by_id("Number").send_keys(Arguments.number)

    def button_all_categories(self):
        # check button 'AllCategories' and click
        button_all_selected = self.driver.find_element_by_name("AllSelect")
        button_all_selected.is_enabled()
        button_all_selected.click()

    def select_two_categories(self):
        driver = self.driver
        driver.find_element_by_id("Active").click()
        driver.find_element_by_xpath("//*[@id="
                                     "'Categories']").click()
        driver.find_elements_by_id('Categories')[2].click()
        driver.find_element_by_name("CurSelect").click()

    def list_comment_one_page(self, list_comments):
        driver = self.driver
        row_comment = \
            (driver.find_elements_by_class_name("webgrid-row-style")) + \
            (driver.find_elements_by_class_name("webgrid-alternating-row"))
        for td in row_comment:
            number = td.find_element_by_class_name("numbercolumn").text
            text = \
                td.find_element_by_class_name("textcolumn").text
            categories = \
                td.find_element_by_class_name("categorycolumn").text
            comment = Comment(number, text, categories)
            list_comments.append(comment)

    def all_comments(self):
        driver = self.driver
        place_pages = driver.find_element_by_class_name("webgrid-footer")
        count_pages = len(place_pages.find_elements_by_tag_name("a"))
        list_comments = []
        for _ in range(count_pages - 1):
            self.list_comment_one_page(list_comments)
            driver.find_element_by_link_text(">").click()
        self.list_comment_one_page(list_comments)
        return list_comments


class Arguments:

    def __init__(self, commit_text, number):
        self.commit_text = commit_text
        self.number = number


class Comment:

    def __init__(self, number, text, categories):
        self.number = number
        self.text = text
        self.categories = categories

    def __eq__(self, other):
        return self.number == other.number and \
               self.text == other.text and self.categories == other.categories
