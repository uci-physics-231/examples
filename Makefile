# List the examples we build
EXAMPLES = git-internals

# We build the corresponding list of .textile files by default
default : $(EXAMPLES:%=%.textile)

# How to build .textile from .sh
%.textile : %.sh Makefile
	./shtowiki.py -i $<
	mv $@ ../examples.wiki
