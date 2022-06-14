import os
import unittest
from pathlib import Path
from steganography import write_text, encode_image, decode_image
from time import sleep

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


class TestVisualSteganography(unittest.TestCase):

    def test_write_text(self):
        """
        Test that it can ---
            1. create new image base on given size
            2. configure font to be visible with ImageFont.trueType - (family, size, width, etc)
            3. write the text to image with draw.text
        returns an image
        """
        image = write_text("Your Secret Message Goes Here", [960, 960])
        image.save("./temp_text_image.png")
        self.assertEqual(str(type(image)), "<class 'PIL.Image.Image'>",
                         "should be <class 'PIL.Image.Image'>")
        sleep(10)
        Path("./temp_text_image.png").unlink()

    def test_encode_image(self):
        """
        Test that it can ---
            1. open an image and pull out expected properties (red_channel, green_channel, blue_channel, x_size, y_size)
            2. create an image with given text to encode (same as first test) then convert it to a binary
            3. create a blank image and iterate over it combining the 2 images above based on pixel density
            4. save newly encoded image to filesystem
        returns nonthing
        """
        pass

    def test_decode_image(self):
        """
        Test that it can ---
            1. open an encoded image & pull out the red value channel and size
            2. create a new blank image
            3. itterate over encoded image red channel for hidden message
            4. save newly decoded image to filesystem
        returns nothing
        """
        pass


if __name__ == '__main__':
    unittest.main()
