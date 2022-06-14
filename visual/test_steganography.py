import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")


class TestEndcodeImage(unittest.TestCase):

  def test_open_image(self):
    pass

  def test_getting_image_properties(self):
    pass

  def test_create_new_image(self):
    pass

  def test_embeding_image(self):
    pass

if __name__ == '__main__':
    unittest.main()
