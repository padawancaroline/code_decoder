# CipherFun

CipherFun is a simple Python application built with Streamlit for encrypting and decrypting messages using Caesar's Cipher and Vigenère's Cipher.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

CipherFun provides a user-friendly interface for encoding and decoding messages using classic cipher algorithms. It offers two main ciphers: Caesar's Cipher, which shifts characters by a fixed offset, and Vigenère's Cipher, which uses a keyword to determine variable offsets for each character.

## Features

- **Easy-to-Use Interface**: CipherFun comes with a simple web interface built using Streamlit, allowing users to interactively input messages and select encryption or decryption options.
- **Support for Multiple Ciphers**: Users can choose between Caesar's Cipher and Vigenère's Cipher based on their preferences and requirements.
- **Real-Time Feedback**: The application provides real-time feedback, displaying the encrypted or decrypted message immediately after user submit input.

## Setup

To set up CipherFun locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application by executing `streamlit run streamlit_app.py` in your terminal.

## Usage

Once the application is running, access it through your web browser. You'll be presented with a user interface where you can:

1. Select the cipher type (Caesar's Cipher or Vigenère's Cipher).
2. Choose whether to encrypt or decrypt a message.
3. Input the message and any additional parameters (such as the offset or keyword).
4. Click the "Submit" button to see the result.

## Contributing

Contributions to CipherFun are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.
