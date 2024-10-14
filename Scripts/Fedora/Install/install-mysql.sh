#!/bin/bash

# Title: MySQL Installation Script
# Purpose: Install MySQL on Fedora, start the service, and enable it at boot.

# Constants
LOG_DIR="../Logs"
LOG_FILE="$LOG_DIR/mysql_installation_$(date '+%Y-%m-%d').log"
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

log_message "---- Starting MySQL Installation ----"

# Update repositories
log_message "Updating package repositories..."
dnf update -y >> "$LOG_FILE" 2>&1

# Install MySQL
log_message "Installing MySQL..."
dnf install mysql mysql-server -y >> "$LOG_FILE" 2>&1

# Start and enable MySQL service
log_message "Starting MySQL service..."
systemctl start mysqld >> "$LOG_FILE" 2>&1
log_message "Enabling MySQL service at boot..."
systemctl enable mysqld >> "$LOG_FILE" 2>&1

# Secure MySQL installation (interactive step for user to configure root password)
log_message "Securing MySQL installation..."
mysql_secure_installation >> "$LOG_FILE" 2>&1

log_message "MySQL installation and configuration completed successfully."
log_message "---- MySQL Installation Completed ----"
