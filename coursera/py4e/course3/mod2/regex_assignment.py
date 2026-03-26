# regex_assignment.py

import re

# file = open('regex_sum_2152089.txt','r')
# content = file.read()
# nums = re.findall(r'[0-9]+',content)
# print(sum([int(num) for num in nums]))

print(
    sum(
        [
            int(n)
            for n in re.findall("[0-9]+", open("regex_sum_2152089.txt", "r").read())
        ]
    )
)
