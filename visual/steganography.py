from PIL import Image, ImageFont, ImageDraw
import textwrap


def decode_image(file_location, decoded_name):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    # Create the new image and load the pixel map
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            r = red_channel.getpixel((i, j))
            if r | 1 == r:
                decoded_image.putpixel((i, j), (0, 0, 0))
            else:
                decoded_image.putpixel((i, j), (255, 182, 193))

    decoded_image.save("images/{}.png".format(decoded_name))


def write_text(text, img_size):
    font_path = "~/Library/Fonts/Arial Unicode.ttf"

    image = Image.new("RGB", img_size)
    draw = ImageDraw.Draw(image)
    txt = text
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.95

    font = ImageFont.truetype(font_path, fontsize)
    while font.getsize(txt)[0] < img_fraction*image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)

    draw.text((25, 25), txt, font=font)  # put the text on the image
    return image


def encode_image(file_location, text, encoded_name):
    image = Image.open(file_location)
    red_channel, green_channel, blue_channel = image.split()

    x_size = image.size[0]
    y_size = image.size[1]

    # txt draw
    img_txt = write_text(text, image.size)
    bw_encode = img_txt.convert('1')

    # Create the new image and load the pixel map
    encoded_image = Image.new("RGB", image.size)
    pixels = encoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            red_channel_pix = bin(red_channel.getpixel((i, j)))
            tencode_pix = bin(bw_encode.getpixel((i, j)))

            if tencode_pix[-1] == '1':
                red_channel_pix = red_channel_pix[:-1] + '1'
            else:
                red_channel_pix = red_channel_pix[:-1] + '0'
            pixels[i, j] = (int(red_channel_pix, 2), green_channel.getpixel(
                (i, j)), blue_channel.getpixel((i, j)))

    encoded_image.save("images/{}.png".format(encoded_name))


if __name__ == "__main__":
    encode_image("images/Me-in-august.png",
                 "!!!!I am a Hacker keep it a secret or you will be in trouble!!!!", "my_secret")

    decode_image("images/my_secret.png", "my_decoded_secret")


# Inspiration from
# https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
# https://github.com/tempor1s/steganograpgy/blob/master/steganograpgy.py
