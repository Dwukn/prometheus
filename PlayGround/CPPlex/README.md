# Cpp_learn

Welcome to the `Cpp_learn` repository! This project contains C++ implementations of popular cryptographic algorithms, including MD5 and SHA-1, as part of a learning process for understanding hashing and security concepts.

<!--
## Table of Contents

- [Overview](#overview)
- [Algorithms Implemented](#algorithms-implemented)
  - [MD5](#md5)
  - [SHA-1](#sha-1)
- [Installation](#installation)
- [Contributing](#contributing) -->

## Overview

This repository is dedicated to learning and understanding cryptographic algorithms in C++. It includes simple implementations of the MD5 and SHA-1 hashing algorithms. These algorithms are widely used for generating hash values of data, often for data integrity checks, password storage, and more.

The purpose of this project is to demonstrate the underlying mechanisms of these hash functions and their implementation in C++.

## Algorithms Implemented

### MD5

MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit hash value, typically rendered as a 32-character hexadecimal number. MD5 was designed by Ronald Rivest in 1991 and is commonly used in various security applications and data integrity checks.

### SHA-1

SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function that produces a 160-bit hash value, typically rendered as a 40-character hexadecimal number. It was designed by the NSA and published by NIST in 1993. However, due to vulnerabilities discovered over time, SHA-1 is considered weak and should not be used in security-critical applications.

## Installation

To get started with this project, you need to have a C++ development environment set up. You can use any IDE or text editor for writing C++ code, and the following tools for compiling and running the code:

- **g++**: C++ compiler (or any other C++ compiler)
- **Make** (optional): To automate the build process

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Cpp_learn.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Cpp_learn
   ```

3. **Compile the code**:
   To compile the C++ code for hashing algorithms, you can use the following command:
   ```bash
   g++ -o hash_algorithms md5.cpp sha1.cpp
   ```

4. **Run the program**:
   After compilation, you can run the program to see the hash outputs:
   ```bash
   ./hash_algorithms
   ```


## Contributing

Contributions are welcome! If you'd like to improve the project or add new features (e.g., other hashing algorithms like SHA-256), feel free to open an issue or submit a pull request.

### How to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a pull request.
