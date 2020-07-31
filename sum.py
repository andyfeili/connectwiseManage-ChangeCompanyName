

my_dict = {}
currentCompanyName = ""

with open('myoutput.txt') as f:
   for line in f:
       #print(line)
       
       splitLineName = line.split('-', 1)[0].strip().lower()
       
       splitLineNumber = line.split(' ', 1)
       
       if(splitLineNumber[0] == "CPU:" or splitLineNumber[0] == "SSD:" or splitLineNumber[0] == "RAM:"):
           #print("")
           value = float(splitLineNumber[1].strip())
           
           if my_dict[currentCompanyName] == "empty":
               valuesDic = {}
               valuesDic[splitLineNumber[0]] = value
               my_dict[currentCompanyName] = valuesDic
           elif splitLineNumber[0] not in my_dict[currentCompanyName].keys():
           
               my_dict[currentCompanyName][splitLineNumber[0]] = value
               
               #tempDic = my_dict[currentCompanyName]
               #my_dict[currentCompanyName] = my_dict[currentCompanyName] + 1
           else:
               temp = my_dict[currentCompanyName][splitLineNumber[0]]
               my_dict[currentCompanyName][splitLineNumber[0]] = temp + value
       else:
           #print(splitLineName[0])
           #print("")
           currentCompanyName = splitLineName
           
           if splitLineName not in my_dict.keys():
               my_dict[splitLineName] = "empty"
           #else:
               #my_dict[splitLineName] = my_dict[splitLineName] + 1
               #print("do nothing")
           
       #print(splitLineNumber[0])
       
       
       
       if 'str' in line:
          break
          
          
#print(my_dict)

for key in my_dict:
    print(key)
    for innerkey in my_dict[key]:
        print(innerkey + " ", end = '')
        print(my_dict[key][innerkey])

