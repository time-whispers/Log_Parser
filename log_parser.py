"""
1 : Reading the file
2 : Extract IP Address, Error and Success Logs
3 : Save The Output in CSV/Excel File
4: Send Email
"""

import re                               # Regular Expressions
import pandas as pd
import pprint                           # Pretty Print

logfile = open("serverlogs.log", "r")


pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

ip_addrs_lst = []
failed_lst = []
success_lst = []

for log in logfile:
    ip_add = re.search(pattern,log)
    ip_addrs_lst.append(ip_add.group())
    lst = log.split(" ")
    failed_lst.append(int(lst[-1]))
    success_lst.append(int(lst[-4]))

total_failed = sum(failed_lst)
total_success = sum(success_lst)

ip_addrs_lst.append("Total")
success_lst.append(total_success)
failed_lst.append(total_failed)

df = pd.DataFrame(columns=['IP Address',"Success","Failed"])
df['IP Address'] = ip_addrs_lst
df["Success"] = success_lst
df["Failed"] = failed_lst

df.to_csv("output.csv", index= False)

pprint.pprint(df)