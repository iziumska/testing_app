from page.aplication import Comment

expected_variables = {"comments": "Comments",
                      "new_button": "New",
                      "list_header":
                          ["", "Number", "Comment Text",
                           "Inactive", "Categories"],
                      "select_one_category":
                          "Please, select one category",
                      "deleted_successfull":
                          "Selected comments deleted successfull",
                      "unique_number_field":
                          "Number field should be unique of empty",
                      "first_comment":
                          Comment('123', 'abc', 'Cat0; Cat1; '
                                                'Cat2; Cat3; Cat4; Cat5'),
                      "second_comment":
                          Comment('124', 'abc2', 'Cat0; Cat2'),
                      "at_list_one_category":
                          "Please, select at least one category",
                      "text_field_is_required":
                          "The Comment Text field is required.",
                      "empty_list": ["", "", ""],
                      "max_text_field":
                          "The maximum length of Comment Text field is "
                          "50 characters",
                      "contains_only_digits":
                          "Number field should contains only digits"}
