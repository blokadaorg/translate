#!/bin/sh

echo "Reseting repo state"

git reset --hard --recurse-submodule

echo "Done"