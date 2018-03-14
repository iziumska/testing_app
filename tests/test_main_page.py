"""
This tests check main fields on the first main page
"""

import unittest
from page.aplication import Aplication
from page.expected_variables import expected_variables


class TestMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestMainPage.app = Aplication()

    @classmethod
    def tearDownClass(cls):
        TestMainPage.app.driver.close()

    def test_check_title(self):
        title = self.app.driver.find_element_by_tag_name("h1").text
        self.assertEqual(title, expected_variables["comments"])

    def test_text_new_button(self):
        text_new_button = self.app.driver.find_element_by_id("newbutton").text
        self.assertEqual(text_new_button, expected_variables["new_button"])

    def test_text_header(self):
        # this test failed("Categories" != "Категории")
        text_header = []
        row_header = self.app.driver.find_elements_by_tag_name("th")
        for th in row_header:
            text = th.text
            text_header.append(text)
        self.assertListEqual(text_header, expected_variables["list_header"])


if __name__ == '__main__':
    unittest.main()
