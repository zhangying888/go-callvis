import collections
import subprocess
import json

'''
Usage:

  go-callvis [flags] package

  Package should be main package, otherwise -tests flag must be used.

Flags:

  -debug
        Enable verbose log.
  -file string
        output filename - omit to use server mode
  -focus string
        Focus specific package using name or import path. (default "main")
  -format string
        output file format [svg | png | jpg | ...] (default "svg")
  -group string
        Grouping functions by packages and/or types [pkg, type] (separated by comma)
  -http string
        HTTP service address. (default ":7878")
  -ignore string
        Ignore package paths containing given prefixes (separated by comma)
  -include string
        Include package paths with given prefixes (separated by comma)
  -limit string
        Limit package paths to given prefixes (separated by comma)
  -minlen uint
        Minimum edge length (for wider output). (default 2)
  -nodesep float
        Minimum space between two adjacent nodes in the same rank (for taller output). (default 0.35)
  -nointer
        Omit calls to unexported functions.
  -nostd
        Omit calls to/from packages in standard library.
  -skipbrowser
        Skip opening browser.
  -tags build tags
        a list of build tags to consider satisfied during the build. For more information about build tags, see the description of build constraints in the documentation for the go/build package
  -tests
        Include test code.
  -version
        Show version and exit.
'''

defaultArgs = {
    "debug": True,
    "file": 'defaultOutPut',
    "focus": 'main',
    "format": 'svg',
    "group": 'type',
    "ignore": [],
    "include": [],
    "limit": [],
    "minlen": 2,
    #     "nodesep": 0.1,
    "nointer": False,
    "nostd": True,
    "skipbrowser": True
}

# config
ignore = [
    ''
]
mainPackage = "github.com/zhangying888/go-callvis"


def getParameters(o):
    params = []
    for k in o:
        if isinstance(o[k], bool):
            if o[k]:
                params.append('-' + k)
        elif isinstance(o[k], list):
            if len(o[k]) > 0:
                params.append('-' + k)
                params.append("'{}'".format(','.join(o[k])))
        else:
            params.append('-' + k)
            params.append(str(o[k]))
    return params


def setOutputName(name):
    defaultArgs['file'] = name


def callGraphVis():
    workingDir = '/tmp'
    print(' '.join(['go-callvis', *getParameters(defaultArgs), mainPackage]))
    p = subprocess.Popen(
        ['go-callvis', *getParameters(defaultArgs), mainPackage], cwd=workingDir)
    retval = p.wait()
#     lines = p.stdout.readlines()
#     print(lines)
#     lines = [item.decode('utf-8') for item in lines]
#     with open('/home/zy/demo/demoCalloutput', 'w+') as f:
#         f.writelines(lines)
