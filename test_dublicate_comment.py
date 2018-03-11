"""
Tests perform a check on dublication of comment
"""


import unittest
from aplication import Aplication, Comment

data_dublicate_comment = [["999"], ["Dublicate comment"]]
expected_list_text = ["Number field should be unique of empty",
                      "Please, select one category"]


class TestDublicateComment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestDublicateComment.app = Aplication()

    @classmethod
    def tearDownClass(cls):
        TestDublicateComment.app.driver.close()

    def test_dublicate_comment(self):
        # select item for dublicate
        comment_for_dublicate = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                  "div/div[5]/form/table/"
                                                  "tbody/tr[1]")
        comment_for_dublicate.find_element_by_name("SelectedId").click()

        self.app.dublicate_button()

        # data dublicate comment
        dublicate_number = self.app.driver.find_element_by_id("Number")
        dublicate_number.clear()
        dublicate_number.send_keys(*data_dublicate_comment[0])
        dublicate_text = self.app.driver.find_element_by_id("Text")
        dublicate_text.clear()
        dublicate_text.send_keys(*data_dublicate_comment[1])
        dublicate_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        dublicate_comment = Comment(*data_dublicate_comment[0],
                                    *data_dublicate_comment[1],
                                    dublicate_selected_categories)
        self.app.save_return()

        # check an element
        list_comments = self.app.all_comments()
        self.assertIn(dublicate_comment, list_comments)
        self.app.button_return()

    def test_dublicate_comment_without_changes(self):
        # select item for dublicate
        comment_for_dublicate = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/div/"
                                                  "div[5]/form/table/"
                                                  "tbody/tr[2]")
        comment_for_dublicate.find_element_by_name("SelectedId").click()

        self.app.dublicate_button()
        self.app.button_save()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_list_text[0])
        self.app.button_return()

    def test_not_selected_dublicate_comment(self):
        self.app.dublicate_button()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning, expected_list_text[1])

    def test_two_items_selected(self):
        # select item for dublicate
        comment_for_dublicate = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                  "div/div[5]/form/"
                                                  "table/tbody/tr[1]")
        comment_for_dublicate.find_element_by_name("SelectedId").click()

        comment2_for_dublicate = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/div/"
                                                  "div[5]/form/table/"
                                                  "tbody/tr[2]")
        comment2_for_dublicate.find_element_by_name("SelectedId").click()

        self.app.dublicate_button()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning, expected_list_text[1])


if __name__ == '__main__':
    unittest.main()
