#!/bin/bash

# Title: PHP Installation Script
# Purpose: Install PHP and common PHP modules on Fedora.

# Constants
LOG_DIR="../Logs"
LOG_FILE="$LOG_DIR/php_installation_$(date '+%Y-%m-%d').log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S') 

# Check if Logs directory exists, create if it doesn't
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Logging function
log_message() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
    log_message "ERROR: Please run as root."
    exit 1
fi

log_message "---- Starting PHP Installation ----"

# Update repositories
log_message "Updating package repositories..."
dnf update -y >> "$LOG_FILE" 2>&1

# Install PHP and common PHP modules
log_message "Installing PHP and common PHP modules..."
dnf install php php-mysqlnd php-pdo php-gd php-mbstring php-xml php-cli -y >> "$LOG_FILE" 2>&1

# Restart Apache to apply PHP configurations (assuming Apache is used)
log_message "Restarting Apache web server to apply PHP configurations..."
systemctl restart httpd >> "$LOG_FILE" 2>&1

log_message "PHP installation completed successfully."
log_message "---- PHP Installation Completed ----"
