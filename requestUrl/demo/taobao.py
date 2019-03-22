import requests
import re
import pandas
import numpy

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'getHTMLText Error'

def parsePage(html):
    itemList = []

    try:
        titleList = re.findall(r'\"raw_title\"\:\".*?\"', html)
        priceList = re.findall(r'\"view_price\"\:\"[\d\.]*?\"', html)
        for i in range(len(priceList)):
            price = eval(priceList[i].split(':')[1])
            title = eval(titleList[i].split(':')[1])
            itemList.append([title, price])
        return itemList
    except:
        return 'parsePage Error'

def saveGoodsList_xlsx(itemList, titleList, xlsxName, sheet_range):
    titleNum = len(titleList)
    rowData_num = len(itemList)
    colData = []
    table = {}

    for i in range(titleNum):
        colData.append([])
        for j in range(rowData_num):
            colData[i].append(itemList[j][i])
    colData = numpy.transpose(itemList)
    for i in range(titleNum):
        table[titleList[i]] = colData[i]
    dataFrame = pandas.DataFrame(table)
    with pandas.ExcelWriter(xlsxName, engine = 'xlsxwriter') as wirter:
        dataFrame.to_excel(wirter, sheet_name=sheet_range)
        wirter.save()

def main():
    goods = '书包'
    titles = ['商品名称', '商品价格']
    pageNum = 20
    infoList = []
    count = 0
    base_url = 'https://s.taobao.com/search?q=' + goods

    for i in range(pageNum):
        url = base_url + '&s=' + str(44*i)
        html = getHTMLText(url)
        if html == 'getHTMLText Error':
            continue
        infoList.extend(parsePage(html))
        if infoList == 'getHTMLText Error':
            continue
        count = count + 1
        print('\r{:.2f}%'.format(count*100/pageNum), end = '...')
    saveGoodsList_xlsx(infoList, titles, 'taobao.xlsx', goods)

main()
