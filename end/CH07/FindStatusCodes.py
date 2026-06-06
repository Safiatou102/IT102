#By Safiatou T
"""
This is for counting status codes
"""


#Libaries
import re
from collections import defaultdict


def main():
    LOG_FILE = r"C:\Users\justincase\Desktop\IT.102\IT102\end\CH07\access.log"
    counts = defaultdict(int)

    with open (LOG_FILE, "r") as f:
        for line in f:
            match = re.search(r'" (\d{3}) ', line)
            if match:
                counts[match.group(1)] += 1


    for code, count in sorted(counts.items()):
        print(f"{code}: {count}")   

if __name__ == "__main__":   
    main()         