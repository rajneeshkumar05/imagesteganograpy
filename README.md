# 🖼️ Image Steganography using Python (LSB Method)

This project demonstrates **Image Steganography** using Python, where a **secret text message** is hidden inside an image using the **Least Significant Bit (LSB)** technique.

The encoded image looks visually identical to the original image, but it secretly contains hidden information.

---

## 🔐 What is Image Steganography?

Image steganography is the process of hiding secret data inside an image such that **no one can detect the presence of the hidden message** by looking at the image.

Unlike encryption, steganography hides the **existence** of the message, not just its meaning.

---

## 🧠 Technique Used

- **LSB (Least Significant Bit) Steganography**
- Secret data is stored in the last bit of pixel values
- Changes are invisible to the human eye

---

## 🛠️ Technologies Used

- **Python**
- **Pillow (PIL)** – Image processing library
- Binary encoding & decoding
- Pixel manipulation

---

## 📁 Project Structure

image-steganography/
│── encode.py # Hide message in image
│── decode.py # Extract hidden message
│── input.png # Original image
│── encoded.png # Image with hidden message
│── README.md
