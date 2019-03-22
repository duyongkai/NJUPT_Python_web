import sys
import bs4
import re

def import_modules(dir = r'E:\Users\dyk\Source\Libs\Python', file = '__init__.py'):
    try:
        if not dir in sys.path:
            sys.path.append(dir)
        if not file in sys.modules:
            module = __import__(file)
        else:
            eval('import ' + file)
            module = eval('reload(' + file + ')')
        return module
    except:
        return ModuleNotFoundError

def saveFinish_cmd():
    print('<successful!>')
    input('press any key to continue...')

# def parseGet_itemList_bsReStr(html = ''):
#     itemList = []

#     soup = bs4.BeautifulSoup(html, 'html.parser')
#     div_list = soup.find_all('div')
#     for div in div_list:
#         try:
#             divId = div.attrs['id']
#             if divId == 'container_content':
#                 for child in div.contents:
#                     if child.name == 'div':
#                         if child.frag == '窗口4':
#                             aimHTML_area = child.contents[0].contents
#             for tr in aimHTML_area[1:]:
#                 item = []
#                 td_list = tr.contents
#                 item.append(td_list[1].contents[0].string)
#                 item.append(td_list[0].contents[0].string)
#                 item.append(td_list[0].contents[0].attrs['href'])
#                 itemList.append(item)
#         except:
#             continue
#     return itemList

def parseGet_itemList_bsReStr(html = ''):
    itemList = []

    soup = bs4.BeautifulSoup(html, 'html.parser')
    tr_list = soup.contents[0].contents[3].contents[3].contents[3].contents[5].contents[1].contents[7].contents[7].contents[1].contents[1].contents[0].contents[1].contents[1].contents
    for tr in tr_list:
        try:
            td_title = tr.contents[3].contents[1].contents[1].contents[1].contents[0]
            td_date = tr.contents[3].contents[1].contents[1].contents[3].contents[0]
            itemList.append([td_date.string, td_title.string, 'http://jwc.njupt.edu.cn'+td_title.attrs['href']])
        except:
            continue
    return itemList

def main():
    page_deep = 201
    count = 0
    base_url = 'http://jwc.njupt.edu.cn/1594/list'
    itemTitle = ['公告日期', '公告标题', '公告内容链接']
    itemList = []

    get_source = import_modules(r'E:\Users\dyk\Source\Libs\Python\crawler', 'get_source')
    save = import_modules(r'E:\Users\dyk\Source\Libs\Python\file', 'save')

    for page in range(page_deep):
        url = base_url + str(page+1) + '.htm'
        html = get_source.getHTMLText(url)[0]
        itemList.extend(parseGet_itemList_bsReStr(html))
        count = count + 1
        print('\r{:.2f}%'.format(count*100/page_deep), end = '...')

    save.saveItem_xlsx(itemList, itemTitle, 'jwc', 'inform')
    # saveFinish_cmd()

main()
