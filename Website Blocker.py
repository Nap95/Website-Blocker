#

import time
from datetime import datetime as dt

hosts_path = r""                            # path where files go i.e. C\Windows\User\ etc...
redirect = ""                               # input local ip address in order to block site
website_list = [""]                         # put the list of websites you want to block i.e facebook.com, twitter.com
final_list = [redirect + " " + i for i in website_list]
final_string_block = "\n".join(final_list)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Within time...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(2.5)


