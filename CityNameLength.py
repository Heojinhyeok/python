citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

length = [len(city) for city in citys]
longestname = max(length)
shortestname = min(length)
#print(longestname, shortestname)

longestname1 = []
shortestname1 = []
for city in citys:
    if len(city) == 8:
        longestname1.append(city)
    elif len(city) == 5:
        shortestname1.append(city)
print("Long name city : ", ' '.join(longestname1))
print("Short name city : ", ', '.join(shortestname1))
