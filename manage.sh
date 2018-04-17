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
	echo "Importing app..."
	src=$app
	for x in $xml; do
	    importXml
	done
	echo "Importing gscore..."
	cp $gscore/src/main/res/values/strings_gscore.xml gscore/strings_gscore.xml

	echo "Importing web..."
	src=$web
	for x in $pages; do
	    importContent
	done
elif [ "$choice" = "e" ]; then
	echo "Exporting app..."
	rm -rf $app/src/main/res/values-*
	cp -rf build/app/* $app/src/main/res/
	cd $app/src/main/res/
	git checkout -- values-w820*
	cd -

	echo "Exporting gscore..."
	rm -rf $gscore/src/main/res/values-*
	cp -rf build/gscore/* $gscore/src/main/res/
	cd $gscore/src/main/res/
	git checkout -- values-w820*
	cd -

	echo "Exporting web..."
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

	echo "Done. Check removed files."
else
    echo "Cancelled"
fi
