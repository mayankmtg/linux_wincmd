from optparse import OptionParser
import sys
from utils import HeaderChecks

parser = OptionParser()
parser.add_option("-n", "--name", dest="name", help="name of command")
parser.add_option("-d", "--desc", dest="desc", help="Description of the command")
parser.add_option("-e", "--example", dest="example", help="An example usage of the command")
parser.add_option("-t", "--head", dest ="head", help="Header of the file")

(options, args) = parser.parse_args()
HeaderChecks(options, args)
sys.exit(0)
if(options.name == None or options.desc == None):
    print ("error (missing arguments)\t:\t there are some missing arguments -- python create.py -h")
    sys.exit(0)

with open("README.md") as f:
    content_flag = False
    file_content = ""
    for line in f:
        if(line == "## Table of contents\n"):
            content_flag = True
        if(content_flag and line == "\n"):
            file_content += "[" + options.name.title() + "](#" + options.name.lower() + ")\n"
            content_flag = False
        file_content += line

with open("README.md", 'w') as f:
    f.write(file_content)

append_string = "### " + options.name.lower() + "\n"
append_string += options.desc + "\n"
if(options.example != None):
    append_string += "```\n" + options.example + "\n```\n"
append_string += "\n\n"

with open("README.md", 'a') as f:
    f.write(append_string)


header_name = None
if(options.head == None):
    header_name = "header.txt"
else:
    header_name = options.header

command_header = ""
with open(header_name) as f:
    for line in f:
        command_header += line
    command_header += options.desc + "\n\n\n"

with open("commands/" + options.name.lower() + ".bat", 'w') as f:
    f.write(command_header)
    f.write("@echo off\n")
print ("created command template")