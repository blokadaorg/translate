#!/usr/bin/python3

'''
This file is part of Blokada.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

Copyright © 2021 Blocka AB. All rights reserved.

@author Karol Gusak (karol@blocka.net)
'''

'''
Manages translations for all Blokada projects.

Actions:
- sync: pulls source strings (en) from translate repo to all projects
- import: pulls translated strings (all languages) from translate repo to all projects
'''

import sys
import os
import getopt
import glob
import json
import shutil
import re
import subprocess
from os import path

def main(argv):
    def usage():
        print("usage: translate -a action")
        print("Actions: ios, android5, android4, common, landing, dashboard, landing-gp")

    print("Translate v0.4")

    # parse command line options
    base_path = "."
    config = {
        "translate_dir": "..",
        "target_dir": "../..",
        "action": None,
    }

    try:
        opts, _ = getopt.getopt(argv, "r:a:")
    except getopt.GetoptError:
        print("  Bad parameters")
        usage()
        return 1

    with open('../langs.js', 'r') as langs_file:
        data = langs_file.read().replace('export default ', '')
        langs = json.loads(data)

    for opt, arg in opts:
        if opt == "-a":
            config["action"] = arg
        else:
            print("  Unknown argument: %s" % opt)
            usage()
            return 2

    if config["action"] not in ["ios", "android5", "android4", "common", "landing", "dashboard", "landing-gp"]:
        print("  Unknown action")
        usage()
        return 1

    print(config)
    print("")
    print(f"Action: {config['action']}")

    repo = path.join(base_path, config["translate_dir"])
    if config["action"] == "ios":
        iosSync(config["translate_dir"], config["target_dir"])
        iosImport(langs["langs"], config["translate_dir"], config["target_dir"])
    elif config["action"] == "android5":
        android5Sync(config["translate_dir"], config["target_dir"])
        android5Import(langs["langs"], langs["langs-android"], config["translate_dir"], config["target_dir"])
    elif config["action"] == "android4":
        android4Sync(config["translate_dir"], config["target_dir"])
        android4Import(langs["langs"], langs["langs-android-res"], config["translate_dir"], config["target_dir"])
    elif config["action"] == "common":
        android4Sync(config["translate_dir"], config["target_dir"])
        android4Import(langs["langs"], langs["langs-web4"], config["translate_dir"], config["target_dir"])
    elif config["action"] == "landing":
        landingSync(config["translate_dir"], config["target_dir"])
        landingImport(langs["langs"], config["translate_dir"], config["target_dir"])
    elif config["action"] == "landing-gp":
        web4Sync(config["translate_dir"], config["target_dir"])
        web4Import(langs["langs"], langs["langs-web4"], config["translate_dir"], config["target_dir"])
    elif config["action"] == "dashboard":
        webSync(config["translate_dir"], config["target_dir"])
        webImport(langs["langs"], config["translate_dir"], config["target_dir"])

    print("Done")

def iosSync(translate, mobile):
    print(f"  Syncing iOS")
    try:
        shutil.rmtree(f"{mobile}/ios/App/Assets/en.lproj")
    except:
        pass
    try:
        shutil.copytree(f"{translate}/v6", f"{mobile}/ios/App/Assets/en.lproj")
    except:
        pass

def iosImport(langs, translate, mobile):
    print(f"  Importing to iOS")
    for lang in langs:
        print(f"    importing: {lang}")
        try:
            shutil.rmtree(f"{mobile}/ios/App/Assets/{lang}.lproj")
        except:
            pass
        try:
            shutil.copytree(f"{translate}/build/v6/{lang}.lproj", f"{mobile}/ios/App/Assets/{lang}.lproj")
        except:
            pass

def android5Sync(translate, mobile):
    print("  Syncing Android 5")

    if not os.path.exists(f"{mobile}/android5/app/src/main/assets/translations/root"):
        os.makedirs(f"{mobile}/android5/app/src/main/assets/translations/root")

    subprocess.call(f"./convert.py -i {translate}/v6/Ui.strings -o {mobile}/android5/app/src/main/res/values/strings_ui.xml", shell = True)
    subprocess.call(f"./convert.py -i {translate}/v6/PackTags.strings -o {mobile}/android5/app/src/main/assets/translations/root/tags.json -f \"json\"", shell = True)
    subprocess.call(f"./convert.py -i {translate}/v6/Packs.strings -o {mobile}/android5/app/src/main/assets/translations/root/packs.json -f \"json\"", shell = True)
    subprocess.call(f"./convert.py -i {translate}/v5/Android.strings -o {mobile}/android5/app/src/main/res/values/strings_android.xml", shell = True)

