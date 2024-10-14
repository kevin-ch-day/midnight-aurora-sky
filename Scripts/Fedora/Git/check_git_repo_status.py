import subprocess

# Title: Git Repository Status Checker
# Author: [Your Name]
# Purpose: To check the status of the current Git repository, including the current branch,
#          any uncommitted changes, whether the branch can be merged with the main branch,
#          provide feedback for improvement, and merge all branches into the current branch.

def run_command(command):
    """Run a shell command and return its output and exit code."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout.strip(), result.returncode

def list_branches():
    """List all branches in the Git repository."""
    print("\n--- Available Branches ---")
    branches, _ = run_command("git branch --all")
    print(branches)
    print("---------------------------")

def check_git_status():
    """Check the current status of the Git repository and provide feedback."""
    # Check if we are inside a Git repository
    stdout, returncode = run_command("git rev-parse --is-inside-work-tree")
    if returncode != 0:
        print("ERROR: Not inside a Git repository.")
        return

    # Get the current branch name
    branch_name, _ = run_command("git branch --show-current")
    print(f"Current branch: {branch_name}")

    # Check for uncommitted changes
    status, _ = run_command("git status --porcelain")
    if status:
        print("You have uncommitted changes:")
        print(status)
    else:
        print("No uncommitted changes.")

    # Fetch the latest changes from the remote repository
    print("Fetching the latest changes from the remote...")
    run_command("git fetch")

    # Check for commits ahead/behind main
    commits_ahead, commits_behind = check_branch_status(branch_name)

    if commits_ahead > 0:
        print(f"You have {commits_ahead} commits ahead of the main branch.")
    if commits_behind > 0:
        print(f"You are {commits_behind} commits behind the main branch.")

    # Check if the branch can be merged with main
    check_merge_status(branch_name)

    # Provide feedback for improvement
    provide_feedback(commits_ahead, commits_behind)

def check_branch_status(branch_name):
    """Check how many commits the current branch is ahead or behind the main branch."""
    # Get the number of commits ahead and behind
    stdout_ahead, _ = run_command(f"git rev-list --count {branch_name}..origin/main")
    stdout_behind, _ = run_command(f"git rev-list --count origin/main..{branch_name}")

    commits_behind = int(stdout_ahead)
    commits_ahead = int(stdout_behind)

    return commits_ahead, commits_behind

def check_merge_status(branch_name):
    """Check if the current branch can be merged with the main branch."""
    # Get merge base
    merge_base, _ = run_command(f"git merge-base {branch_name} origin/main")
    if not merge_base:
        print("ERROR: Unable to determine merge base. You may need to pull the latest changes.")
        return

    # Check if the branch can be merged
    merge_status, _ = run_command(f"git merge --no-commit --no-ff origin/main")
    if "CONFLICT" in merge_status:
        print("The branch cannot be merged due to conflicts.")
    else:
        print("The branch can be merged with the main branch.")

def provide_feedback(commits_ahead, commits_behind):
    """Provide feedback based on branch status."""
    print("\n--- Feedback for Improvement ---")
    if commits_ahead > 0 and commits_behind > 0:
        print("You are both ahead and behind the main branch. Consider synchronizing your changes with the remote.")
    elif commits_ahead > 0:
        print("Your branch has new commits that are not yet merged into the main branch. Consider pushing your changes.")
    elif commits_behind > 0:
        print("Your branch is behind the main branch. Consider pulling the latest changes to stay updated.")
    else:
        print("Your branch is in sync with the main branch. Good job!")

def merge_all_branches():
    """Merge all branches into the current branch."""
    current_branch, _ = run_command("git branch --show-current")
    print(f"\nMerging all branches into '{current_branch}'...")

    branches, _ = run_command("git branch --format='%(refname:short)'")
    branch_list = branches.splitlines()

    for branch in branch_list:
        if branch.strip() != current_branch:
            print(f"Merging branch: {branch}")
            # Checkout to the current branch before merging
            run_command(f"git checkout {current_branch}")
            # Merge the branch
            merge_result, merge_returncode = run_command(f"git merge {branch}")

            if merge_returncode != 0:
                print(f"ERROR: Could not merge branch '{branch}'. Resolve conflicts manually.")
                continue
            print(f"Successfully merged branch: {branch}")

def display_menu():
    """Display the main menu options to the user."""
    while True:
        print("\n--- Git Repository Status Checker Menu ---")
        print("1. Check Git Status")
        print("2. Check Merge Status")
        print("3. List Available Branches")
        print("4. Merge All Branches")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            check_git_status()
        elif choice == '2':
            list_branches()
            branch_name = input("Enter the branch name to check merge status: ")
            check_merge_status(branch_name)
        elif choice == '3':
            list_branches()
        elif choice == '4':
            merge_all_branches()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    display_menu()
