import unittest

from hamcrest import *


class TestExercise(unittest.TestCase):
    def should_detect_text(self):
        text = TextDetector().detect()

        assert_that(text, equal_to("Image Test Text"))
