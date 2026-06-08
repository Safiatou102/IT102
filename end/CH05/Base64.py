#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Safiatou Traore

"""
This script is to take an input and encode and decode BASE64
"""

# Imported libraries
import base64

def encode_to_base64(plaintext: str) -> str:
    """
    Encoding plaintext to base64.
    Steps:
    1.) Convert the string using UTF-8
    2.) Pass the bytes into a function called b64encode
    3.) Decode the resulting bytes back to string
    """
    text_as_bytes = plaintext.encode("utf-8")           # "Hello" -> b"Hello"
    encoded_bytes = base64.b64encode(text_as_bytes)     # b"Hello" -> b"SGVsbG8="
    return encoded_bytes.decode("utf-8")                # b"SGVsbG8=" -> "SGVsbG8="


def decode_from_base64(encoded_text: str) -> str:
    """
    Decoding a base64 string back to original plaintext
    Steps:
    1.) Convert base64 string to bytes
    2.) Decode those bytes back to UTF-8 string
    """
    encoded_as_bytes = encoded_text.encode("utf-8")     # "SGVsbG8=" -> b"SGVsbG8="
    decoded_bytes = base64.b64decode(encoded_as_bytes)  # b"SGVsbG8=" -> b"Hello"
    return decoded_bytes.decode("utf-8")               # b"Hello" -> "Hello"


def main():
    message = input("Enter text to encode: ").strip()
    if not message:
        print("No message entered. Exiting.")
        return

    # Encode
    encoded = encode_to_base64(message)
    print(f"Encoded message: {encoded}")

    # Ask if the user wants to decode
    answer = input("Do you want to decode it back? (yes/no): ").strip().lower()
    if answer in ("yes", "y"):
        decoded = decode_from_base64(encoded)
        print(f"Decoded message: {decoded}")
    else:
        print("Decoding skipped.")


if __name__ == "__main__":
    main()