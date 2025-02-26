 # Development process instructions

## 1. Fork the Repository

Go to the original repository: https://github.com/maxdotio/agent-quick-hack
Click the "Fork" button in the top-right corner of the page to create a personal copy of the repository under 
your GitHub account MYACCOUNT.

## 2. Clone Your Fork Locally

Once you have forked the repository, clone it to your local machine to start making changes.  

```bash
# Clone your forked repository
git clone git@github.com/MYACCOUNT/agent-quick-hack.git
```

If that doesn't work, use https instead of ssh:

```bash
# Navigate into the cloned repository
git clone https://github.com/MYACCOUNT/agent-quick-hack
```

Then navigate into the cloned repository

```bash
cd agent-quick-hack
```

## 3. Add the Upstream Repository

To keep your fork updated with the original repository, add it as a remote:

```bash
# Add the original repository as a remote named 'upstream'
git remote add upstream https://github.com/maxdotio/agent-quick-hack.git
```

## 4. Fetch and Merge Updates from Upstream

When the team's changes are added to the original repo, you should fetch and merge the updates to keep your 
fork current:

```bash
# Fetch the latest changes from the upstream repository
git fetch upstream

# Checkout your local main branch
git checkout main

# Merge changes from upstream/main into your local main branch
git merge upstream/main
```

## 5. Resolve Any Conflicts

If there are any merge conflicts, resolve them using your preferred code editor. After resolving conflicts, 
stage the changes and complete the merge:

```bash
# After resolving conflicts
git add .

# Complete the merge
git commit -m "Merge updates from upstream"
```

## 6. Push the Updated Branch to Your Fork

Push the updated branch to your fork on GitHub:

```bash
git push origin main
```

## 7. Open a Pull Request

To get your changes added back to the main agent-quick-hack repo, you need to open a pull request in github and 
tell the team leader.
