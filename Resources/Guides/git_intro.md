# Table of Contents - Interacting With Git

## 1. Introduction
- Background
- Cloning & Forking
- Using a repo locally
- Interacting with remotes

## 2. Typical Workflow
- Personal repository
- Shared Repositories

## 3. Resources

# 1. Intro to Git and GitHub

## A. Background 

GitHub is one of the most popular tools for people to develop software collaboratively via the Internet. At the heart of GitHub is Git, a distributed version control system for software development. It allows us to keep track of and manage all of the different versions of our files for a project. It does this by keeping a history of all of the changes that we make to our files. When used correctly, Git also works as a backup of our files: it allows us to keep a backup copy of our work on GitHub, and it allows us to roll back any of our files to any previous version that we have *committed* to the repo.

While Git is a distributed version control system, GitHub is a hosting service for Git *repos* (repositories for software projects). In other words, GitHub is a hosting service for projects that use Git. GitHub allows us to share our projects with other people, and to allow other people to collaborate with us on our projects either privately or publicly. We interact with Git locally on our computers through our `bash` terminal, whereas we interact with GitHub through a web browser.

### Diving In

Before we can work and interact with a Git repository (either locally or 
through GitHub), we first have to obtain a Git repository! First, we'll make a local copy of a Git repo by cloning it from GitHub. Then we'll use `git` commands to interact with the repo. 

#### What's a repo, anyway?

A Git repository is a **local** collection of files and contains a hidden `.git` 
subdirectory in its root. Git keeps track of the state of the files in the 
repository's directory on disk (so long as those files have been added to the index - we'll get to that below). There are two different ways to create a new repository: 

* Initializing an empty, new local repository (*not* recommended)
* *Cloning* a repository from GitHub (highly recommended)


## B1. Cloning

The process of copying a Git repo from GitHub to your computer is called *cloning*. To clone a repository, we simply issue the `git clone` command followed by a URL.

The syntax looks like this:
```bash 
git clone https://github.com/$USERNAME/$REPO_NAME
```

Of course, you need to fill in the actual values above:
 * Replace $USERNAME with a GitHub username
 * Repalce $REPO_NAME with an actual repo name

The URL that you copy an existing repository from will almost always be the URL of somebody's repo on GitHub (or your own repo on GitHub). Directions for how to create your own repository on GitHub (that you then clone to your local machine) can be found here: [https://help.github.com/articles/create-a-repo/](https://help.github.com/articles/create-a-repo/)

## B2. Forking

*Forking* is kind of like *cloning*, but there are two important distinctions: 

