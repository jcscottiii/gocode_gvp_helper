#!/usr/bin/python

# Modify this section.
gocode_bin = ""
additional_paths = [
  # where you can put additional strings to like the goroot of the appengine SDK
]
# Typical user should not have to modify anything below.

import os
import sys
import platform
import subprocess


###
### Form string for OS_ARCH folder.
###

# Determine OS type.
os_env_var = platform.system().lower()
os_string = ""
if "linux" in os_env_var:
  os_string = "linux"
elif "darwin" in os_env_var:
  os_string = "darwin"
else:
  print "Unsupported OS, found environment variable = ", os_env_var
  sys.exit(1)

# Determine Architecture.
host_env_var = platform.machine().lower()
if "x86_64" in host_env_var:
  arch_string = "amd64"
elif "x86" in host_env_var:
  arch_string = "i386"
else:
  print "Unsupported ARCH, found environment variable = ", host_env_var
  sys.exit(1)

lib_folder = os_string + "_" + arch_string
print lib_folder
gopath_env_var = os.environ["GOPATH"]
gopaths = gopath_env_var.split(":")
gopaths = additional_paths + gopaths
folders = ""
for gopath in gopaths:
  folder = gopath
  # If the pkg folder isnt in the path, add it.
  if lib_folder not in folder:
    folder = os.path.join(gopath, "pkg", lib_folder)
  if os.path.isdir(folder):
    if folders == "":
      folders = folder
    else:
      folders = folders + ":" + folder
  else:
    print "Warning could not find %s. Not adding it", folder
###
### Check for gocode bin.
###
if gocode_bin == "":
  # Gocode must be in path if not specified.
  gocode_bin = "gocode"
try:
  subprocess.call([gocode_bin, "close"])
  subprocess.call([gocode_bin, "set", "lib-path", folders])
  print "Added the following path to gocode: ", folders
except OSError as error:
  if error.errno == os.errno.ENOENT:
    print "Can't find gocode bin", gocode_bin
  else:
    print "Unknown error"
  sys.exit(1)
