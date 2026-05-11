#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Safiatou Traore

"""
This script is to take an input and encode and decode BASE64
"""

# Imported libaries
import base64

"""
encoding planintext to base64
We will do the following steps
1.) Convert the string using UTF-8
2.) Pass the bytes into a function called b64.encode
4.) Resulted bytes and return
"""

 def encode_to_base64(plaintext: str) -> str: 
 text_as_bytes = plaintext.encode("utf-8") # "Hello" -1> b"Hello" == 0x48 0x65 0x6c
encoded_bytes = base64.b64encode(text_as_bytes) # b'Hello" -> b"SGVsbG8="
return encoded_bytes.decode("utf-8") # b"SGVsbG8=" -> "SGVsbG"