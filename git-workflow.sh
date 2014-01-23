# Git is a low-level tool for managing version content. A git "workflow" is a set of guidelines
# for effectively using Git on a project. There are many possible workflows and the right one
# for a given project depends on the number of developers and the complexity of the project.

# Every git commit object has zero, one, or more parent commits. The initial commit has no parent
# and most commits just have a single parent. When two commits share the same parent, we call
# this a "branch". When one commit has multiple parents, we call this a "merge". Lets create
# some commits to get started.
git init
touch a
git add a
git commit --quiet -m 'a'
touch b
git add b
git commit --quiet -m 'b'
touch c
git add c
git commit --quiet -m 'c'

# The commit history forms a directed acyclic graph (DAG) that can get quite complex. The following
# command displays the DAG nicely:
git log --graph --pretty=format:'%h%d %s (by %an %ar)' --all

# You can save an alias for this using (add the @--global@ option to use the alias on all your local repos)
git config alias.dag "log --graph --pretty=format:'%h%d %s (by %an %ar)' --all"
git dag

