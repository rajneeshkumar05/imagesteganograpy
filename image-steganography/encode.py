from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'

def encode_image(image_path, secret_text, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_text = text_to_binary(secret_text)
    data_index = 0

    for y in range(img.height):
        for x in range(img.width):
            if data_index < len(binary_text):
                r, g, b = pixels[x, y]

                r = (r & ~1) | int(binary_text[data_index])
                data_index += 1

                pixels[x, y] = (r, g, b)
            else:
                img.save(output_path)
                print("✅ Message hidden successfully!")
                return

    img.save(output_path)

encode_image("original.png", "HELLO STEGANOGRAPHY", "encoded.png")
