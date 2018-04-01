#!/bin/bash
# A simple script to pull English strings from sources
#
# Syntax:
# ./pull.sh app-path web-path gscore-path
#
# Notes:
# - app-path - Where is Blokada app repo
# - gscore-path - Where is gscore lib repo
# - web-path - Where is Blokada website repo

xml="filter main notification tunnel update dns"
pages="cleanup donate help intro obsolete updated help_dns intro_dns"
props="filters dns"

l=""
x=""

function runXml {
    cp "$src/src/main/res/values/strings_$x.xml" "app/strings_$x.xml"
}

function runPages {
    cp "$src/api/v3/canonical/strings/$x.html" "content/$x.html"
}

function runProps {
    cp "$src/api/v3/canonical/strings/$x.properties" "content/$x.properties"
}

app=$1
web=$2
gscore=$3

echo "app: $app"
echo "gscore: $gscore"
echo "web: $web"
echo "xml: $xml"
echo "pages: $pages"
echo "properties: $props"
echo ""

read -p "Continue? (y/n) " choice
if [ "$choice" = "y" ]; then
    echo "Running..."
	src=$app
	for j in $xml; do
	    x="$j"
	    runXml
	done
	src=$gscore
	x="gscore"
	runXml
	src=$web
	for j in $pages; do
	    x="$j"
	    runPages
	done
	for j in $props; do
	    x="$j"
	    runProps
	done
else
    echo "Cancelled"
fi
