import unittest

from hamcrest import *

from code import TextDetector


class TestExercise(unittest.TestCase):
    def test_should_detect_text(self):
        text = TextDetector().detect()

        assert_that(text, equal_to("Image Test Text"))
