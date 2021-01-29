#!/usr/bin/python3

'''
This file is part of Blokada.

Blokada is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Blokada is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Blokada.  If not, see <https://www.gnu.org/licenses/>.

Copyright © 2020 Blocka AB. All rights reserved.

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
        print("Actions: ios, android5, android4, landing, dashboard, landing-gp")

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

    with open('../langs.js') as langs_file:
        langs = json.load(langs_file)

    for opt, arg in opts:
        if opt == "-a":
            config["action"] = arg
        else:
            print("  Unknown argument: %s" % opt)
            usage()
            return 2

    if config["action"] not in ["ios", "android5", "android4", "landing", "dashboard", "landing-gp"]:
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
    elif config["action"] == "landing":
        webSync(config["translate_dir"], config["target_dir"])
        webImport(langs["langs"], config["translate_dir"], config["target_dir"])
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
        shutil.rmtree(f"{mobile}/ios/IOS/Assets/en.lproj")
    except:
        pass
    try:
        shutil.copytree(f"{translate}/v5", f"{mobile}/ios/IOS/Assets/en.lproj")
    except:
        pass

def iosImport(langs, translate, mobile):
    print(f"  Importing to iOS")
    for lang in langs:
        print(f"    importing: {lang}")
        try:
            shutil.rmtree(f"{mobile}/ios/IOS/Assets/{lang}.lproj")
        except:
            pass
        try:
            shutil.copytree(f"{translate}/build/v5/{lang}.lproj", f"{mobile}/ios/IOS/Assets/{lang}.lproj")
        except:
            pass

def android5Sync(translate, mobile):
    print("  Syncing Android 5")

    if not os.path.exists(f"{mobile}/android5/app/src/main/assets/translations/root"):
        os.makedirs(f"{mobile}/android5/app/src/main/assets/translations/root")

    subprocess.call(f"./convert.py -i {translate}/v5/Ui.strings -o {mobile}/android5/app/src/main/res/values/strings_ui.xml", shell = True)
    subprocess.call(f"./convert.py -i {translate}/v5/PackTags.strings -o {mobile}/android5/app/src/main/assets/translations/root/tags.json -f \"json\"", shell = True)
    subprocess.call(f"./convert.py -i {translate}/v5/Packs.strings -o {mobile}/android5/app/src/main/assets/translations/root/packs.json -f \"json\"", shell = True)

def android5Import(langs, langs_android, translate, mobile):
    print(f"  Importing to Android 5")
    for lang in langs:
        print(f"    importing {lang}")
        alang = langs_android.get(lang, lang)

        if not os.path.exists(f"{mobile}/android5/app/src/translations/res/values-{alang}"):
            os.makedirs(f"{mobile}/android5/app/src/translations/res/values-{alang}")
        if not os.path.exists(f"{mobile}/android5/app/src/main/assets/translations/{lang}"):
            os.makedirs(f"{mobile}/android5/app/src/main/assets/translations/{lang}")

        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/PackTags.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/tags.json -f \"json\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/Packs.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/packs.json -f \"json\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/Ui.strings -o {mobile}/android5/app/src/main/assets/translations/{lang}/ui.json -f \"json\"", shell = True)
        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/Ui.strings -o {mobile}/android5/app/src/translations/res/values-{alang}/strings_ui.xml -f \"xml\"", shell = True)

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

def webSync(translate, web):
    print(f"  Syncing web ({web})")
    subprocess.call(f"./convert.py -i {translate}/v5/Ui.strings -o {web}/src/locales/en.json -f \"json_vue\"", shell = True)

def webImport(langs, translate, web):
    print(f"  Importing strings to web ({web})")
    for lang in langs:
        print(f"    importing {lang}")
        subprocess.call(f"./convert.py -i {translate}/build/v5/{lang}.lproj/Ui.strings -o {web}/src/locales/{lang}.json -f \"json_vue\"", shell = True)

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

def outputAsAndroidXml(output_file, strings):
    with open(output_file, "w") as f:
        f.write("<resources>\n")
        for key in strings:
            f.write(f"    <string name=\"{makeAndroidKey(key)}\">{makeAndroidValue(strings[key])}</string>\n")
        f.write("</resources>\n")

def outputAsJson(output_file, strings):
    with open(output_file, "w") as f:
        f.write("{ \"strings\": {\n")
        count = 0
        for key in strings:
            count += 1
            f.write(f"    \"{key}\": \"{strings[key]}\"")
            if count < len(strings):
                f.write(",")
            f.write("\n")
        f.write("} }\n")

def makeAndroidKey(line):
    line = remove_chars(line, keep=ascii_letters + ' ')
    line = line.replace(" ", "_")
    return line.lower()

def makeAndroidValue(line):
    line = line.replace("&", "&amp;")
    line = line.replace("'", "\\'")
    return line

def remove_chars(input_string, keep):
    return ''.join([_ for _ in input_string if _ in keep])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
