import csv

def createDict(keys, values): # keys is a list, and  values is a list
    dict_info = {}
    for i in range(len(keys)):
        dict_info[keys[i]] = values[i]
    return dict_info

def parseField(field): # string
    new_one = None
    if "(" in field:
        i = field.index('(')
        j = field.index(')')
        new_one = field[i+1:j] if j-i != 1 else None
    return new_one

def cleanDict(theDict): # dictionary
    new_dict = {}
    new_dict['Title'] = theDict['Title']
    new_dict['Artist'] = theDict['Artist']
    if parseField(theDict['Nationality']) != None:
        new_dict['Nationality'] = parseField(theDict['Nationality'])
    if parseField(theDict['Gender']) != None:
        new_dict['Gender'] = parseField(theDict['Gender'])
    new_dict['Classification'] = theDict['Classification']
    new_dict['Department'] = theDict['Department']
    new_dict['OnView'] = True if theDict['OnView'] != "" else False
    new_dict['Active'] = True if parseField(theDict['EndDate']) == None else False
    if len(theDict['Date']) == 4 and theDict['Date'].isdigit():
       new_dict['Year'] = int(theDict['Date'])
       new_dict['Decade'] = new_dict['Year'] - new_dict['Year']%10
    return new_dict

def readFromCSV(filename): # filename
    list_1 = [] # list of dictionaries
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        keys = next(reader)
        for line in reader:
            dict_info = createDict(keys, line)
            dict_info = cleanDict(dict_info)
            list_1.append(dict_info)
    return list_1

def writeToCSV(keys, lod, filename): # kes(list), lod(list), filename
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        for dict in lod:
            alist = []
            for name in keys:
                if name in dict.keys():
                    alist.append(dict[name])
                else:
                    alist.append("")
            writer.writerow(alist)
    return None
