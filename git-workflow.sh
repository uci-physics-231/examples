# Git is a low-level tool for managing version content. A git "workflow" is a set of guidelines
# for effectively using Git on a project. There are many possible workflows and the right one
# for a given project depends on the number of developers and the complexity of the project.

# Every git commit object has zero, one, or more parent commits. The initial commit has no parent
# and most commits just have a single parent. When two commits share the same parent, we call
# this a "branch". When one commit has multiple parents, we call this a "merge". Lets create
# some commits to get started.
git init
echo "a" > a
git add a
git commit --quiet -m 'a'
echo "b" > b
git add b
git commit --quiet -m 'b'
echo "c" > c
git add c
git commit --quiet -m 'c'

# The commit history forms a directed acyclic graph (DAG) that can get quite complex. The following
# command displays the DAG nicely:
git log --graph --pretty=format:'%h%d %s (by %an %ar)' --all

# You can save an alias for this using (add the @--global@ option to use the alias on all your local repos)
git config alias.dag "log --graph --pretty=format:'%h%d %s (by %an %ar)' --all"
git dag

# Every leaf node of the DAG is a named "branch". The initial branch is named @master@.
# @HEAD@ is an alias for your current branch. To create a new branch named @feature-1@ from
# @master@ branch, use:
git branch feature-1 master

# Note that you are still on the master branch
git status

# To switch between branches, use @git checkout@.
git checkout feature-1
git status

# Now let's add some content on this new branch
echo "d" > d
git add d
git commit --quiet -m 'd'
echo "e" > e
git add e
git commit --quiet -m 'e'
git dag

# Suppose someone else (or perhaps you) is working on a different feature in a separate branch.
# Note how we combine the @branch@ and @checkout@ commands into a single @checkout@ command.
git checkout -b feature-2 master
echo "f" > f
git add f
git commit --quiet -m 'f'
echo "g" > g
git add g
git commit --quiet -m 'g'
echo "h" > h
git add h
git commit --quiet -m 'h'
git dag

# Note that switching between branches will generally change files in your working
# tree if they are being tracked in the repo, but this is safe because they are tracked!
ls -F
git checkout master
ls -F

# To see all your active branches, use (the current branch is marked with an asterisk)
git branch -v

# The @git diff@ command lets you compare any two commits (leave off the @--stat@ option
# for more details). You can refer to leaf-node commits using their branch names.
git diff --stat feature-1 feature-2

# You can also refer to any commit using its (abbreviated) hash or using "tree-ish" aliases, e.g.
git diff --stat HEAD HEAD^

# A good workflow practice is to think of your @master@ branch as the public face of
# your project, so you can work freely on topic branches and then merge completed
# new features back to the @master@ branch when you are ready. To merge @feature-1@:
git checkout master
git merge feature-1
git dag

# Similarly for @feature-2@
git checkout master
git merge feature-2
git dag

# The git merge logic will automatically do the right thing when it is obvious what that
# means. For example, as long as the branches being merged agree on the files they have
# in common, the merge yields the union of all the files. However, when two branches have
# changed the same file, some manual editing to resolve the conflict is often required
# (see @man git-merge@ for details). This is generally painful, but breaking your work into
# many small commits will make it easier (and is a good idea anyway).
