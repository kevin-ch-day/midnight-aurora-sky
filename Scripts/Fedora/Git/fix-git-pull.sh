#!/bin/bash

# Title: Fix Git Pull Configuration Script
# Purpose: Configure Git to resolve divergent branches for future pulls.

# Function to check if Git is installed
check_git_installed() {
    if ! command -v git &> /dev/null; then
        echo "Git is not installed. Please install Git before running this script."
        exit 1
    fi
}

# Function to configure Git pull behavior
configure_git_pull() {
    echo "Choose your preferred Git pull behavior:"
    echo "1) Merge (default)"
    echo "2) Rebase"
    echo "3) Fast-forward only"

    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            git config --global pull.rebase false
            echo "Git pull behavior set to merge."
            ;;
        2)
            git config --global pull.rebase true
            echo "Git pull behavior set to rebase."
            ;;
        3)
            git config --global pull.ff only
            echo "Git pull behavior set to fast-forward only."
            ;;
        *)
            echo "Invalid choice. Please run the script again and select 1, 2, or 3."
            exit 1
            ;;
    esac
}

# Main execution
check_git_installed
configure_git_pull

echo "Configuration completed. You can now run 'git pull' without issues."
