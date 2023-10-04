#!/usr/bin/env python
import subprocess
import re

update = subprocess.run(["checkupdates"], stdout=subprocess.PIPE)
result = len(re.findall('\n', str(update.stdout, 'utf-8')))

if result >= 30:
    subprocess.run(["/usr/bin/notify-send","--icon=info", "Update Available" ,"-a","Update"])
else:
    print('not wank')



# TODO

# - We have our result, the number of packages
# - We need to check if the number is above 30
#   - If above 30, send a notfication otherwise do nuthin