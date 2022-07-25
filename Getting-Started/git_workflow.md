# Practicing with Git and GitHub

This guide will walk you through forking the repository for this
program, cloning your forked copy to your local machine, and some of the
Git commands discussed in lecture. Similar to the Unix assignment, this
assignment will be fairly brief, as familiarity with Git and Github will
come over time as you interact with them more and more.

## Forking & Cloning the repository
1. Open up your browser and navigate to this program's repository on GitHub:
[https://github.com/rdowd003/RD_Mentoring](https://github.com/rdowd003/RD_Mentoring)`

2. Fork this repository, making sure to fork it to your Github
account (usually it forks to your Github account by default, so if you're not
prompted, then you should be fine). The button to `Fork` should be up in the
top right of the page.

3. Now navigate to your own Github repository, and grab the URL for your
fork so that you can clone it to your local machine. You should be able
to find the URL in the top middle of the page.

4. Create a directory called `Repositories` in your home directory and change into it. Note that `~/` is a shortcut to your home directory!
```bash
mkdir ~/Repositories
cd ~/Repositories
```

5. Use the URL you just copied to clone your fork of this program's repository. (Make sure that the URL contains *your* username, not `gschool`!)

## Creating a branch
6. Now, `cd` into the repo that you just clonedy, create a new branch
```bash
git checkout -b new_branch
```

## Adding a file
7. Now, while on the new branch, use the `touch` command to create an empty file called `test_git_file.txt`. This will require some of the Unix commands that we have previously discussed.

8. Type `git status` to see the change you have made in red.

9. Add this file using the `git add` command.

10. Type `git status` again. What dolor do you see now?

11. Commit this file using the `git commit` command, and be sure to specify a message of `"Add test_git_file.txt"`.

12. Type `git status` *again*. What happened?

13. Push your change to your fork-branch of the repo on GitHub.
```bash
git push -u origin new_branch
```

14. Type `git status` **again**. What's different this time?

15. Use your web browser to navigate to your forked version of the repository on Github, and check to make sure that the `test_git_file` appears.

## Removing a file
16. Back in your terminal on your local, delete `test_git_file.txt` from
the repository.
```bash
rm `test_git_file.txt`
```

17. Now, check your `git status` again.

18. Add the change.

19. Type `git status` again.

20. Commit the change. What should your commit message say? (Hint: professionals always start each commit message with a present-tense verb, i.e. `Remove` or `Delete`, not `Removing` or `Deleted`.)

21. One more `git status`.

22. In your web browser, refresh your view of the forked version of the repository on Github. You should see that the `test_git_file.txt` is no longer there. However, if you click on the number of commits, you'll see the history of your changes.


## Submitting a Pull Request
23. Go to Github ...