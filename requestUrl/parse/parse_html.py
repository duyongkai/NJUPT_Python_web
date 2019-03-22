import bs4
import re

def parseGet_itemList_bsReStr(html = ''):
    itemList = []

    soup = bs4.BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            itemList.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue
    return itemList

def parseGet_itemList_reDict(html = ''):
    itemList = []

    dictList1 = re.findall(r'\"raw_title\"\:\".*?\"', html)
    dictList2 = re.findall(r'\"view_price\"\:\"[\d\.]*?\"', html)
    for i in range(len(dictList1)):
        dict1_value = eval(dictList1[i].split(':')[1])
        dict2_value = eval(dictList2[i].split(':')[1])
        itemList.append([dict1_value, dict2_value])
    return itemList
