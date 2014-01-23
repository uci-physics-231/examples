# A "git repo" is just a directory tree containing a @.git/@ folder at the top level.
git init
ls -F .git

# File contents (but not names or other metadata) is stored in a "blob".
# Every blob is identified by a ~unique SHA-1 hash. The same contents always has the
# same hash, on any system.
echo "Hello, world" > hello.txt
git hash-object hello.txt

# A different file with the same contents has the same hash.
echo "Hello, world" > hello2.txt
git hash-object hello2.txt

# The git db stores snapshots of the contents of each file you are tracking, but it is
# up to you to decide which snapshots to remember. A "commit" is a set of snapshots for 
# all the files you are tracking. It is often useful to commit something different than
# current state of all the files in your "working tree", so git provides a staging area
# (the binary file @.git/index@) where you prepare the next commit.

# To add a file to the staging area, use:
git add hello.txt

# You now have your first tracked object in the repo db (but it is still only staged to the index)
find .git/objects -type f

# Tracked contents is saved in binary "blob" format, but can always be reconstructed:
git cat-file -t a5c19667710254f835085b99726e523457150e03
git cat-file -p a5c19667710254f835085b99726e523457150e03

# All git commands allow you to shorten a hash as long as you include enough digits to be
# unique within your repo.
git cat-file -p a5c1

# Content is stored in a flat db and doesn't know where it belongs in a directory tree,
# so files with different names but the same contents are only stored once.
git add hello2.txt
find .git/objects -type f

# The 'git status' command lists the files in your staging area (index)
git status

# It also shows any files that have changed but not been staged
echo "Bonjour, monde." > bonjour.txt
git status

# An empty subdirectory has no new content, so is ignored by git
mkdir french
git status

# Any subdirectory with new contents will be flagged and can be added
mv bonjour.txt french/
git status

# Adding a directory adds all of its contents
git add french
git status

# We now have two stored "blob" objects (for our 3 files)
find .git/objects -type f

# Finally, let's "commit" the staged changes to the repo, which stores permanent
# snapshots of the contents of our three files (in "blob" objects), as well as
# their layout in the file system (using "tree" objects).  The commit action requires
# that you provide some descriptive text, that becomes an important (and permanent)
# part of your project's documentation.
git commit -m "My first commmit"
