def countMatches(lod, key, val):
    count = 0
    for part in lod:
        for keys, value in part.items():
            if keys:
                if keys == key and value == val:
                    count += 1
    return count


def valuesForKey(lod, key):
    result = []
    for part in lod:
        if key in part.keys():
            if part[key] in result:
                pass
            else:
                result.append(part[key])
    
    return result

def filterByKey(lod, key, val):
    result = []
    for part in lod:
        for keys, value in part.items():
            if keys == key and value == val:
                result.append(part)
    return result

def countByKey(lod, key):
    result = {}
    for part in lod:
        if key in part.keys():
            if part[key] in result.keys():
                result[part[key]] += 1
            else:
                result[part[key]] = 1
    return result


def topKForKey(lod, key, k):
    result = {}
    freq = countByKey(lod, key)
    for i in range(k):
        temp = 0
        max_key = None
        if freq:
            for keys, values in freq.items():
                if values > temp:
                    max_key = keys
                    temp = values
                elif values == temp:
                    if keys < max_key:
                        max_key = keys
                        temp = values
            freq.pop(max_key)
            result[max_key] = temp
    return result
