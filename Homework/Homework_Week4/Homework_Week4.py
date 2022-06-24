# Question 1
# Complete definitions for key Git & GitHub terminology
# GIT WORKFLOW FUNDAMENTALS
# ·        Working Directory
# It is the folder that contains the project's source files which Git will keep track of the changes.
# Git is a version control system that you can use locally in your computer or integrated with GitHub, in the web,
# for instance. Git holds the record of all files and changes. In short, it is a historical backup, and you can go
# back to restore a specific version.
# ·        Staging Area
# It is the area where Git keeps the changes of a project in your working directory you want to include in the next
# commit.
# ·        Local Repo (head)
# It is a local copy of the head in a remote repository that points to the master branch. It is updated every time you
# commit.
# ·        Remote repo (master)
# It is a repository hosted on the internet or in a network that can be cloned and used on a local computer. It is also
# a shared central repository where a team can collaborate by using branches between repositories. A popular one is
# Github.
#
#
# WORKING DIRECTORY STATES:
# ·        Staged
# A file that contains the changes to be included in the next commit.
# ·        Modified
# It's how Git label the file that has been modified but is not in the staging area to be committed.
# ·        Committed
#
#
# GIT COMMANDS:
# ·        Git add
# The command adds a change in the working directory to the staging area.
# ·        Git commit
# The command will save all staged changes, along with a short description and committs to the local repository.
# ·        Git push
# The command lets you send the commits from your local branch to a remote repository.
# ·        Git fetch
# It is the command utilised to download the content from a remote repository that change the local files.
# ·        Git merge
# The command is used for merging changes from another branch and combines all integrated changes into one history.
# ·        Git pull
# It is the command used to download and integrate changes from a remote repository to the local one.


# TASK 2 (Exception Handling)

def validate_pin(input_pin):
    valid_pin = 12345
    return input_pin == valid_pin


def pin():
    for i in range(3):
        user_pin = int(input("Type your pin: "))
        if validate_pin(user_pin):
            return
        else:
            if i < 2:
                print(f"Invalid pin, you can try {2 - i} more time(s)")
    raise BaseException("Account blocked")


def user_withdrawal(amount):
    balance = 100
    if amount > balance:
        print("The amount requested is not available.")
    else:
        balance_after_withdrawal = (balance - amount)
        print("Your balance after withdrawal: ", balance_after_withdrawal)


def main():
    pin()
    amount = int(input("How much would you like to withdrawal? "))
    user_withdrawal(amount)


# TASK 3 (Testing)

import unittest


class TestHomeworkWeek4(unittest.TestCase):
    def test_validate_pin_invalid(self):
        assert not validate_pin(1234)

    def test_validate_pin_valid(self):
        assert validate_pin(12345)

    def test_user_withdrawal_no_funds(self):
        amount = 110
        user_withdrawal(amount)

