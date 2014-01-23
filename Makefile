# List the examples we build
EXAMPLES = git-internals

# Specify the path of our wiki repo
WIKI_REPO = ../examples.wiki

# We build the corresponding list of .textile files by default
default : $(EXAMPLES:%=%.textile)

# How to build *.textile from *.sh (or if the Makefile is changed)
%.textile : %.sh Makefile
	./shtowiki.py -i $<
	mv $@ $(WIKI_REPO)
	cd $(WIKI_REPO) && git add $@

# Updates our wiki on github
update :
	cd $(WIKI_REPO) && git commit -m 'Makefile automatic update' && git push
