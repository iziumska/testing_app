"""This tests check main fields on the first main page"""

import unittest
from aplication import Aplication

expected_list = \
    ["Comments", "New",
     ["", "Number", "Comment Text", "Inactive", "Categories"]]


class TestMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestMainPage.app = Aplication()

    @classmethod
    def tearDownClass(cls):
        TestMainPage.app.driver.close()

    def test_check_title(self):
        title = self.app.driver.find_element_by_tag_name("h1").text
        self.assertEqual(title, expected_list[0])

    def test_text_newbutton(self):
        text_newbutton = self.app.driver.find_element_by_id("newbutton").text
        self.assertEqual(text_newbutton, expected_list[1])

    def test_text_header(self):
        # this test failed("Categories" != "Категории")
        text_header = []
        row_header = self.app.driver.find_elements_by_tag_name("th")
        for th in row_header:
            text = th.text
            text_header.append(text)
        self.assertListEqual(text_header, expected_list[2])


if __name__ == '__main__':
    unittest.main()
