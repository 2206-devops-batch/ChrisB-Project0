# We will use wave package available in native Python installation to read and write .wav audio file
import wave


def encode_sound(file_location, text, encoded_name):
    # read wave audio file
    song = wave.open(file_location, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # The "secret" text message
    # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    text = text + int((len(frame_bytes)-(len(text)*8*8))/8) * '#'
    # Convert text to bit array
    bits = list(
        map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in text])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open(f'../audio/{encoded_name}.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()


def decode_sound(file_location, decoded_name):
    # read wave audio file
    song = wave.open(file_location, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    string = "".join(chr(
        int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]

    # Print the extracted text
    decoded_output = f'Sucessfully decoded: {decoded} from file {file_location}'
    f = open(f'{decoded_name}.txt', "w")
    f.write(decoded_output)
    f.close()
    print(decoded_output)
    song.close()


if __name__ == "__main__":
    soundFiles = ["../audio/Silent.wav", "../audio/Fairground.wav"]
    sampleText = [
        "Peter Parker is the Spiderman!",
        "!!!!I am a Hacker keep it a secret or you will be in trouble!!!!"
    ]

    encode_sound(soundFiles[0], sampleText[0], "my_secret")
    decode_sound("../audio/my_secret.wav", "my_decoded_secret")

    encode_sound(soundFiles[1], sampleText[1], "my_secret_fair")
    decode_sound("../audio/my_secret_fair.wav", "my_decoded_secret_fair")
