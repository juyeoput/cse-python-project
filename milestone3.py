import milestone1
import milestone2
import matplotlib.pyplot as plt

data = milestone2.readFromCSV('full.csv')

def barByDecade(data, mustBeOnView):
    new_dict = {}
    x = []
    y = []
    if mustBeOnView:
        lod = milestone1.filterByKey(data, 'OnView', True)
        title = 'Artworks on Display by Decade'
    else:
        lod = data
        title = 'Artworks in Collection by Decade'

    dict = milestone1.countByKey(lod, 'Year')

    for key in dict.keys():
        new_key = str(int(key) - (int(key)%10))
        if new_key in new_dict.keys():
            new_dict[new_key] += dict[key]
        else:
            new_dict[new_key] = dict[key]
    for k in new_dict.keys():
        x.append(int(k))
        y.append(new_dict[k])     
    plt.bar(x, y, width = 8)
    plt.xlabel('Decade')
    plt.ylabel('# of Artworks')
    plt.title(title)
    plt.show()


def filteredBarByCategory(data, category, key, value, mustBeOnView):
    lod = milestone1.filterByKey(data, key, value)
    if mustBeOnView == True:
        lod = milestone1.filterByKey(lod, 'OnView', True)
        title = f'Artworks on Display by {category} for {key} {value}'
    else:
        title = f'Artworks in Collection by {category} for {key} {value}'
    dict = milestone1.countByKey(lod, category) 
    x = list(dict.keys())
    y = list(dict.values())
    plt.barh(x, y)
    plt.title(title)
    plt.xlabel('# of Artworks')
    plt.ylabel(category)
    plt.show()
        

def pieByCategory(data, category, mustBeOnView):
    if mustBeOnView == True:
        lod = milestone1.filterByKey(data, 'OnView', True)
        title = f'Artworks on Display by {category}'
    else:
        lod = data
        title = f'Artworks in Collection by {category}'
    dict = milestone1.countByKey(lod, category)
    plt.pie(list(dict.values()), labels= list(dict.keys()))
    plt.title(title)
    plt.show()


def pieByCategoryTopK(data, category, k ,mustBeOnView):
    if mustBeOnView == True:
        lod = milestone1.filterByKey(data, 'OnView', True)
        title = f'Artworks on Display, Top {k} Most Frequent {category}'
    else:
        lod = data
        title = f'Artworks in Collection, Top {k} Most Frequent {category}'
    dict = milestone1.topKForKey(lod, category, k)
    others = len(lod)-sum(list(dict.values()))
    final_keys = list(dict.keys())
    final_keys.append('other')
    final_values = list(dict.values())
    final_values.append(others)
    plt.pie(final_values, labels = final_keys)
    plt.title(title)
    plt.show()
