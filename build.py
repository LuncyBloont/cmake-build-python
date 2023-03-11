
import os
import sys
import re

root = os.path.dirname(sys.argv[0])

print(root)

subList = os.listdir(root)
dirList = []
nameList = []

normalCheck = re.compile('^[^.].*$')
sourceCheck = re.compile('.*\\.(cpp|h)')

for e in subList:
    if os.path.isdir(os.path.join(root, e)) and normalCheck.match(e):
        dirList.append(os.path.join(root, e))
        nameList.append(e)

for i, proj in enumerate(dirList):
    print('configure project: {} [at {}]'.format(nameList[i], proj))
    with open(os.path.join(proj, 'CMakeLists.txt'), 'w') as fw:
        fw.write('CMAKE_MINIMUM_REQUIRED(VERSION 3.10)\n')
        fw.write('PROJECT({})\n'.format(nameList[i]))

        _tmp = os.listdir(proj)
        source = []
        for file in _tmp:
            if sourceCheck.match(file):
                source.append(file)

        print('source file: ' + str(source))

        fw.write('add_executable({} {})'.format(nameList[i], ' '.join(source)))
    if not os.path.exists(os.path.join(proj, 'build')):
        os.mkdir(os.path.join(proj, 'build'))
    os.chdir(os.path.join(proj, 'build'))
    os.system('cmake ..')
    os.system('cmake --build .')

