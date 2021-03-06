'''
HOW TO USE:
  This file extracts the option "value" attributes, and creates a hash if the option's text does not match the option's value

  Copy this file to a separate location (so as not to send random files
    to github)

  Create a folder named "input" in the same location

  Copy the section of the HTML containing the form options that you
    want to extract (does not have to be exact, you can even copy and paste
    the entire HTML source code if you want, only there is less chance for
    errors if you only copy/paste the section containing the form)

  Paste into a text file (NOT word) and save in the "input" folder.

  Run the .py file in python 3.3, and copy/paste the resulting output.

  It is recommended to check the output for any errors (if the attribute is
  in single quotes you can change this in the regular expression below to
  r'(?:<option.*?value\s*=\s*)(\'.*?\')'.
'''

import os
import re

YAMLselections = []

#compile regular expressions
#select = re.compile(r'<select.*?</select>', re.DOTALL | re.IGNORECASE)
selectoptions = re.compile(r'(?:<option.*?value\s*=\s*\")(.*?)(?:\")', re.IGNORECASE)
selecttext = re.compile(r'(?:<option.*?value.*?>)(.*?)(?:</)', re.IGNORECASE)

for root,dirs,files in os.walk('.\input'):
    for file in files:
        with open('.\input\\' + file, 'r') as f:
            html = f.read()
        #selectors = re.findall(select, html)
        #for selector in selectors:
        options = re.findall(selectoptions, html)
        text = re.findall(selecttext, html)
        data = '------------\n' + file + '\n' + 'options:' + '\n'
        if len(options) != len(text):
            print("\nerror with text, printing option values only")
            for option in options:
                data = data + "          "
                data = data + "- \"" + option + "\"\n"
            YAMLselections.append(data)
        elif set(options) != set(text):
            print("\noptions != text, printing hash")
            for i in range(0,len(options)):
                data = data + "          "
                data = data + "\"" + text[i] + "\":" + " \"" + options[i] + "\"\n"
            YAMLselections.append(data)
        else:
            for option in options:
                data = data + "          "
                data = data + "- \"" + option + "\"\n"
            YAMLselections.append(data)
            
for x in YAMLselections:
    print(x)
