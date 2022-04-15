def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    fromDict = {}

    for line in handle:
        line = line.strip()
        if line.startswith("From "):
            sender = line.split()[1]
            if sender not in fromDict:
                fromDict[sender] = 1
            else:
                fromDict[sender] += 1

    dictVals = fromDict.values()
    maxVal = max(dictVals)

    print(max(fromDict, key=fromDict.get), maxVal)
    


        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()
