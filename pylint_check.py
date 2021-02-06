#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.

import fnmatch
import os
import os.path
import re
import subprocess

import pylint as pylint
from pylint import epylint

includes = ['*.py', '*.odt']  # for files only
excludes = ['git']  # for dirs and files
print("DOING STUFF")
# transform glob patterns to regular expressions
# includes = r'|'.join([fnmatch.translate(x) for x in includes])
# excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

# for root, dirs, files in os.walk('.'):
#
#     exclude dirs
    # dirs[:] = [os.path.join(root, d) for d in dirs]
    # dirs[:] = [d for d in dirs if not re.match(excludes, d)]
    #
    # exclude/include files
    # files = [os.path.join(root, f) for f in files]
    # files = [f for f in files if not re.match(excludes, f)]
    # files = [f for f in files if re.match(includes, f)]
    #
    # for fname in files:
    #     print(fname)

print("\n\n\n")
print("DOING STUFF")
python_files= []
for root, dirs, files in os.walk('.', topdown=True):
    # excludes can be done with fnmatch.filter and complementary set,
    # but it's more annoying to read.
    dirs[:] = [d for d in dirs if
               d not in ['.git', '.idea', 'build', 'dist', 'venv38-pure', '__pycache__', 'mainmodulename.egg-info']]
    for pat in includes:
        for f in fnmatch.filter(files, pat):
            print(os.path.join(root, f))
            python_files.append(os.path.join(root, f))


msg = subprocess.run(['pylint', ' '.join(python_files)], capture_output=True)
# msg = subprocess.run(['pylint', 'pylint_check.py'], capture_output=True, check=False)
# {print(str_msg) for str_msg in (msg.stdout).strip().decode().splitlines()}

msg = epylint.py_run('src',return_std=True)
# print(msg[0].read())

print("DOING STUFF")


print("END.")