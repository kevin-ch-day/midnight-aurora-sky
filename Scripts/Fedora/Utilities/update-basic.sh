#!/bin/bash

# Title: Update Fedora VM Script
# Purpose: Update and upgrade the Fedora VM with a single command.

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "ERROR: Please run as root."
    exit 1
fi

echo "Updating package repositories..."
dnf check-update

echo "Upgrading installed packages..."
dnf upgrade -y

echo "Cleaning up unused packages..."
dnf autoremove -y
dnf clean all

echo "Update and upgrade completed successfully."
