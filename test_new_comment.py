"""
The tests perform a check for entering a new comment
"""

import unittest
from arguments import Arguments
from aplication import Aplication, Comment


new_comment_data = [["abc", "123"], ["abc2", "124"],
                    ["abc3", "125"], ["", "125"],
                    ["ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
                     ""], ["abc4", "-1"], ["abc5", "1000"]]
expected_list = \
    [Comment("123", "abc", "Cat0; Cat1; Cat2; Cat3; Cat4; Cat5"),
     Comment("124", "abc2", "Cat0; Cat2"),
     "Please, select at least one category",
     "The Comment Text field is required.", ["", "", ""],
     "The maximum length of Comment Text field is 50 characters",
     "Number field should contains only digits",
     "Number field should be unique of empty", "Save & Return"]


class TestNewComment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestNewComment.app = Aplication()

    @classmethod
    def tearDownClass(cls):
        TestNewComment.app.driver.close()

    def test_empty_field_comment(self):
        self.app.click_button_new()
        text_field_comment = self.app.driver.find_element_by_id("Text").text
        self.assertEqual(text_field_comment, "")
        self.app.button_return()

    def test_empty_field_number(self):
        self.app.click_button_new()
        text_field_number = self.app.driver.find_element_by_id("Number").text
        self.assertEqual(text_field_number, "")
        self.app.button_return()

    def test_empty_field_categories(self):
        self.app.click_button_new()
        text_field_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        self.assertEqual(text_field_selected_categories, "")
        self.app.button_return()

    def test_new_comment(self):
        # check for entering a new comment with a choice of all categories
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[0]))
        self.app.button_all_categories()
        self.app.save_return()

        # check an element
        list_comments = self.app.all_comments()
        self.assertIn(expected_list[0], list_comments)

    def test_new_comment_two_categories(self):
        # check for entering a new comment with two categories
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[1]))
        self.app.select_two_categories()
        self.app.save_return()

        # check an element
        list_comments = self.app.all_comments()
        self.assertIn(expected_list[0], list_comments)

    def test_new_comment_without_categories(self):
        # check for entering a new comment with no categories
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[2]))
        self.app.button_save()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_list[2])
        self.app.button_return()

    def test_new_comment_text_comment(self):
        # check for entering a new comment with no text comment
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[3]))
        self.app.button_save()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_list[3])
        self.app.button_return()

    def test_button_refresh(self):
        # check for entering a new comment with no text comment
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[0]))
        self.app.button_refresh()
        text_field_comment = self.app.driver.find_element_by_id("Text").text
        text_field_number = self.app.driver.find_element_by_id("Number").text
        text_field_selected_categories = \
            self.app.driver.find_element_by_id("selectedCategories").text
        empty_fields = [text_field_comment, text_field_number,
                        text_field_selected_categories]
        self.assertListEqual(empty_fields, expected_list[4])
        self.app.button_return()

    def test_invalid_text_comment(self):
        # check for entering a new comment with invalid text comment
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[4]))
        block_warning = \
            self.app.driver.find_element_by_class_name("field-"
                                                       "validation-error")
        warning = block_warning.find_element_by_tag_name("span").text
        self.assertEqual(warning, expected_list[5])
        self.app.button_return()

    def test_negative_number_comment(self):
        # check for entering a new comment with negative number comment
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[5]))
        self.app.select_two_categories()
        self.app.button_save()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_list[6])
        self.app.button_return()

    def test_max_number_comment(self):
        # check for entering a new comment with max value number comment
        self.app.click_button_new()
        self.app.adding_data(Arguments(*new_comment_data[6]))
        self.app.select_two_categories()
        self.app.button_save()
        warning = self.app.driver.find_element_by_id("errorfield").text
        self.assertEqual(warning, expected_list[7])
        self.app.button_return()


if __name__ == '__main__':
    unittest.main()
