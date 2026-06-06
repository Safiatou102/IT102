#Print any IP gets a 404 status code

"""
The purpose of this script is to return 404 source IP if its found
"""


#librarires utilized
import re

def main():
    LOG_FILE = r"C:\Users\justincase\Desktop\IT.102\IT102\start\CH07\access.log"
    with open(LOG_FILE, "r") as f:
        for line in f:
            #Status code which is right after request and first numbers
            ip = line.split()[0]
            match = re.search(r'" 404', line)
            if match:
                print(f"{ip}")



if __name__ == "__main__":
    main()