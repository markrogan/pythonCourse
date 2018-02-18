import sys

myDict = {"key1": "val1", "key2": "val2"}

myDict["key3"] = "val3"

for key, value in myDict.items():
    print key, value

print sys.argv[0]
