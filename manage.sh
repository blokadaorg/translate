#!/bin/bash
# A simple script to pull English strings from sources
# and push translated strings to sources.
#
# Syntax:
# ./manage.sh app-path web-path
#
# Arguments:
# - app-path - Where is Blokada app repo
# - web-path - Where is Blokada website repo

xml="filter main notification tunnel update dns gscore panel logger widget"
pages="cleanup.html donate.html help.html intro.html obsolete.html updated.html help_dns.html intro_dns.html filters.properties dns.properties"

x=""

function importXml {
    cp "$src/src/legacy/res/values/strings_$x.xml" "app/strings_$x.xml"
}

function importContent {
    cp "$src/api/v3/canonical/strings/$x" "content/$x"
}

function importWeb {
    cp "$src/index.html" "web/index.html"
}

app=$1
web=$2

echo "app: $app"
echo "web: $web"
echo "xml: $xml"
echo "pages: $pages"
echo ""

read -p "Do you want to import sources (i), export translations (e), or refetch English (r)? (i/e/r) " choice
if [ "$choice" = "i" ]; then
	echo "Importing app..."
	src=$app
	for x in $xml; do
	    importXml
	done

	echo "Importing web..."
	src=$web
	importWeb

	echo "Importing content..."
	for x in $pages; do
	    importContent
	done
elif [ "$choice" = "e" ]; then
	echo "Exporting app..."
	rm -rf $app/src/legacy/res/values-*
	cp -rf build/app/* $app/src/legacy/res/

	# English is not exported by default
	rm -rf $app/src/legacy/res/values-en-rUS

	# Some files should not be removed. Revert
	cd $app/src/legacy/res/
	git checkout -- values-w420dp-port
	git checkout -- values-w840dp-land
	git checkout -- values-w960dp
	cd -

	echo "Exporting web..."
	rm -rf $web/lang/*

	cp -rf build/web/* $web/local/
	for D in $web/local/*/; do
		cp -r $web/css $D/
		cp -r $web/js $D/
		ln -s $web/static $D/static
		ln -s $web/img $D/img
	done

	echo "Exporting content..."
	rm -rf $web/api/v3/content/*

	mkdir $web/api/v3/content/en
	cp -r $web/api/v3/canonical/css $web/api/v3/content/en/
	cp $web/api/v3/canonical/strings/* $web/api/v3/content/en/
	cp $web/api/v3/canonical/defaults/* $web/api/v3/content/en/

	cp -rf build/content/* $web/api/v3/content/
	for D in $web/api/v3/content/*/; do
		cp -r $web/api/v3/canonical/css $D/
		cp $web/api/v3/canonical/defaults/* $D/
		cp -n $web/api/v3/canonical/strings/* $D/
	done

	# English is not exported by default
	rm -rf $web/api/v3/content/en_US

	echo "Exporting web (dns)..."
	rm -rf $web/api/v3/content_dns/*

	mkdir $web/api/v3/content_dns/en
	cp -r $web/api/v3/canonical/css $web/api/v3/content_dns/en/
	cp $web/api/v3/canonical/strings/* $web/api/v3/content_dns/en/
	cp $web/api/v3/canonical/defaults/* $web/api/v3/content_dns/en/

	cp -rf build/content/* $web/api/v3/content_dns/
	for D in $web/api/v3/content_dns/*/; do
		cp -r $web/api/v3/canonical/css $D/
		cp $web/api/v3/canonical/defaults/* $D/
		cp -n $web/api/v3/canonical/strings/* $D/
		mv $D/intro_dns.html $D/intro.html
		mv $D/help_dns.html $D/help.html
		mv $D/filters_dns.txt $D/filters.txt
	done

	# English is not exported by default
	rm -rf $web/api/v3/content_dns/en_US

	echo "Done. Check removed files."
elif [ "$choice" = "r" ]; then
	echo "Refetching English in app..."
	cp -rf build/app/values-en-rUS/* $app/src/legacy/res/values/

	echo "Refetching English in web..."
	cp -rf build/content/en_US/*.html $web/api/v3/canonical/strings/

	echo "Done. Don't forget to export."
else
    echo "Cancelled"
fi
