pip3 uninstall tlist
git rm -r dist
git rm -r build
git rm -r tlist.egg-info
rm -r dist
rm -r build
rm -r tlist.egg-info
git add .
git commit -m "remove old build"
