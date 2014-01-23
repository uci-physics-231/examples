# List the examples we build
EXAMPLES = git-internals git-workflow

# Specify the path of our wiki repo
WIKI_REPO = ../examples.wiki

# We build the corresponding list of .textile files by default
default : $(EXAMPLES:%=%.textile)

# How to build *.textile from *.sh
%.textile : %.sh
	./shtowiki.py -i $<
	cp $@ $(WIKI_REPO)
	cd $(WIKI_REPO) && git add $@

# Updates our wiki on github
update :
	cd $(WIKI_REPO) && git commit -m 'Makefile automatic update' && git push
