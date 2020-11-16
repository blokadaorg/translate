#!/bin/sh

echo "Importing translations to all repos (will push)"

cd translate
git checkout master
git pull
hash=$(git rev-parse --short HEAD)
commit="translate: sync translations to: $hash"
cd ..

echo $commit

cd dashboard
git checkout master
git pull
cd ..

cd landing
git checkout master
git pull
cd ..

cd blokada5
git checkout 5
git pull
cd ..

cd blokada4
git checkout 4
git pull
cd ..

./translate.py -a import

cd dashboard
git commit -am "$commit"
git push
cd ..

cd landing
git commit -am "$commit"
git push
cd ..

cd blokada5
git commit -am "$commit"
git push
cd ..

cd blokada4
git commit -am "$commit"
git push
cd ..

git add .
git commit -am "$commit"
git push

echo "Done"