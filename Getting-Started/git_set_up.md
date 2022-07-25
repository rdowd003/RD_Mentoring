# Getting Set Up & Practicing With Git/GitHub

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

5. Now in the "Respositories" directory, & use the URL you just copied to clone your fork of this program's repository. 


## Updating the forked repository with upstream changes
7. Now, `cd` into the newly cloned repoository (directory). You will have to set the original repository as an "upstream" remote.
```bash
git remote add rd_upstream https://github.com/rdowd003/RD_Mentoring.git
git remote -v # Verify rd_upstream
```

8. You will also need to periodically "fetch" changes from the upstream, merge it into master branch ** You will want to do this often **
```bash
git fetch rd_upstream
git branch -va

git checkout master
git merge rd_upstream/master
```

## Working on your branch
9. Next you can begin working in the branch that was set up for you (your name, lowercase, no spaces)
```bash
git branch # should be on master/main (if not, git checkout master)
git fetch
git branch -a # see all local & remote branches
git pull # bring in all data
git checkout --track origin/<yourname> # set origin to this branch
```

## Adding to the branch
10. While on the new branch, use the `mkdir` command to create a new directory titled "Articles" in the root directory of the repository branch
```bash
mkdir Articles
```

11. Now, `cd` into the "Articles" directory you just created & use the `touch` command to create an empty file called `test_git_file.txt`.

12. Type `git status` to see the change you have made in red.

13. Add this file using the `git add` command.

14. Type `git status` again. What dolor do you see now?

15. Commit this file using the `git commit` command, and be sure to specify a message of `"Add test_git_file.txt"`.

16. Type `git status` *again*. What happened?

17. Push your change to your fork-branch of the repo on GitHub, using this command (if pushing for the first time)
```bash
git push -u origin <yourname> # if the branch already exists locally, just use `git push`
```

18. Type `git status` **again**. What's different this time?

19. Use your web browser to navigate to your forked version of the repository on Github, and check to make sure that the `test_git_file` appears.

## Removing a file
20. Back in your terminal on your local machine, delete `test_git_file.txt` from
the repository, "Articles" directory.
```bash
rm `test_git_file.txt`
```

21. Now, check your `git status` again.

22. Add the change.

23. Type `git status` again.

24. Commit the change. What should your commit message say? (Hint: professionals always start each commit message with a present-tense verb, i.e. `Remove` or `Delete`, not `Removing` or `Deleted`.)

25. One more `git status`.

26. In your web browser, refresh your view of the forked version of the repository on Github. You should see that the `test_git_file.txt` is no longer there. However, if you click on the number of commits, you'll see the history of your changes.

## Setting up the rest of the repository
27. Repeat step 8, adding a new file title "week1_article_summary.txt"
28. Repeat steps 9-15 to push this new file into the repository on the branch with your name. This file will stay there. 

## Preparing to submit a pull request *Always do this before submitting a pull request*
29. Fetch upstream master and merge with your repo's master branch
```bash
git fetch rd_upstream
git checkout master # Switch to master
git merge rd_upstream/master # Merge any changes from upstream into the master branch
```

30. If there *were* any changes, you'll need to "rebase" your branch, meaning incorporate these changes into your branch.
```bash
git checkout <yourname>
git rebase master
```

## Submit a Pull Request to the original
31. Go to Github & follow [this documentation](https://gist.github.com/Chaser324/ce0505fbed06b947d962) for submitting a pull request