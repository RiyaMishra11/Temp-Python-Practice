"""108 - Simple Text File Encoder using Base64"""
import base64
from pathlib import Path

def encode_text(text):
    return base64.b64encode(text.encode("utf-8")).decode("ascii")

def decode_text(encoded):
    return base64.b64decode(encoded.encode("ascii")).decode("utf-8")

def encode_file(input_file, output_file):
    text = Path(input_file).read_text(encoding="utf-8")
    Path(output_file).write_text(encode_text(text), encoding="utf-8")

def decode_file(input_file, output_file):
    encoded = Path(input_file).read_text(encoding="utf-8")
    Path(output_file).write_text(decode_text(encoded), encoding="utf-8")

def main():
    original = "Hello from Python!"
    encoded = encode_text(original)
    decoded = decode_text(encoded)

    print("Original:", original)
    print("Encoded:", encoded)
    print("Decoded:", decoded)

if __name__ == "__main__":
    main()
