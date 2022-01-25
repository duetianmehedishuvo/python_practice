import sys

randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("next entry")
        print()
print("The reciprocal of", entry, "is", r)

# 2nd way Practice


randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("next entry")
        print()
print("The reciprocal of", entry, "is", r)
