import requests

def search(base_url = '', key = '', interface_url = {'search_key': '', 'page_deep': ''}, pageNum = 1, one_pageNum = 1, flag_printStep = 1):
    init_url = base_url + '?' + interface_url['search_key'] + '=' + key
    count = 0

    for i in range(pageNum):
        url = init_url + '&' + interface_url['page_deep'] + '=' + str(one_pageNum*i)
        html = getHTMLText(url)
        if html[1] != 200:
            continue
        if flag_printStep == 1:
            count = count + 1
            print('\r{:.2f}%'.format(count*100/pageNum), end = '...')
    return html

def getHTMLText(url = ''):
    get_timeout = 20

    try:
        r = requests.get(url, timeout = get_timeout)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return [r.text, r.status_code]
    except:
        return [r.url, r.status_code, r.reason]
