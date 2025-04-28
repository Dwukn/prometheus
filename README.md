# Kondo
![Kondo Badge](https://img.shields.io/badge/Clean%20Up%20Your%20Files-Spark%20Joy-ffc0cb?style=for-the-badge&logo=spring&logoColor=white)


> **Inspired by Marie Kondo**, the queen of decluttering, **Kondo** is a simple yet powerful CLI tool to tidy up your directories by organizing files into folders based on their extensions.

---

## ✨ Features

- Organizes files by their extension (e.g., `.jpg`, `.pdf`, `.txt`).
- Supports a `--dry-run` mode to preview changes without modifying any files.
- Simple and fast — perfect for quick directory cleanups.
- Easy to use with minimal setup.

---

## 📦 Installation

You will need [Rust](https://www.rust-lang.org/tools/install) installed. Then:

```bash
git clone https://github.com/Dwukn/kondo.git
cd kondo
cargo build --release
```

The compiled binary will be located in `target/release/kondo`.

---

## 🚀 Usage

```bash
kondo [OPTIONS]
```

### Options

| Option           | Description                                                 |
|------------------|-------------------------------------------------------------|
| `-d, --directory` | Specify the directory to organize (default is current `.`) |
| `--dry-run`       | Show what would happen without actually moving files       |

### Examples

Organize the current directory:

```bash
kondo
```

Organize a specific directory:

```bash
kondo --directory /path/to/your/folder
```

Preview what will happen (no files are moved):

```bash
kondo --directory /path/to/your/folder --dry-run
```

---

## 🛠 How It Works

- **Scan**: The program scans all files in the specified directory (non-recursively).
- **Group**: Files are grouped based on their extensions.
- **Move**: Files are moved into new folders named after their extensions.
  - Files without an extension are moved into a folder called `no_extension`.

Example:

```
Before:
  - photo.jpg
  - document.pdf
  - notes.txt
  - README

After running `kondo`:
  /jpg/photo.jpg
  /pdf/document.pdf
  /txt/notes.txt
  /no_extension/README
```

---

## 📚 About the Name

**Kondo** is named after **Marie Kondo**, the organizational expert famous for the *KonMari* method. This tool aims to "spark joy" by cleaning up your filesystem effortlessly.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/your-username/kondo/issues) if you want to contribute.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Future Improvements

- Recursive directory organization
- Configurable rules (e.g., based on file size, creation date)
- Better error handling
- Option to undo the last organization
