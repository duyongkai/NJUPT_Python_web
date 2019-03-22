import numpy
import pandas

def saveItem_xlsx(itemList = [], itemTitle = [], fileName = '', sheetName = ''):
    table  = {}
    dataList = []

    for i in range(len(itemTitle)):
        dataList.append([])
        for j in range(len(itemList)):
            dataList[i].append(itemList[j][i])

    for i in range(len(itemTitle)):
        table[itemTitle[i]] = dataList[i]
    tableFrame = pandas.DataFrame(table)
    with pandas.ExcelWriter(fileName + '.xlsx', engine = 'xlsxwriter') as xlsx_writer:
        tableFrame.to_excel(xlsx_writer, sheet_name = sheetName)
        xlsx_writer.save()
