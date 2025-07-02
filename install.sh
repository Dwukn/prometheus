#!/bin/bash

set -e

REPO="Dwukn/kondo"
BINARY_NAME="kondo"
INSTALL_DIR="/usr/local/bin"

# Detect OS
OS="$(uname -s)"
ARCH="$(uname -m)"

# Map OS and ARCH to release asset naming
case "$OS" in
    Linux) PLATFORM="linux" ;;
    Darwin) PLATFORM="macos" ;;
    MINGW*|MSYS*|CYGWIN*) PLATFORM="windows" ;;
    *) echo "Unsupported OS: $OS"; exit 1 ;;
esac

# Adjust binary name for Windows
if [[ "$PLATFORM" == "windows" ]]; then
    BINARY_NAME="${BINARY_NAME}.exe"
fi

# Download latest release info from GitHub API
echo "Fetching latest release..."
LATEST_URL=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" \
    | grep "browser_download_url" \
    | grep "$PLATFORM" \
    | cut -d '"' -f 4)

if [ -z "$LATEST_URL" ]; then
    echo "Could not find a release for platform: $PLATFORM"
    exit 1
fi

echo "Downloading $BINARY_NAME for $PLATFORM..."
curl -L "$LATEST_URL" -o "$BINARY_NAME"
chmod +x "$BINARY_NAME"

echo "Installing to $INSTALL_DIR..."
sudo mv "$BINARY_NAME" "$INSTALL_DIR/kondo"

echo "✅ Kondo installed successfully!"
echo "Run it using: kondo --help"
