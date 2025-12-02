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
Converts iOS translation file to one of:
- android XML translation format
- android json format (used for runtime translating from assets)
- vue json format (used for web dashboard and homepage)
- flutter json format (used by flutter) - same as vue actually, plain json
'''

import sys
import os
import getopt
import re
from os import path
from string import ascii_letters

def main(argv):
    def usage():
        print("usage: convert -i <input-file.strings> [-o <output-file.xxx>] [-k <key_prefix>] [-f <xml|json|vue|flutter>]")
        print("Default output file is ./strings")

    print("Convert Strings v0.2")

    # parse command line options
    base_path = "."
    config = {
        "input": None,
        "output": "strings",
        "key_prefix": "",
        "json": False,
        "vue": False,
        "flutter": False
    }

    try:
        opts, _ = getopt.getopt(argv, "i:o:k:f:")
    except getopt.GetoptError:
        print("  Bad parameters")
        usage()
        return 1

    for opt, arg in opts:
        if opt == "-i":
            config["input"] = arg
        elif opt == "-o":
            config["output"] = arg
        elif opt == "-k":
            config["key_prefix"] = arg
        elif opt == "-f":
            config["json"] = arg.startswith("json")
            config["vue"] = "vue" in arg
            config["flutter"] = "flutter" in arg
        else:
            print("  Unknown argument: %s" % opt)
            usage()
            return 2

    # check for mandatory parameters
    if not config["input"]:
        print("  Missing input parameter")
        usage()
        return 1

    print(config)

    print("Converting...")
    input_file = path.join(base_path, config["input"])
    output_file = path.join(base_path, config["output"])
    counter = 0

    strings = {}
    #seenEndOfTopComment = False
    seenEndOfTopComment = True # Not using for now
    with open(input_file) as f:
        for line in f:
            if line.startswith("*/"):
                seenEndOfTopComment = True
                continue
            elif not seenEndOfTopComment:
                continue
            elif line.startswith("//"):
                continue
            elif not line:
                continue

            name, var = line.partition("=")[::2]
            name = name.strip().strip("\"")
            var = var.strip().strip("\"")

            if not name or not var:
                continue

            strings[name] = var.replace("\";", "")
            counter += 1

    if config["vue"]:
        outputAsJsonVue(output_file, strings)
    elif config["json"]:
        outputAsJson(output_file, strings)
    elif config["flutter"]:
        outputAsFlutter(output_file, strings)
    else:
        outputAsAndroidXml(output_file, strings)

    print(f"Converted {counter} strings")

def outputAsAndroidXml(output_file, strings):
    with open(output_file, "w") as f:
        f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        f.write("<resources>\n")
        for key in strings:
            f.write(f"    <string name=\"{makeAndroidKey(key)}\">{convertPlaceholders(makeAndroidValue(strings[key]))}</string>\n")
        f.write("</resources>\n")

def outputAsJson(output_file, strings):
    with open(output_file, "w") as f:
        f.write("{ \"strings\": {\n")

        count = 0
        for key in strings:
            count += 1
            f.write(f"    \"{key}\": \"{convertPlaceholders(strings[key])}\"")
            if count < len(strings):
                f.write(",")
            f.write("\n")

        f.write("} }\n")

def outputAsJsonVue(output_file, strings):
    with open(output_file, "w") as f:
        f.write("{\n")

        count = 0
        for key in strings:
            count += 1
            f.write(f"    \"{key}\": \"{convertPlaceholdersToVue(strings[key])}\"")
            if count < len(strings):
                f.write(",")
            f.write("\n")

        f.write("}\n")

def outputAsFlutter(output_file, strings):
    with open(output_file, "w") as f:
        f.write("{\n")

        count = 0
        for key in strings:
            count += 1
            f.write(f"    \"{key}\": \"{convertPlaceholders(strings[key])}\"")
            if count < len(strings):
                f.write(",")
            f.write("\n")

        f.write("}\n")

def makeAndroidKey(line):
    # Android does not support numbers. Replace the common ones.
    line = line.replace("1", "one")
    line = line.replace("2", "two")
    line = line.replace("3", "three")
    line = line.replace("4", "four")
    line = line.replace("5", "five")
    line = line.replace("6", "six")
    line = line.replace("7", "seven")
    line = line.replace("8", "eight")
    line = line.replace("9", "nine")

    line = remove_chars(line, keep=ascii_letters + ' ')
    line = line.replace(" ", "_")
    return line.lower()

def makeAndroidValue(line):
    line = line.replace("&", "&amp;")
    line = line.replace("'", "\\'")
    return line

def makeArbKey(line):
    # Flutter wants Dart names (no spaces, camel case but we ignore)
    line = remove_chars(line, keep=ascii_letters + ' ')
    line = line.replace(" ", "_")
    return line.lower()

def convertPlaceholders(line):
    # Android requires positional markers when there are multiple arguments.
    # Convert %@/ %s-like tokens in occurrence order to %1$s, %2$s, ...
    placeholders = list(re.finditer(r"%@", line))
    if not placeholders:
        return line

    out = line
    offset = 0
    for idx, match in enumerate(placeholders, start=1):
        start, end = match.span()
        # Adjust for any growth due to previous replacements
        start += offset
        end += offset
        replacement = f"%{idx}$s"
        out = out[:start] + replacement + out[end:]
        offset += len(replacement) - (end - start)
    return out

def convertPlaceholdersToVue(line):
    params = [0, 1, 2]
    out = line
    for p in params:
        out = out.replace("%@", "{" + f"{p}" + "}", 1)
    out = out.replace("*", "") # No bold
    return out

def remove_chars(input_string, keep):
    return ''.join([_ for _ in input_string if _ in keep])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
