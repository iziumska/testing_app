"""
The tests perform a check for editing comment
"""

import unittest
from page.aplication import Aplication, Comment
from page.expected_variables import expected_variables

new_data = [["Edit comment", "555"], ["Edit comment2", "777"]]


class TestEditComment(unittest.TestCase):

    def setUp(self):
        self.app = Aplication()

    def tearDown(self):
        self.app.driver.close()

    def test_edit_comment(self):
        self.app.select_first_comment()
        self.app.edit_button()

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

    def test_is_old_comment_change(self):
        # select item
        comment_for_edit = \
            self.app.driver.find_element_by_css_selector("tbody > "
                                                         "tr:nth-child(1)")
        text = \
            comment_for_edit.find_element_by_class_name("textcolumn").text
        number = \
            comment_for_edit.find_element_by_class_name("numbercolumn").text
        categories = \
            comment_for_edit.find_element_by_class_name("categorycolumn").text
        old_comment = Comment(number, text, categories)
        self.app.driver.find_element_by_name("SelectedId").click()

        self.app.edit_button()

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

    def test_not_selected_edit_comment(self):
        self.app.edit_button()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning,
                         expected_variables["select_one_category"])

    def test_two_items_selected(self):
        # select items for edit
        self.app.select_first_comment()
        self.app.select_second_comment()

        self.app.edit_button()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning,
                         expected_variables["select_one_category"])


if __name__ == '__main__':
    unittest.main()
