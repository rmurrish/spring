
### Run this script from the command line
### python update_static.py
### from within the folder containing /articles and /live (currently pages)
### files in /live will be overwritten, ready to be served
### generated for each .md file in /articles

import os, re, subprocess

#should clear out /live directory first. Else old content may appear.

for filename in os.listdir('articles'):
  if filename[-3:] == ".md":
    cmdString = "cat static/header.htm <(pandoc articles/" + filename + ") static/footer.htm > ../live/articles/" + filename[0:-2] + "htm"
    #print cmdString
    print "Generated " + filename[0:-2] + "htm"
    #os.system(cmdString)
    subprocess.call(['bash','-c',cmdString])

#should also check diff between /static and /live/static and overwrite
#doing manually for now
print "Finished. Remember to overwrite any changes to /static into /live/static manually for now. Or update update_static.py if you get tired of doing that."
