# Project 0 - Spy's Journal

In the past, you may have tried to accomplish some kind of subterfuge using invisible inks or using special keywords with your friends. \
However, as fearless coders we have access to fancier ways to sneak data around. !! Making it less likely that they’ll want to try to crack your code !!

For Example: [Steganography] is really handy to use, because people won’t even suspect that they’re looking at or listening to a secret message.

## What Is Steganography

In a nutshell, Steganography is the technique of creating secret data by hiding it within an "Ordinary, Non-Secret, File" in order to avoid detection. \
It's then extracted by the reciver at the destination if they are ware of the proper encription methods.

> Therefore, the use of steganography can be combined with encryption as an extra step for hiding or protecting data.

| Take for example, this sentence                                                           | Which gets ​turned into |
| ----------------------------------------------------------------------------------------- | ----------------------- |
| ```Since everyone can read, encoding text in neutral sentences is definitely effective``` | ```Secret inside```     |

### How You May Ask?

<details>
    <summary>Answer</summary>
    <br>
    Take the first letter of every word.
</details>

<br>

### **Aside**:

The concept of “most significant bit” (MSB) and “least significant bit” (LSB) occurs in other contexts as well. For example, [ParityBits] are used as a basic form of error checking. \
Additionally, because the LSBs will change rapidly even if the value of the bit changes a little, they are very useful for use in [HashFunctions] and [Checksums] for validation purposes.

### LSB (Least Significant Bit) Algorithm

> LSB algorithm is a classic Steganography method used to conceal the existence of secret data inside a “public” cover. \
> The LSB or “Least Significant Bit”, in computing terms, represents the bit at the unit’s place in the binary representation of a number.

<br>

## Image Steganography

> The technique use to transmit hidden information by modifying an image file.
> The image selected for this purpose is called the `cover image` and the image obtained after steganography is called the `stego image`.

<!-- In this toolbox exercise you will delve a bit deeper into the specifics of how images are created in addition to learning more about bits and binary math. \
This exercise was modified from [Interactive-Python], though this version encodes an image into another image instead of ASCII text. -->
​
### The value of one pixel
​
There are multiple ways to hide things within other things, but today we will be working with images. \
A black and white image (not grayscale) is an easy thing to conceptualize, where a black pixel has a value of 1 and a white pixel as a value of 0. \
​Color images have three color channels (RGB), with pixel values of 0-255 for each pixel. So a pixel with the value (255,255,255) would be entirely white while (0,0,0) would be black. \
The upper range is 255 because it is the largest value that can be represented by an 8 bit binary number. Binary is a base-two paradigm, in contrast to decimal which is in base-ten, \
which means you calculate the value of a binary number by summing the 2s exponent of each place where a 1 appears.
​

So if we wanted to convert the number `10001011` from binary into decimal, it would look something like:
​
```python
2^8 + 2^4 + 2^2 + 2^1 = 139
```
​
You can also test this out in your Python interpreter. Binary numbers are automatically converted to integers so you don’t actually need to have a print statement. (It’s just there for clarity.)
​
```python
>>> print(0b10001011)
139
>>> type(0b10001011)
<class 'int'>
>>> 0b00001011
11
>>> 0b10001010
138
```
​
From our quick tests above, you can see that the leftmost bit place matters a lot more than rightmost bit because the rightmost bit only modifies the value of the number by 1. We saw that:
​
```
10001011 = 139` while `00001011 = 11
10001011 = 139` while `10001010 = 138
```
​
Because of this, we describe the leftmost bit as the “most significant bit” (MSB) while the rightmost bit is the “least significant bit” (LSB). \
We can observe that its entirely possible to hide a black and white image inside an RGB image by changing the LSB of a pixel in a single color channel to correspond to the value of the image we want to hide. \
​

