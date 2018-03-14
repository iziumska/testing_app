from page.aplication import Comment

# test main page
COMMENTS = "Comments"

NEW_BUTTON = "New"

LIST_HEADER = ["", "Number", "Comment Text", "Inactive", "Categories"]

# test delete comment

SELECT_ONE_CATEGORY = "Please, select one category"

DELETED_SUCCESSFULL = "Selected comments deleted successfull"

# test duplicate comment

UNIQUE_NUMBER_FIELD = "Number field should be unique of empty"

# test new comment

FIRST_COMMENT = Comment("123", "abc", "Cat0; Cat1; Cat2; Cat3; Cat4; Cat5")

SECOND_COMMENT = Comment("124", "abc2", "Cat0; Cat2")

AT_LEAST_ONE_CATEGORY = "Please, select at least one category"

TEXT_FIELD_IS_REQUIRED_ = "The Comment Text field is required."

EMPTY_LIST = ["", "", ""]

MAX_TEXT_FIELD = "The maximum length of Comment Text field is 50 characters"

CONTAINS_ONLY_DIGITS = "Number field should contains only digits"
