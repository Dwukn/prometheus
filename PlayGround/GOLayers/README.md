# Information Security Lab Programs in Go

This repository contains implementations of various programs from my Information Security lab, developed in the Go programming language. I am using Go to learn and understand key concepts of information security, cryptography, and networking. Each program is aimed at demonstrating a specific topic or technique relevant to information security.
<!--
## Table of Contents

- [Introduction](#introduction)
- [Programs](#programs)
  - [Encryption & Decryption](#encryption--decryption)
  - [Hashing Algorithms](#hashing-algorithms)
  - [Networking](#networking)
  - [Authentication](#authentication)
- [Learning Goals](#learning-goals)
- [Setup](#setup)
- [Contributing](#contributing)
- [License](#license)-->

## Introduction

Information security is a critical aspect of modern computing, and in this lab, I am working to implement foundational security concepts using Go. Go is a powerful and efficient language that is well-suited for building secure applications, and by implementing these security techniques, I hope to gain hands-on experience and enhance my skills in both Go and information security.

## Programs

Here are some of the key programs in this repository:

### Encryption & Decryption
- **Caesar Cipher**: Implemented a basic Caesar cipher encryption and decryption.
- **Vigenère Cipher**: Implemented a Vigenère cipher for encrypting and decrypting text using a key.
- **AES Encryption**: A program demonstrating the Advanced Encryption Standard (AES) for symmetric encryption.
  
### Hashing Algorithms
- **MD5 Hashing**: Implementation of the MD5 hash function to convert data into a fixed-length hash.
- **SHA-256 Hashing**: Implemented SHA-256 to demonstrate secure hash functions used for integrity checking.
  
### Networking
- **Socket Programming**: Basic TCP and UDP socket programming to understand secure communication between clients and servers.
  
### Authentication
- **Password Hashing**: Example of hashing user passwords using algorithms like bcrypt for secure user authentication.
  
Each program is implemented to demonstrate various cryptographic techniques, secure networking, and authentication mechanisms.

## Learning Goals

- Learn Go by implementing information security algorithms.
- Understand core concepts in cryptography, including encryption, decryption, and hashing.
- Explore network security by implementing socket-based communication.
- Practice secure password management and authentication techniques.
  
## Setup

To get started with this repository, you need to have Go installed on your local machine. You can download Go from [here](https://golang.org/dl/).

### Steps to run the programs:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/info-security-labs-in-go.git
    ```

2. Navigate to the project directory:
    ```bash
    cd info-security-labs-in-go
    ```

3. Install dependencies (if applicable):
    - For most of the programs in this repository, there are no external dependencies. However, if you are using any third-party libraries, you can run `go mod tidy` to download and install the required modules.

4. Run a program (example for Vigenère cipher):
    ```bash
    go run vigenere_cipher.go
    ```

## Contributing

Contributions are welcome! If you have any improvements, suggestions, or new programs you'd like to add, feel free to open an issue or submit a pull request.
