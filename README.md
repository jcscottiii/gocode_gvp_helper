Purpose of this script is to still easily use tools like GVP to switch your GO environment variables easily but with this script update your gocode lib-path accordingly. This way you can still get auto completion working as you switch around development envs.

This script will read your newly set GO environment variables and then call gocode setlib appropriately.

Workflow:

1) Use gvp to set your local GO environment variables

$ source gvp in

2) Use this script to update your gocode.

$ gocode_gvp_helper

Instructions:

1) chmod the file to execute permissions. (chmod 711)

2) Modify the script in the following:
  
  a) If you have any additional paths you wish to add, modify the "additional_paths variable.

Optional step but helpful

Add the gocode_gvp_helper to your $PATH