Additionally, since changing the LSB doesn’t drastically change the overall value of the of 8 bit number, we can hide our data without modifying a source image in any detectable sort of way. \
You can test this out with any [RGB-Color-Wheel] to get a sense of how little difference there is between a color like (150, 50, 50) and (151, 50, 50)
​
<!--
## Decoding the sample image
​
Provided in this toolbox is a picture of a cute dog. However, this dog is hiding a very secret message… can you decode it? This image is also included in the toolbox under `images/encoded_sample.png`.
​
![img](https://sd18spring.github.io/images/toolboxes/image-steganography/encoded_sample.png)
​
**Provided below is the starter code is a function called `decode_image`. The secret image was hidden in the LSB of the pixels in the red channel of the image. That is, the value of the LSB of each red pixel is 1 if the hidden image was 1 at that location, and 0 if the hidden image was also 0. Your task is to iterate though each pixel in the encoded image and set the `decode_image` pixel to be (0, 0, 0) or (255, 255, 255) depending on the value of that LSB.**
​
**You may want to look at the Python [Bin] function as you convert between integer and binary**. Remember that bin will convert an integer to a *binary string*. Also, remember that you have to isolate the `red_channel` from the original RGB image. You can do this using the `.split()` method that PIL provides.
​
```python
from PIL import Image
​
def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
​
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
​
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
​
    #TODO: Fill in decoding functionality
​
    decoded_image.save("images/decoded_image.png")
```

## Encoding a secret message
​
Now that we can decode secret messages, it’s only natural that we want to encode some too! Provided in the starter code are a pair of functions called `write_text()` and `encode_image()`. `write_text()` will take a string and convert it to a black and white image of the string. You may use it as a helper function in completing your implementation of `encode_image()`.

-->

<br>

## Audio Steganography

> The technique used to transmit hidden information by modifying an audio signal in an imperceptible manner. \
> The host message before steganography and stego message after steganography have the same characteristics. \
> For, it is the science of hiding some secret text or audio information in a host message.

Further Reading: HidingSecretsWithinEarshot-[Pt1]-&-[Pt2]
### The value of one sound bite

```python
  # Convert text to bit array
  bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in text])))

  # Replace LSB of each byte of the audio data by one bit from the text bit array
  for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
  # Get the modified bytes
  frame_modified = bytes(frame_bytes)

  # Write bytes to a new wave audio file
  with wave.open(f'../audio/{encoded_name}.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
```

---
## Encoding & Decoding Secret Messages

> source venv/bin/activate
> pip3 install -r requirements.txt

> Python3 visual/steganography.py

or

> Python3 vocal/steganography.py

> deactivate

### Final Notes

- `Images` in this example are `.png` files. We recommend that you avoid working with `.jpg` files so that file compression does not make your task more difficult.
- `Audio` in this example are `.wav` files. We recommend that you avoid working with `.mp4` files so that file compression does not make your task more difficult.

<!-- Resources -->
[Steganography]: https://en.wikipedia.org/wiki/Steganography

[HashFunctions]: https://en.wikipedia.org/wiki/Hash_function
[ParityBits]: https://en.wikipedia.org/wiki/Parity_bit
[Checksums]: https://en.wikipedia.org/wiki/Checksum

<!-- [Interactive-Python]: http://interactivepython.org/runestone/static/everyday/2013/03/1_steganography.html -->
[RGB-Color-Wheel]: http://www.colorspire.com/rgb-color-wheel

[ADUIO-STEGANOGRAPHY]: https://gist.github.com/sumit-code/c3d5f27fdeda44dd0922e14263ede4c4

<!-- HidingSecretsWithinEarshot -->
[Pt1]:https://medium.com/@sumit.arora/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-1-of-2-6a3bbd706e15
[Pt2]:https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3

<!-- [Bin](https://docs.python.org/3/library/functions.html#bin)  -->

<!-- [Pseudonymization] -->
[Pseudonymization]: https://en.wikipedia.org/wiki/Pseudonymization#:~:text=Pseudonymization%20is%20a%20data%20management,more%20artificial%20identifiers%2C%20or%20pseudonyms.

https://www.chciken.com/digital/signal/processing/2020/05/13/guitar-tuner.html
https://www.ideals.illinois.edu/bitstream/handle/2142/104007/ECE499-Sp2019-ding.pdf?sequence=2&isAllowed=y
https://www.connollymusic.com/stringovation/how-your-violin-produces-sound
https://www.physicscentral.com/explore/action/fiddle.cfm
http://hyperphysics.phy-astr.gsu.edu/hbase/Music/mussca.html#c2
http://hyperphysics.phy-astr.gsu.edu/hbase/Music/guita.html#c3
http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/timbre.html#c2
http://hyperphysics.phy-astr.gsu.edu/hbase/Music/violin.html#:~:text=The%20violin%2C%20the%20most%20commonly,the%20A4%20%3D%20440Hz%20standard.

<!-- Great -->
[](https://faroit.com/)
[](https://nsfwjs.com/)
[](https://www.audacityteam.org/download/)

<!-- Supplemental -->
[](https://github.com/infinitered/nsfwjs)
[](https://github.com/gantman/nsfw_model)

<!-- Other Inspiration -->
[](https://github.com/sukumo28/vscode-audio-preview)
[](https://devpost.com/software/deep-fandom)

<!-- Open CV -->
[](https://opencv.org/)
[](https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html)
[](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html)


<!-- Less Likely -->
[](https://github.com/sigsep/open-unmix-pytorch)
<!-- This repository contains the PyTorch (1.8+) implementation of Open-Unmix, a deep neural network reference implementation for music source separation, applicable for researchers, audio engineers and artists.  -->
[](https://github.com/faroit/countnet)
[](https://github.com/RocketScienceAbteilung/git-grid)
[](https://github.com/RocketScienceAbteilung/git-wig)
[](https://github.com/faroit/magiclock)
