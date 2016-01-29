import os
import glob
import re

path = 'gemfiles/'

GEM_REGEX = r'gem \'(?P<name>.*?)\'(\,\s*\'(?P<version>.*?)\')?'

gems = {} 

for infile in glob.glob(os.path.join(path, '*')):
    #print('Looking at ' + infile)
    gemfile_file = open(infile, 'r')
    text = gemfile_file.read()
    gemfile_file.close()
    filename = os.path.splitext(os.path.split(infile)[1])[0]
    p = re.compile(GEM_REGEX)
    m = p.finditer(text)
    for match in m:
        name = match.group('name')
        if 'padrino' in name:
            print('Padrino ' + filename + ' (' + name + ')')
        if 'sinatra' in name:
            print('Sinatra ' + filename + ' (' + name + ')')
        #if 'rails' in name:
        #    print('Rails ' + filename + ' (' + name + ')')
        #print(match.group('name'), match.group('version'))
        if name in gems:
            gems[name] += 1
        else:
            gems[name] = 1
#print(gems)


