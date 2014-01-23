# A "git repo" is just a directory tree containing a @.git/@ folder at the top level.
git init
ls -CF .git

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

# You now have 2 "blob" objects, 2 "tree" objects, and 1 "commit" object in your db.
find .git/objects -type f

# A "tree" object represents one node in a directory tree, and includes file names
# and (simplified) file permissions, e.g.
git cat-file -p f4a3

# The "commit" object saves the top-level "tree" node and who/why/when metadata.
# Since the commit's contents includes this metadata, its hash value does also and
# will be different when you run this command (unlike the blob and tree hash values).
# You can inspect your most recent commit object using
git log -1

# For your second commit, lets change one of the files.
echo "Welcome" >> hello.txt
git status

# Although this file is already tracked, we still need to "add" changes to save
# a new snapshot. This creates a new "blob" object for an old file, because
# its contents has changed.
git add hello.txt
find .git/objects -type f

# Commit the change to record a new snapshot of @hello.txt@ (along with the old snapshots
# of the other files we are tracking). Note that a commit already records what changed, so
# your message should focus on why it changed.
git commit -m "Expand upon the English version"

# In addition to creating or changing content ("add"), you can also remove content
# (see @man git-rm@), in which case old snapshots are still retained, or move contents
# to another directory or filename (see @man git-mv@). In both of these cases, only
# "tree" objects are changed.

# Its fine to leave some changes unstaged when you commit, but if you have files that
# you never intend to commit you should ignore them properly (see @man gitignore@).

# Now that you have seen the insides of git, you will normally just use the @git add@ command
# to move changes into the index (remember that edits are also called 'adds'), followed by
# a @git commit@.