#!/bin/bash

# Title: Apache Web Server Installation Script
# Purpose: Install Apache Web Server on Fedora and configure it to start automatically.

# Constants
LOG_DIR="../Logs"
LOG_FILE="$LOG_DIR/apache_installation_$(date '+%Y-%m-%d').log"
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

log_message "---- Starting Apache Web Server Installation ----"

# Update repositories
log_message "Updating package repositories..."
dnf update -y >> "$LOG_FILE" 2>&1

# Install Apache
log_message "Installing Apache Web Server (httpd)..."
dnf install httpd -y >> "$LOG_FILE" 2>&1

# Start Apache service
log_message "Starting Apache service..."
systemctl start httpd >> "$LOG_FILE" 2>&1

# Enable Apache to start at boot
log_message "Enabling Apache service to start at boot..."
systemctl enable httpd >> "$LOG_FILE" 2>&1

# Check Apache service status
log_message "Checking Apache service status..."
systemctl status httpd >> "$LOG_FILE" 2>&1

# Adjust firewall to allow HTTP and HTTPS traffic (Optional)
log_message "Configuring firewall to allow HTTP and HTTPS traffic..."
firewall-cmd --permanent --add-service=http >> "$LOG_FILE" 2>&1
firewall-cmd --permanent --add-service=https >> "$LOG_FILE" 2>&1
firewall-cmd --reload >> "$LOG_FILE" 2>&1

log_message "---- Apache Web Server Installation Completed Successfully ----"
