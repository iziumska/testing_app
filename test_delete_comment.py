
import unittest
from aplication import Aplication, Comment

expected_list_text = ["Please, select one category",
                      "Selected comments deleted successfull"]


class TestDeleteComment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestDeleteComment.app = Aplication()

    @classmethod
    def tearDownClass(cls):
        TestDeleteComment.app.driver.close()

    def test_delete_comment(self):
        # select item
        text = self.app.driver.find_element_by_xpath("//*[@id='main']/div/"
                                                     "div[5]/form/table/tbody/"
                                                     "tr[1]/td[3]").text
        number = self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                       "div/div[5]/form/"
                                                       "table/tbody/"
                                                       "tr[1]/td[2]").text
        categories = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/div/div[5]/"
                                                  "form/table/tbody/tr[1]/"
                                                  "td[5]").text
        delete_comment = Comment(number, text, categories)
        self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                              "div/div[5]/form/table/tbody/"
                                              "tr[1]/td[1]/input[1]").click()

        self.app.button_delete()

        # check is comment delete
        list_comments = self.app.all_comments()
        self.assertNotIn(delete_comment, list_comments)
        self.app.button_return()

    def test_not_selected_delete_comment(self):
        # click delete
        self.app.driver.find_element_by_xpath("//*[@id='command-navigation']/"
                                              "input[3]").click()
        alert = self.app.driver.switch_to.alert
        warning = alert.text
        alert.accept()
        self.assertEqual(warning, expected_list_text[0])

    def test_two_items_selected(self):
        # select item for delete
        comment_for_deleting = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/"
                                                  "div/div[5]/form/table/"
                                                  "tbody/tr[1]")
        comment_for_deleting.find_element_by_name("SelectedId").click()

        comment2_for_deleting = \
            self.app.driver.find_element_by_xpath("//*[@id='main']/div/"
                                                  "div[5]/form/table/"
                                                  "tbody/tr[2]")
        comment2_for_deleting.find_element_by_name("SelectedId").click()

        self.app.button_delete()

        # check is comment delete
        actual_text = \
            self.app.driver.find_element_by_xpath("// *[ @ id = "
                                                  "'infoField']").text
        self.assertEqual(actual_text, expected_list_text[1])


if __name__ == '__main__':
    unittest.main()
