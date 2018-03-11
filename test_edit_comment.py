"""
The tests perform a check for editing comment
"""

import unittest
from aplication import Aplication, Comment

new_data = [["Edit comment", "555"], ["Edit comment2", "777"]]
expected_list_text = ["Please, select one category", ]


class TestEditComment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestEditComment.app = Aplication()

    @classmethod
    def tearDownClass(cls):
        TestEditComment.app.driver.close()

    def test_edit_comment(self):
        # select item
        self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                              "div/div[5]/form/table/"
                                              "tbody/tr[1]/td[1]/"
                                              "input[1]").click()

        self.app.button_edit()

        # data edit comment
        edit_text = self.app.driver.find_element_by_id("Text")
        edit_text.clear()
        edit_text.send_keys(new_data[0][0])
        edit_number = self.app.driver.find_element_by_id("Number")
        edit_number.clear()
        edit_number.send_keys(new_data[0][1])
        edit_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        edit_comment = Comment(new_data[0][1], new_data[0][0],
                               edit_selected_categories)
        self.app.save_return()

        # check is comment edit
        list_comments = self.app.all_comments()
        self.assertIn(edit_comment, list_comments)
        self.app.button_return()

    def test_is_old_comment_change(self):
        # select item
        text = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                  "div/div[5]/form/table/"
                                                  "tbody/tr[1]/td[3]").text
        number = self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                       "div/div[5]/form/"
                                                       "table/tbody/tr[1]/"
                                                       "td[2]").text
        categories = self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                           "div/div[5]/form/"
                                                           "table/tbody/"
                                                           "tr[1]/td[5]").text
        old_comment = Comment(number, text, categories)
        self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                              "div/div[5]/form/table/tbody/"
                                              "tr[1]/td[1]/input[1]").click()
        self.app.button_edit()

        # data edit comment
        edit_text = self.app.driver.find_element_by_id("Text")
        edit_text.clear()
        edit_text.send_keys(new_data[1][0])
        edit_number = self.app.driver.find_element_by_id("Number")
        edit_number.clear()
        edit_number.send_keys(new_data[1][1])
        self.app.save_return()

        # check is no old comment
        list_comments = self.app.all_comments()
        self.assertNotIn(old_comment, list_comments)
        self.app.button_return()

    def test_not_selected_edit_comment(self):
        self.app.button_edit()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning, expected_list_text[0])

    def test_two_items_selected(self):
        # select item for edit
        comment_for_editing = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/div/"
                                                  "div[5]/form/table/"
                                                  "tbody/tr[1]")
        comment_for_editing.find_element_by_name("SelectedId").click()

        comment2_for_editing = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/div/"
                                                  "div[5]/form/table/"
                                                  "tbody/tr[2]")
        comment2_for_editing.find_element_by_name("SelectedId").click()

        self.app.button_edit()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning, expected_list_text[0])


if __name__ == '__main__':
    unittest.main()