* *Forking* occurs only on GitHub, and is specific to GitHub (i.e. you can't 
*fork* on your local machine - it's not an option). 
* *Forking* creates your own personalized copy of the repo on your GitHub account. Now, if you would like to make changes, you would clone your forked repository. Even if you don't have write access to the original repo, you can push new commits directly to your *fork* of the original repo.
* A *pull request* is a request *by you* for the owner of a repo to *pull* changes from your fork of that repo (and incorporate them into the original). Pull requests are useful for open-source projects, where anyone can propose changes and contribute code, but these proposed changes need to be reviewed and approved by the project owners before they get merged into the original project.

You will be asked to fork *this* repository, and submit pull requests when you have changes you are ready to submit. This will help you become more familiar with the workflows commonly used in a collaborative environment on a data science team. The only caveat is that you will only be submitting pull requests for changes to a specific *branch* set up for you. See below for explanation of what a branch is!


## D. Interacting with a Git Repository

Now that we have a Git repository, we can start working in that repository 
(directory), and have Git keep track of the changes that we are making to 
any of the files in our repo. The standard workflow within a Git repository 
is that you will change one or more files in the repository, possibly review
the changes, add them to the *index* (a file that Git uses to keep track of 
tracked files), and then create a new commit with those changes. Let's look
at some commands, and then we'll go into a little bit more detail about how
this all works. 

The following are all commands that we would issue on the command line from 
within our Git repository. Note that any time we issue a Git command, it 
will be prefixed by `git`. 

```bash
git status  # Do this EARLY and OFTEN. Red = bad, fix it!
git add foo.txt  # Add the file foo.txt to the staging area (green). 
git add bar/  # Add the folder bar/ (and all its contents).
git commit -m 'Add foo and bar.'  # Commit all staged items.
```

I've mentioned the *index* above, and while understanding it isn't necessary, it can help us to understand exactly how Git works. The *index* (which is hidden in the .git subdirectory of any Git repository) keeps track of all files that the Git repository is actually responsible for tracking. The `git add` command above will put files into the staging area. Once the file is committed with `git commit`, `git status` will only note *changes* to the file (i.e. what's different from the last time it was committed).

If you see something in *red* in `git status`, think of this as seeing "blood" on your repo. The goal is to fix it immediately. You do this by *adding* and *committing* your changes. It does NOT matter whether your code is working or "finished" because you can always commit additional changes later! Commit early and often to your repo.

Remember, *A.B.C.*: Always Be Committing.

### Branching
Branches can be thought of as "versions" of the git repository. The default branch that is intiated with the repository is referred to as *master* or *main*. These branch names refer to the original version, and are often reserved as the ground-truth, clean, best-versions of the repository. That said, developers can "check-out" (either create or literally check-out an existing one, like a library book) and develop on this branch. This provides a developer with a safe space to work on teh code, add his/her own work, and then safely "merge" it back into the *master* branch. In some cases, branches can be merged into automatically, and sometimes they will require a pull request, as with this repository. See the "Resources / Guides / " directory for a more in-depth view of this workflow and how we will use it. 


## D. Working with a Cloned Repository 

Now that we know how to clone a repository, it's time to talk about pushing
and pulling, the process by which we keep a remote copy of our repository (on GitHub) 
up to date and in sync with a local copy of our repository (and vice versa). 
Anytime that we have cloned a repository from a URL, the repository at that 
URL will become the *remote* copy of that repository. *Pulling* is the way that 
we will keep our local copy of the repository up to date with any changes made 
by others to the *remote*, and *pushing* is the way that we will keep 
the *remote* up to date with changes we have made locally.

Note that you will  have to have write access to the remote repo in order to be able to push your changes to it directly. 

You can see your *remotes* at any time:

```bash
git remote -v
```

Pushing and pulling only work properly when all changes have been *committed*. This means that if you  have made changes to a repository, but not gone through the process of *adding* and *committing* them, then issuing the push commands below will 
not actually push any changes to the remote repository. Similarly, if there have been 
no changes to the remote repository since you last issued a pull, then issuing 
the pull commands below will not actually pull anything.

**If you see blood in your `git status`, fix that *first* before running any other git commands.**

To push and pull: 

```bash 
git push  # Update the remote repo with new local commits from your computer. 
git pull  # Update the local repo on your computer with new commits from the remote.
```


Note that `git push` is normally short for `git push origin master` (push to the `master` branch on the remote called `origin`) and, similarly, `git pull` is short for `git pull origin master`.


# 2. Typical Git Workflow

## A. Personal Repositories

When developing in a personal repository, there is not always a need to create & develop on branches. If it is an important prokect, it is likely still worth it to preserve the good code while working on something new, before adding back into the original *master* branch. But consequently, you have free reign. 

## B1. Shared Repositories - Collaborative

When working on a shared rerpository, it is absolutely essential to be aware of (1) what other work is being done at the same time, and (2) what works before you merge. Shared repositories where your contributions are welcome are most likely what you'll come to find is the case in most data science teams. For this reason, There are some best practices & commonwokflows you can follow to ensure that everyone's work is protected. Let's say you are joining a team with an existting repository and they have added you as a collaborator, ad you are setting up your laptop at the start. You should:

1. Go to github, and click "Clone" to get the copy-link
2. Navigate to your local file system > Documents and create a new folder titled "Repositories"
3. Using your terminal, change directories into this new "Repository" directory
4. In the terminal, clone the repository:
```bash 
git clone https://github.com/$USERNAME/$REPO_NAME
```
5. Check to see if there are ay recent changes pushed by one of your teammates. In the terminal:
```bash 
git pull origin master
```
6. Create a new branch, for your development work
```bash 
git checkout -b <branch_name> # if a branch does not exist with this name, one will be created
```
7. Make a change (add a file, modify a file, etc)
8. Check to see that git has tracked your change:
```bash 
git status # Output should be either under "modified:" or "Untracked new files:", with the changeed/added file name afterwards
```
9. Stage your change
```bash 
git add filename_with_change.py
```
10. Commit the change to the *branch*, NOT *master*
```bash 
git push -u origin <branch_name>
```
11. Go to Github & submit a pull-request for your branch 


## B2. Shared Repositories - Forks
Forked repositories are similar to branches, except it's a duplicate that gets added to the account of the person who did the forking. As mentioned above, this can only be done on Github UI. That said, when you select a repository to fork, a copy of the repository will be added to your account, and you are even welcome to rename it. You are also welcome to make new branches, and make any changes that you want to *this* version of the repository. There are 2 things you'll want to keep in mind. (1) You will have to remember to update your version continuously if there are new files/changes to the original repository that are important for your work. And (2) your (forked) version *can* in fact be merged back into the original repository, through a pull request. This is the process we will follow; refer to the git_workflow.md file in the "Getting-Started" directory. 


# 3. Resources
There are many compelxities involved in working with collaborators in the Git/Github environment. You will continuously learn new commands like "reset", "rebase", and more. Trouble shooting issues with git can commonly be done by google-searcing for threads & documentation. A go-to site for help is "Stack Overflow", as well as the [github documentation](https://docs.github.com/en) itself. 