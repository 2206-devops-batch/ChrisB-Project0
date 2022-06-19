import visual.steganography as visuals
import vocal.steganography as vocals
import sys


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


if __name__ == "__main__":
    vocal = ("-voc" or "--vocal") in sys.argv
    visual = ("-vis" or "--visual") in sys.argv
    both = vocal and visual

    soundFiles = ["audio/Silent.wav", "audio/Fairground.wav"]
    imageFiles = ["images/Me-in-august.png", "images/my_secret.png"]

    fontFiles = [
        "~/Library/Fonts/Arial Unicode.ttf",
        "fonts/georgia/Georgia.ttf",
        "fonts/roboto/Roboto-Regular.ttf"
    ]

    sampleText = [
        "Peter Parker is the Spiderman!",
        "!!I am a Hacker keep it a secret or you will be in trouble!!",
        """According to all know laws of aviation, there is no way a bee should be able to fly.
            Its wings are too small to get its fat little body off the ground.
            The bee, of course, flies anyway because bees don't care waht humans think is impossible."""
    ]

    # decrypt sample sound file
    # decrypt resulting image file

    # Modify / Reply

    # encrypt as new cover image
    # encrypt as new ste sound

    if both:
        print(f'{style.CYAN}Look How Far You\'ve Advanced As A Spy{style.RESET}')
        vocals.decode_sound("sound2image2text.wav", "decoded_sound2img")
        visuals.decode_image("decoded_sound2img", "decoded_img2txt")
        YOUR_NEW_SECRET = "SAY SOMETHING FANCY OR TOP SECRET HERE!!"
        YOUR_COVER_IMAGE = "images/covers/ ----------- .png"
        YOUR_COVER_AUDIO = "audio/covers/ ----------- .wav"
        visuals.encode_image(YOUR_COVER_IMAGE, fontFiles[0], YOUR_NEW_SECRET, "encoded_txt2img")
        vocals.encode_sound(YOUR_COVER_AUDIO, YOUR_NEW_SECRET, "encoded_txt2sound")

    elif visual:
        print(f'{style.GREEN}Welcome To Being A Visual Spy{style.RESET}')
        visuals.encode_image(
            imageFiles[0], fontFiles[0], sampleText[1], "my_secret")
        visuals.decode_image(imageFiles[1], "my_decoded_secret")

    elif vocal:
        print(f'{style.GREEN}Welcome To Being A Vocal Spy{style.RESET}')
        vocals.encode_sound(soundFiles[0], sampleText[0], "my_secret")
        vocals.decode_sound("audio/my_secret.wav", "my_decoded_secret")
        vocals.encode_sound(soundFiles[1], sampleText[1], "my_secret_fair")
        vocals.decode_sound("audio/my_secret_fair.wav", "my_decoded_secret_fair")
