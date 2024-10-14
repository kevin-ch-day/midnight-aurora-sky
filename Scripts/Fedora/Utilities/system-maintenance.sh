#!/bin/bash

# Title: Fedora System Maintenance Script
# Purpose: Update, upgrade, and optimize Fedora VM with detailed logging and error handling.

# Constants
LOG_DIR="../Logs"
LOG_FILE="$LOG_DIR/fedora_system_maintenance_$(date '+%Y-%m-%d').log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Check if Logs directory exists, create if it doesn't
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Function to check if script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "[$TIMESTAMP] ERROR: Please run as root" | tee -a "$LOG_FILE"
    exit 1
fi

# Logging function to append to log file and output to console
log_message() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

# Function to check for network connectivity before proceeding
check_network() {
    echo "Checking network connectivity..."
    ping -c 3 google.com > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        log_message "ERROR: No network connectivity. Exiting script."
        exit 1
    else
        log_message "SUCCESS: Network connectivity confirmed."
    fi
}

# Function to check system disk space and memory usage
check_system_health() {
    log_message "Performing system health check (disk space and memory)..."

    # Check disk space
    DISK_USAGE=$(df -h / | grep '/' | awk '{print $5}')
    log_message "Disk usage: $DISK_USAGE"

    # Check memory usage
    MEM_USAGE=$(free -h | grep 'Mem' | awk '{print $3 "/" $2}')
    log_message "Memory usage: $MEM_USAGE"

    # Check if there is sufficient space (assuming threshold is 80% for disk usage)
    if [[ "$DISK_USAGE" > 80% ]]; then
        log_message "WARNING: Disk usage is over 80%, consider cleaning up space."
    fi

    log_message "System health check completed."
}

# Function to update package repository information
update_system() {
    log_message "Updating package repositories..."
    dnf check-update >> "$LOG_FILE" 2>&1
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: Package repositories updated successfully."
    else
        log_message "ERROR: Failed to update repositories."
        exit 1
    fi
}

# Function to upgrade installed packages
upgrade_system() {
    log_message "Upgrading installed packages..."
    dnf upgrade -y >> "$LOG_FILE" 2>&1
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: All packages upgraded successfully."
    else
        log_message "ERROR: Package upgrade failed."
        exit 1
    fi
}

# Function to clean up system and free space
clean_system() {
    log_message "Cleaning up system and removing unused packages..."
    dnf autoremove -y >> "$LOG_FILE" 2>&1
    dnf clean all >> "$LOG_FILE" 2>&1
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: System cleanup completed successfully."
    else
        log_message "ERROR: System cleanup failed."
        exit 1
    fi
}

# Function to manage log rotation (optional)
rotate_logs() {
    log_message "Checking if log rotation is needed..."
    MAX_LOG_SIZE=10485760  # 10 MB size limit for logs
    if [ -f "$LOG_FILE" ]; then
        LOG_SIZE=$(stat -c%s "$LOG_FILE")
        if (( LOG_SIZE > MAX_LOG_SIZE )); then
            mv "$LOG_FILE" "$LOG_FILE.old"
            log_message "Log rotated as the size exceeded the limit of 10MB."
        fi
    fi
}

# Run all functions in order with status updates
log_message "---- Starting Fedora System Maintenance ----"
check_network
check_system_health
update_system
upgrade_system
clean_system
rotate_logs
log_message "---- Fedora System Maintenance Completed ----"