def android5Import(langs, langs_android, translate, mobile):
    print(f"  Importing to Android 5")
    for lang in langs:
        print(f"    importing {lang}")
        alang = langs_android.get(lang, lang)

        if not os.path.exists(f"{mobile}/android5/app/src/translations/res/values-{alang}"):
            os.makedirs(f"{mobile}/android5/app/src/translations/res/values-{alang}")
        if not os.path.exists(f"{mobile}/android5/app/src/main/assets/translations/{lang}"):
            os.makedirs(f"{mobile}/android5/app/src/main/assets/translations/{lang}")

        subprocess.call(f"./convert.py -i {translate}/build/v6/{lang}.lproj/PackTags.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/tags.json -f \"json\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v6/{lang}.lproj/Packs.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/packs.json -f \"json\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v6/{lang}.lproj/Ui.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/ui.json -f \"json\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v6/{lang}.lproj/Ui.strings -o {mobile}/android5/app/src/translations/res/values-{alang}/strings_ui.xml -f \"xml\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/Android.strings -o {mobile}/android5/app/src/translations/res/values-{alang}/strings_android.xml -f \"xml\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/Android.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/android.json -f \"json\"", shell = True)

def android4Sync(translate, mobile):
    print("  Syncing Android 4")
    for fl in glob.glob(f"{translate}/v4/strings_*"):
        shutil.copy(fl, f"{mobile}/android4/app/src/ui-blokada/res/values/")

def android4Import(langs, langs_android, translate, mobile):
    print("  Importing strings to Android 4")
    for lang in langs:
        print(f"    importing {lang}")
        alang = langs_android.get(lang, lang)

        dst = f"{mobile}/android4/app/src/main/res/values-{alang}"
        shutil.rmtree(dst)
        shutil.copytree(f"{translate}/build/v4/android/values-{alang}", dst)

def commonSync(translate, mobile):
    print("  Syncing Common")

    if not os.path.exists(f"{mobile}/common/lib/l10n"):
        os.makedirs(f"{mobile}/common/lib/l10n")

    subprocess.call(f"./convert.py -i {translate}/v6/Ui.strings -o {mobile}/common/lib/l10n/ui_en.arb -f \"arb\"", shell = True)

def commonImport(langs, langs_web4, translate, mobile):
    print(f"  Importing to Common")
    for lang in langs:
        print(f"    importing {lang}")
        alang = langs_web4.get(lang, lang)

        subprocess.call(f"./convert.py -i {translate}/build/v6/{lang}.lproj/Ui.strings -o {mobile}/common/lib/l10n/ui_{alang}.arb -f \"arb\"", shell = True)

def landingSync(translate, web):
    print(f"  Syncing landing ({web})")
    subprocess.call(f"./convert.py -i {translate}/landing/Homepage.strings -o {web}/src/locales/en.json -f \"json_vue\"", shell = True)

def landingImport(langs, translate, web):
    print(f"  Importing strings to landing ({web})")
    for lang in langs:
        print(f"    importing {lang}")
        subprocess.call(f"./convert.py -i {translate}/build/landing/{lang}.lproj/Homepage.strings -o {web}/src/locales/{lang}.json -f \"json_vue\"", shell = True)

def webSync(translate, web):
    print(f"  Syncing web ({web})")
    subprocess.call(f"./convert.py -i {translate}/v6/Ui.strings -o {web}/src/locales/en.json -f \"json_vue\"", shell = True)

def webImport(langs, translate, web):
    print(f"  Importing strings to web ({web})")
    for lang in langs:
        print(f"    importing {lang}")
        subprocess.call(f"./convert.py -i {translate}/build/v6/{lang}.lproj/Ui.strings -o {web}/src/locales/{lang}.json -f \"json_vue\"", shell = True)

def web4Sync(translate, web):
    print(f"  Syncing web v4 ({web})")
    shutil.copy(f"{translate}/v4/dns.properties", f"{web}/api/v4/canonical/strings/dns.properties")
    shutil.copy(f"{translate}/v4/filters.properties", f"{web}/api/v4/canonical/strings/filters.properties")

def web4Import(langs, langs_web4, translate, web):
    print(f"  Importing v4 strings to web ({web})")

    print(f"    importing root: (en)")
    dst = f"{web}/api/v4/content/en"
    shutil.rmtree(dst)
    shutil.copytree(f"{web}/api/v4/canonical/strings", dst, dirs_exist_ok = True)
    shutil.copytree(f"{web}/api/v4/canonical/defaults", dst, dirs_exist_ok = True)

    for lang in langs:
        l = langs_web4[lang]
        print(f"    importing {l}")
        dst = f"{web}/api/v4/content/{l}"
        shutil.rmtree(dst)
        shutil.copytree(f"{web}/api/v4/canonical/strings", dst, dirs_exist_ok = True)
        shutil.copytree(f"{web}/api/v4/canonical/defaults", dst, dirs_exist_ok = True)
        shutil.copytree(f"{translate}/build/v4/content/{l}", dst, dirs_exist_ok = True)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
