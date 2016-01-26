import os
import glob
import re

path = 'readmes/'

MARKDOWN_REGEX = r'\[!\[(?P<alttext>.*?)\]\s*\((?P<image>.*?)\)\]\s*\((?P<link>.*?)\)' #   alt-text, image, link 
HTML_REGEX = r'\<a href=\"(?P<link>.*?)\"\>\<img src=\"(?P<image>.*?)\".*\<\/a\>' #  link, image

for infile in glob.glob(os.path.join(path, '*.md')):
    print('Looking at ' + infile)
    readme_file = open(infile, 'r')
    text = readme_file.read()
    readme_file.close()
    service_file_name = 'services/' + os.path.splitext(os.path.split(infile)[1])[0] + '.txt'
    service_file = open(service_file_name, 'w')
    p = re.compile(MARKDOWN_REGEX)
    m = p.finditer(text)
    for match in m:
        print(match.group('link'), match.group('image'))
        service_file.write('url: ' + match.group('link'))
        service_file.write('\n')
        service_file.write('badge: ' + match.group('image'))
        service_file.write('\n')
    p = re.compile(HTML_REGEX)
    m = p.finditer(text)
    for match in m:
        print(match.group('link'), match.group('image'))
        service_file.write('url: ' + match.group('link'))
        service_file.write('\n')
        service_file.write('badge: ' + match.group('image'))
        service_file.write('\n')
    service_file.close()
    if os.path.getsize(service_file_name) == 0:
        os.remove(service_file_name)
