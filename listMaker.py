# Used this script for making list of urls

import os
i = 0
a = '['
with open('links.txt') as f:
    for line in list(f.readlines())[100:300]:
        s = "'{}',".format(line.strip())
        a += s
a += ']'
print(a)
