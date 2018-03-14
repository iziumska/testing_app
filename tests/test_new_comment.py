"""
The tests perform a check for entering a new comment
"""

import unittest
from page.aplication import Aplication, Arguments
from page.expected_variables import expected_variables

new_comment_data = [["abc", "123"], ["abc2", "124"],
                    ["abc3", "125"], ["", "125"],
                    ["ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
                     ""], ["abc4", "-1"], ["abc5", "1000"]]


class TestNewComment(unittest.TestCase):

    def setUp(self):
        self.app = Aplication()

    def tearDown(self):
        self.app.driver.close()

    def test_empty_field_comment(self):
        self.app.new_button()
        comment_text_field = self.app.driver.find_element_by_id("Text").text
        self.assertEqual(comment_text_field, "")

    def test_empty_field_number(self):
        self.app.new_button()
        comment_number_field = \
            self.app.driver.find_element_by_id("Number").text
        self.assertEqual(comment_number_field, "")

    def test_empty_field_categories(self):
        self.app.new_button()
        comment_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        self.assertEqual(comment_selected_categories, "")

    def test_new_comment(self):
        # check for entering a new comment with a choice of all categories
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[0]))
        self.app.button_all_categories()
        self.app.save_return()

        # check an element
        list_comments = self.app.all_comments()
        self.assertIn(expected_variables["first_comment"], list_comments)

    def test_new_comment_two_categories(self):
        # check for entering a new comment with two categories
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[1]))
        self.app.select_two_categories()
        self.app.save_return()

        # check an element
        list_comments = self.app.all_comments()
        self.assertIn(expected_variables["second_comment"], list_comments)

    def test_new_comment_without_categories(self):
        # check for entering a new comment with no categories
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[2]))
        self.app.save_button()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_variables["at_list_one_category"])

    def test_new_comment_text_comment(self):
        # check for entering a new comment with no text comment
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[3]))
        self.app.save_button()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_variables["text_field_is_required"])

    def test_refresh_button(self):
        # check for entering a new comment with refresh button
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[0]))
        self.app.refresh_button()
        comment_text_field = self.app.driver.find_element_by_id("Text").text
        comment_number_field = self.app.driver.find_element_by_id("Number").text
        comment_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        empty_fields = [comment_text_field, comment_number_field,
                        comment_selected_categories]
        self.assertListEqual(empty_fields, expected_variables["empty_list"])

    def test_invalid_text_comment(self):
        # check for entering a new comment with invalid text comment
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[4]))
        block_warning = \
            self.app.driver.find_element_by_class_name("field-"
                                                       "validation-error")
        warning = block_warning.find_element_by_tag_name("span").text
        self.assertEqual(warning, expected_variables["max_text_field"])

    def test_negative_number_comment(self):
        # check for entering a new comment with negative number comment
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[5]))
        self.app.select_two_categories()
        self.app.save_button()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_variables["contains_only_digits"])

    def test_max_number_comment(self):
        # check for entering a new comment with max value number comment
        self.app.new_button()
        self.app.adding_data(Arguments(*new_comment_data[6]))
        self.app.select_two_categories()
        self.app.save_button()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_variables["unique_number_field"])


if __name__ == '__main__':
    unittest.main()
