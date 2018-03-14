"""
Tests check deleting of comment
"""


import unittest
from page.aplication import Aplication
from page.expected_list import *


class TestDeleteComment(unittest.TestCase):

    def setUp(self):
        self.app = Aplication()

    def tearDown(self):
        self.app.driver.close()

    def test_delete_comment(self):
        # select item
        comment_for_delete = \
            self.app.driver.find_element_by_css_selector("tbody > "
                                                         "tr:nth-child(1)")
        text = comment_for_delete.find_element_by_class_name("textcolumn").text
        number = \
            comment_for_delete.find_element_by_class_name("numbercolumn").text
        categories = \
            comment_for_delete.find_element_by_class_name("categorycolumn").text
        delete_comment = Comment(number, text, categories)
        self.app.driver.find_element_by_name("SelectedId").click()

        self.app.delete_button()

        # check is comment delete
        list_comments = self.app.all_comments()
        self.assertNotIn(delete_comment, list_comments)

    def test_not_selected_delete_comment(self):
        self.app.driver.find_element_by_xpath("//input[@value = "
                                              "'Delete']").click()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning, SELECT_ONE_CATEGORY)

    def test_two_items_selected(self):
        # select items
        self.app.select_first_comment()
        self.app.select_second_comment()

        self.app.delete_button()

        # check is comments delete
        actual_text = \
            self.app.driver.find_element_by_xpath("// *[ @ id = "
                                                  "'infoField']").text
        self.assertEqual(actual_text, DELETED_SUCCESSFULL)


if __name__ == '__main__':
    unittest.main()
