from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_data = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)

    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == '11111111':
            break
        chars.append(chr(int(byte, 2)))

    print("🔓 Hidden Message:", ''.join(chars))

decode_image("encoded.png")
