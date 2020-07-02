#!/bin/bash
#!/usr/bin/env python

cd "$(dirname "$0")"
python3 passwd-parser.py -p ${1:- /etc/passwd} -g ${2:- /etc/group} >> output.log 2>&1 
