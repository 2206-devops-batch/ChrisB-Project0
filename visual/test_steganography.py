import unittest


class TestSum(unittest.TestCase):

    def test_sum_list(self):
        """
        Test that it can sum a list of integers
        """
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        """
        Test that it can sum a tuple of integers
        """
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")


class TestEndcodeImage(unittest.TestCase):

    def test_open_image(self):
        """
        Test that it can open a image file based on a give path
        """
        pass

    def test_getting_image_properties(self):
        """
        Test that it can output useful data about our opened image
        """
        pass

    def test_create_new_image(self):
        """
        Test that it can create a new GRB image & load/set it to the same size as our input image
        """
        pass

    def test_embeding_image(self):
        """
        Test that it can ...
        """
        pass


if __name__ == '__main__':
    unittest.main()
