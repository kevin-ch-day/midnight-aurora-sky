#!/bin/bash

# Title: Git Configuration Script
# Purpose: Configure Git with username and email on Fedora.

# Constants
LOG_DIR="../Logs"
LOG_FILE="$LOG_DIR/git_configuration_$(date '+%Y-%m-%d').log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Check if Logs directory exists, create if it doesn't
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Logging function
log_message() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

# Ensure the script is run as root (or user with Git installed)
if [ "$EUID" -ne 0 ]; then
    log_message "WARNING: It is recommended to run this script as a user with Git installed."
fi

# Prompt for Git configuration
read -p "Enter your Git username: " GIT_USERNAME
read -p "Enter your Git email: " GIT_EMAIL

# Configure Git with the provided username and email
log_message "Configuring Git with username: $GIT_USERNAME and email: $GIT_EMAIL"
git config --global user.name "$GIT_USERNAME" >> "$LOG_FILE" 2>&1
git config --global user.email "$GIT_EMAIL" >> "$LOG_FILE" 2>&1

# Verify Git configuration
log_message "Verifying Git configuration..."
git config --global --list >> "$LOG_FILE" 2>&1

log_message "Git has been configured successfully."
