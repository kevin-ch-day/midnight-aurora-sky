#!/bin/bash

# Title: Fedora VM Setup Script
# Purpose: Automate the installation of essential tools (Python, MySQL, Git, and development libraries) for a data science environment.

# Constants
LOG_DIR="../Logs"
LOG_FILE="$LOG_DIR/setup_vm_$(date '+%Y-%m-%d').log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S') 

# Check if Logs directory exists, create if it doesn't
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Function to log messages to both the console and a log file
log_message() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

# Function to check if script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "[$TIMESTAMP] ERROR: Please run as root" | tee -a "$LOG_FILE"
    exit 1
fi

# Update the system and install necessary tools
log_message "---- Starting Fedora VM Setup ----"

log_message "Updating system packages..."
dnf update -y >> "$LOG_FILE" 2>&1

log_message "Installing Python 3 and pip..."
dnf install python3 python3-pip -y >> "$LOG_FILE" 2>&1

log_message "Installing Git..."
dnf install git -y >> "$LOG_FILE" 2>&1

log_message "Installing additional Python libraries (Pandas, NumPy, scikit-learn)..."
pip3 install pandas numpy scikit-learn >> "$LOG_FILE" 2>&1

log_message "Installing Vim and other utilities..."
dnf install vim nano htop wget curl -y >> "$LOG_FILE" 2>&1

# Check for installation success
log_message "Verifying installation of key packages..."
if command -v python3 &>/dev/null && command -v pip3 &>/dev/null && command -v git &>/dev/null && command -v mysql &>/dev/null; then
    log_message "SUCCESS: Python and Git are installed and configured."
else
    log_message "ERROR: One or more key tools failed to install. Check the log file for details."
    exit 1
fi

# Optional: Configure MySQL root password and secure the installation
log_message "Configuring MySQL root user and securing installation..."
mysql_secure_installation >> "$LOG_FILE" 2>&1

log_message "---- Fedora VM Setup Completed Successfully ----"

# End of script
