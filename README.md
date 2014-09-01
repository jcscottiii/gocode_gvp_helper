## Purpose
Purpose of this script is to still easily use tools like GVP to switch your GO environment variables easily but with this script update your gocode lib-path accordingly. This way you can still get auto completion working as you switch around development envs.

This script will read your newly set GO environment variables and then call gocode setlib appropriately.

## Workflow:

1) Use gvp to set your local GO environment variables

$ source gvp in

2) Use this script to update your gocode.

$ gocode_gvp_helper

## Instructions:

1) chmod the file to execute permissions. (chmod 711)

2) Modify the script in the following:
  
- If you have any additional paths you wish to add, modify the "additional_paths variable.
- Modify the gocode_bin variable at the top to point to the absolute path to the gocode binary if it is not currently in your path.

Optional step but helpful

Add the gocode_gvp_helper to your $PATH

## TODOS:
Allow one to set and retain the gocode_bin path via command line instead of modifying the python script itself.
