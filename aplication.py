from selenium.webdriver.chrome.webdriver import WebDriver as chrome
from selenium.webdriver.firefox.webdriver import WebDriver as firefox


class Aplication:

    def __init__(self):
        self.driver = chrome(executable_path="./resource/chromedriver.exe")
        # self.driver = firefox(executable_path="./resource/geckodriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net/")

    def click_button_new(self):
        driver = self.driver

        # check and click button 'New'
        new_comment = driver.find_element_by_id("newbutton")
        new_comment.is_enabled()
        new_comment.click()

    def adding_data(self, Arguments):
        driver = self.driver

        # adding data
        driver.find_element_by_id("Text").click()
        driver.find_element_by_id("Text").send_keys(Arguments.commit_text)
        driver.find_element_by_id("Number").click()
        driver.find_element_by_id("Number").send_keys(Arguments.number)

    def button_all_categories(self):
        driver = self.driver

        # check button 'AllCategories' and click
        button_allSelected = driver.find_element_by_name("AllSelect")
        button_allSelected.is_enabled()
        button_allSelected.click()

    def button_save(self):
        driver = self.driver
        driver.find_element_by_css_selector("input.buttonAsLink").click()

    def button_refresh(self):
        driver = self.driver
        driver.find_element_by_link_text("Refresh").click()

    def button_return(self):
        driver = self.driver
        driver.find_element_by_link_text("Return").click()

    def save_return(self):
        driver = self.driver

        # save and return
        driver.find_element_by_css_selector("input.buttonAsLink").click()
        driver.find_element_by_link_text("Return").click()

    def all_comments(self):
        driver = self.driver
        place_pages = driver.find_element_by_class_name("webgrid-footer")
        count_pages = len(place_pages.find_elements_by_tag_name("a"))
        list_comments = []
        for _ in range(count_pages - 1):
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
            driver.find_element_by_link_text(">").click()

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
        return list_comments

    def select_two_categories(self):
        driver = self.driver
        driver.find_element_by_id("Active").click()
        driver.find_element_by_xpath("//*[@id="
                                     "'Categories']").click()
        driver.find_elements_by_id('Categories')[2].click()
        driver.find_element_by_name("CurSelect").click()

    def dublicate_button(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='command-navigation']/"
                                     "input[1]").click()

    def make_dublicate_comment(self):
        driver = self.driver
        # data dublicate comment
        dublicate_comment_number = \
            driver.find_element_by_id("Number").send_keys(999)
        dublicate_comment_text = driver.find_element_by_id("Text").text
        dublicate_selected_categories = \
            driver.find_element_by_id("selectedCategories").text
        dublicate_comment = [dublicate_comment_number,
                             dublicate_comment_text,
                             dublicate_selected_categories]
        return dublicate_comment

    def editing_comment_text(self):
        driver = self.driver
        # edit comment text
        driver.find_element_by_id("Text").click()
        driver.find_element_by_id("Text").clear()
        driver.find_element_by_id("Text").send_keys("Comment Text 2222")

    def button_edit(self):
        driver = self.driver
        # click edit
        driver.find_element_by_xpath("//*[@id='command-navigation']/"
                                     "input[2]").click()

    def select_item(self):
        driver = self.driver
        item = \
            driver.find_element_by_css_selector("tr.webgrid-row-style:"
                                                "nth-child(1)>"
                                                "td:nth-child(1)>"
                                                "input:nth-"
                                                "child(1)").is_selected()
        item.click()

    def button_delete(self):
        driver = self.driver
        # button delete and confirm
        driver.find_element_by_xpath("//*[@id='command-navigation']/"
                                     "input[3]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/"
                                     "div/button[1]/span").click()


class Comment:

    def __init__(self, number, text, categories):
        self.number = number
        self.text = text
        self.categories = categories

    def __eq__(self, other):
        return self.number == other.number and \
               self.text == other.text and self.categories == other.categories
