# Klipb

Klipb is a clipboard manager designed for Wayland environments, utilizing the `wl-clipboard` and `rofi` utilities. It allows you to store, list, decode, delete, and manage clipboard items efficiently.

## Features

- **Store**: Save clipboard contents with deduplication.
- **List**: View stored clipboard items with a preview.
- **Decode**: Retrieve clipboard items by ID.
- **Delete**: Remove clipboard items by ID or query.
- **Wipe**: Clear all stored clipboard items.
- **Version**: Check the current version of the application.

## Requirements

To use Klipb, ensure you have the following:

- **Wayland**: A display server protocol.
- **rofi**: A window switcher and application launcher.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/klipb.git
   cd klipb
   ```

2. Build the application:
   ```bash
   go build -o klipb
   ```

3. Ensure you have `wl-clipboard` installed:
   ```bash
   sudo apt install wl-clipboard
   ```

4. Optionally, install `rofi` if it's not already installed:
   ```bash
   sudo apt install rofi
   ```

## Usage

Klipb provides several commands:

- **Store an item**:
  ```bash
  wl-paste | ./klipb store
  ```

- **List items**:
  ```bash
  ./klipb list
  ```

- **Decode an item**:
  ```bash
  ./klipb decode "1"  # Replace "1" with the ID of the item
  ```

- **Delete an item by ID**:
  ```bash
  echo "1" | ./klipb delete  # Replace "1" with the ID of the item
  ```

- **Delete items by query**:
  ```bash
  ./klipb delete-query "search_term"
  ```

- **Wipe all items**:
  ```bash
  ./klipb wipe
  ```

- **Check version**:
  ```bash
  ./klipb version
  ```

## Configuration

You can configure Klipb via environment variables or by specifying a configuration file. See the usage message for options:

```bash
./klipb -h
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open issues or submit pull requests to improve Klipb.

---

For any issues or feature requests, feel free to create an issue in the repository. Happy clipping!
