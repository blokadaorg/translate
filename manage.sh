#!/bin/bash
# A simple script to pull English strings from sources
# and push translated strings to sources.
#
# Syntax:
# ./manage.sh app-path web-path gscore-path
#
# Arguments:
# - app-path - Where is Blokada app repo
# - gscore-path - Where is gscore lib repo
# - web-path - Where is Blokada website repo

xml="filter main notification tunnel update dns"
pages="cleanup.html donate.html help.html intro.html obsolete.html updated.html help_dns.html intro_dns.html filters.properties dns.properties"

x=""

function importXml {
    cp "$src/src/main/res/values/strings_$x.xml" "app/strings_$x.xml"
}

function importContent {
    cp "$src/api/v3/canonical/strings/$x" "content/$x"
}

app=$1
web=$2
gscore=$3

echo "app: $app"
echo "web: $web"
echo "gscore: $gscore"
echo "xml: $xml"
echo "pages: $pages"
echo ""

read -p "Do you want to import sources (i) or export translations (e)? (i/e) " choice
if [ "$choice" = "i" ]; then
	echo "Importing xml..."
	src=$app
	for x in $xml; do
	    runXml
	done
	src=$gscore
	x="gscore"
	runXml

	echo "Importing web..."
	src=$web
	for x in $pages; do
	    runPages
	done
elif [ "$choice" = "e" ]; then
	echo "Exporting xml..."
	rm -rf $app/src/main/res/values-*
	cp -rf build/app/* $app/src/main/res/

	rm -rf $gscore/src/main/res/values-*
	cp -rf build/gscore/* $gscore/src/main/res/

	echo "Exporting web..."
	rm -rf $web/api/v3/content/*
	cp -rf $web/api/v3/canonical/strings $web/api/v3/content/en
	cp -rf build/content/* $web/api/v3/content/
	for D in $web/api/v3/content/*/; do
		cp -r $web/api/v3/canonical/cache $d/
		cp -r $web/api/v3/canonical/css $d/
	done

	echo "Done. Check removed files."
else
    echo "Cancelled"
fi
