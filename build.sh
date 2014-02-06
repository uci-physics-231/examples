# generate .textile file from each .sh
./shtowiki.py -i git-internals.sh
./shtowiki.py -i git-workflow.sh

# copy new files to wiki folder
cp git-internals.textile ../examples.wiki
cp git-workflow.textile ../examples.wiki

# add new files to wiki repo
cd ../examples.wiki
git add git-internals.textile
git add git-workflow.textile

# commit and push the changes to github
git commit -m 'build.sh automatic update'
git push
