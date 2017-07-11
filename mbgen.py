from importlib import import_module
from utilities import *
import argparse
import os
import time

parser = argparse.ArgumentParser(description="Moodle Block Generator")
parser.add_argument("-m", "--modules", type=str, default="skeleton", help="Module list")
parser.add_argument("-v", "--verbose", type=bool, default=False, help="Verbose output mode")
parser.add_argument("-d", "--destination", type=str, help="Destination path", required=True)
parser.add_argument("-n", "--block-name", type=str, help="Block name", required=True)
parser.add_argument("-s", "--block-name-short", type=str, help="Block name (short)", required=True)
args = parser.parse_args()

destination_path = os.path.abspath(os.path.join(args.destination, args.block_name_short))
if os.path.exists(destination_path):
    raise Exception("Destination path already exists")


def verbose(message):
    if args.verbose:
        print(message)


def walk(path, result):
    for root, subdirs, files in os.walk(path):
        for file in files:
            fn = os.path.abspath(os.path.join(path, file))
            if os.path.exists(fn):
                result.append(fn)
        for sd in subdirs:
            walk(os.path.abspath(os.path.join(path, sd)), result)

var_dispatcher = VarDispatcher()
var_dispatcher\
    .set("BLOCKNAME_SHORT", args.block_name_short)\
    .set("BLOCKNAME", args.block_name)\
    .set("YYYY", time.strftime("%Y"))\
    .set("MM", time.strftime("%M"))\
    .set("DD", time.strftime("%d"))

file_dispatcher = FileDispatcher(var_dispatcher)

for modname in args.modules.split(','):
    ext = import_module("assets.%s.api" % modname)
    files = []
    walk("./assets/%s/root/" % modname, files)
    file_dispatcher.add(files)
    o_api = ext.Api(file_dispatcher, var_dispatcher)

verbose("Variable list: %s" % str(var_dispatcher))
verbose("File list: %s" % str(file_dispatcher))

os.makedirs(destination_path)
file_dispatcher.cp(destination_path)
files = []
walk(destination_path, files)
var_dispatcher.exec(files)
