from pyperclip import copy
from bs4 import BeautifulSoup

print('输入`quit`以退出。')

while (raw := input('请输入`<table>…</table>` >> ')) != 'quit':
    soup = BeautifulSoup(raw, features='html.parser')

    table = soup.find('table')
    del table['cellspacing']
    del table['cellpadding']
    del table['border']

    for tag in soup.find_all(lambda t: 'id' in t.attrs):
        del tag['id']

    for data in soup.find_all('td'):
        del data['width']
        del data['valign']

        if (h4 := data.find('h4')) is not None:
            data.string = h4.text

    copy(str(soup))
    print('已复制到剪贴板。')
