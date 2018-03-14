"""
Tests perform a check on dublication of comment
"""


import unittest
from page.aplication import Aplication, Comment
from page.expected_variables import expected_variables

data_duplicate_comment = [["999"], ["Duplicate comment"]]


class TestDuplicateComment(unittest.TestCase):

    def setUp(self):
        self.app = Aplication()

    def tearDown(self):
        self.app.driver.close()

    def test_duplicate_comment(self):
        self.app.select_first_comment()
        self.app.duplicate_button()

        # data duplicate comment
        duplicate_number = self.app.driver.find_element_by_id("Number")
        duplicate_number.clear()
        duplicate_number.send_keys(*data_duplicate_comment[0])
        duplicate_text = self.app.driver.find_element_by_id("Text")
        duplicate_text.clear()
        duplicate_text.send_keys(*data_duplicate_comment[1])
        duplicate_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        duplicate_comment = Comment(*data_duplicate_comment[0],
                                    *data_duplicate_comment[1],
                                    duplicate_selected_categories)
        self.app.save_return()

        # check an element
        list_comments = self.app.all_comments()
        self.assertIn(duplicate_comment, list_comments)

    def test_duplicate_comment_without_changes(self):
        self.app.select_second_comment()
        self.app.duplicate_button()
        self.app.save_button()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning,
                         expected_variables["unique_number_field"])

    def test_not_selected_duplicate_comment(self):
        self.app.duplicate_button()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning,
                         expected_variables["select_one_category"])

    def test_two_items_selected(self):
        # select items for duplicate
        self.app.select_first_comment()
        self.app.select_second_comment()

        self.app.duplicate_button()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning,
                         expected_variables["select_one_category"])


if __name__ == '__main__':
    unittest.main()
