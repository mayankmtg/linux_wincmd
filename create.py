import sys
from utils import HeaderChecks

(options, args) = HeaderChecks().parse()

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
            file_content += "[" + options.name.title() + "](#" + options.name.lower() + ")<br>\n"
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
print ("-- \t created command template \t --")