# Practicing with Git and GitHub

This assignment will walk you through forking the repository for this
program, cloning your forked copy to your local machine, and some of the
Git commands discussed in lecture. Similar to the Unix assignment, this
assignment will be fairly brief, as familiarity with Git and Github will
come over time as you interact with them more and more.

1. Open up your browser and navigate to this program's repository on GitHub:
[http://www.github.com/gschool/dsi-week-zero](http://www.github.com/gschool/dsi-week-zero)`

2. Fork this repository, making sure to fork it to your Github
account (usually it forks to your Github account by default, so if you're not
prompted, then you should be fine). The button to `Fork` should be up in the
top right of the page.

3. Now navigate to your own Github repository, and grab the URL for your
fork so that you can clone it to your local machine. You should be able
to find the URL in the top middle of the page.

4. Create a directory called `galvanize` in your home directory and change into it. Note that `~/` is a shortcut to your home directory!
```bash

mkdir ~/galvanize
cd ~/galvanize
```

5. Use the URL you just copied to clone your fork of this program's repository. (Make sure that the URL contains *your* username, not `gschool`!)

6. Now, `cd` into the repo that you just cloned, and use the `touch` command to create an empty file called `test_git_file`. This will require some of the Unix commands that we have previously discussed.

7. Type `git status` to see the change you have made in red.

8. Add this file using the `git add` command.

9. Type `git status` again. What dolor do you see now?

10. Commit this file using the `git commit` command, and be sure to specify a message of `"Add test_git_file."`.

11. Type `git status` *again*. What happened?

12. Push your change to your fork of the repo on GitHub.

13. Type `git status` **again**. What's different this time?

14. Use your web browser to navigate to your forked version of the repository on Github, and check to make sure that the `test_git_file` appears.

15. Back in your terminal on your local, delete `test_git_file.txt` from
the repository.

16. Now, check your `git status` again.

17. Add the change.

18. Type `git status` again.

19. Commit the change. What should your commit message say? (Hint: professionals always start each commit message with a present-tense verb, i.e. `Remove` or `Delete`, not `Removing` or `Deleted`.)

20. One more `git status`.

21. In your web browser, refresh your view of the forked version of the repository on Github. You should see that the `test_git_file.txt` is no longer there. However, if you click on the number of commits, you'll see the history of your changes.

# GitHub Assignment

1. Populate your GitHub profile. Add your name, a photo, your info, etc.

2. [Add an SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/). Using SSH will allow you to push and pull without entering your password each time!

3. Create a GitHub repository for your "dream" project.

4. Clone your new GitHub repo into the `~/galvanize` directory on your computer. (Choose "Use SSH" before you copy the URL!)

5. Write a short README.md file for your dream project. Each README.md file should be written in Markdown so that it renders beautifully on GitHub.com. If you are new to writing Markdown, do this [Markdown Tutorial](http://www.markdowntutorial.com/).

6. Add and commit your new README.md file.

7. Push your changes back to GitHub!
