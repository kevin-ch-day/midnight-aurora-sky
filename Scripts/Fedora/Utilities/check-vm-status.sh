#!/bin/bash

# Title: Advanced VM Status Check Script
# Purpose: Monitor CPU, memory, disk usage, and processes to assess the performance of the Fedora VM.

# Constants
THRESHOLD_CPU=80  # CPU usage threshold percentage
THRESHOLD_MEM=80  # Memory usage threshold percentage
THRESHOLD_DISK=85 # Disk usage threshold percentage

# Function to log messages with timestamp
log_message() {
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$TIMESTAMP] $1"
}

# Function to check CPU usage
check_cpu_usage() {
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    log_message "Current CPU usage: $CPU_USAGE%"

    if (( $(echo "$CPU_USAGE > $THRESHOLD_CPU" | bc -l) )); then
        log_message "WARNING: CPU usage exceeds threshold of $THRESHOLD_CPU%."
    fi
}

# Function to check memory usage
check_memory_usage() {
    MEM_TOTAL=$(free | grep Mem | awk '{print $2}')
    MEM_USED=$(free | grep Mem | awk '{print $3}')
    MEM_USAGE=$(echo "scale=2; $MEM_USED / $MEM_TOTAL * 100" | bc)
    
    log_message "Current memory usage: $MEM_USAGE% (Used: $MEM_USED / Total: $MEM_TOTAL)"

    if (( $(echo "$MEM_USAGE > $THRESHOLD_MEM" | bc -l) )); then
        log_message "WARNING: Memory usage exceeds threshold of $THRESHOLD_MEM%."
    fi
}

# Function to check disk usage
check_disk_usage() {
    DISK_USAGE=$(df -h / | grep '/' | awk '{print $5}' | sed 's/%//g')
    log_message "Current disk usage: $DISK_USAGE%"

    if (( DISK_USAGE > THRESHOLD_DISK )); then
        log_message "WARNING: Disk usage exceeds threshold of $THRESHOLD_DISK%."
        log_message "Consider cleaning up unused files or expanding disk space."
    fi
}

# Function to check running processes
check_running_processes() {
    PROCESS_COUNT=$(ps aux --no-heading | wc -l)
    log_message "Current number of running processes: $PROCESS_COUNT"
    
    if (( PROCESS_COUNT > 150 )); then
        log_message "WARNING: High number of running processes detected. Consider reviewing running applications."
    fi
}

# Function to provide overall system feedback
provide_feedback() {
    log_message "---- Performance Summary ----"
    log_message "If CPU or memory usage is high, consider closing unused applications or services."
    log_message "If disk usage is high, check for large files or temporary files that can be deleted."
    log_message "Regular maintenance, such as cleaning up package caches and logs, is recommended."
}

# Main execution
log_message "---- Starting Advanced VM Status Check ----"
check_cpu_usage
check_memory_usage
check_disk_usage
check_running_processes
provide_feedback
log_message "---- VM Status Check Completed ----"
