# A "git repo" is just a directory tree containing a @.git/@ folder at the top level.
git init
ls -F .git

# File contents (but not names or other metadata) is stored in a "blob".
# Every blob is identified by a ~unique SHA-1 hash. The same contents always has the
# same hash, on any system. All git commands allow you to shorten a hash as long as
# you include enough digits to be unique within your repo.
echo "Hello, world" > hello.txt
git hash-object hello.txt
