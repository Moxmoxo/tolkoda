from bs4 import BeautifulSoup
import requests
import json

url = requests.get('https://shop.mts.by/phones/huawei/huawei-nova-y61-6-64gb-s-nfc-black/').text

with open('html_file/fone.html', 'r', encoding='UTF-8') as f:
    file = f.read()
    key_info = []
    count_info =[]
    soup = BeautifulSoup(url, 'lxml')

    info_all = soup.find_all('td')
    for item in range(len(info_all)):
        if item %2 == 1:
            print(info_all[item].text.strip())
            count_info.append(info_all[item].text.strip())
            print('-----------*_*------------')
        elif item %2 == 0:
            print(info_all[item].text.strip())
            key_info.append(info_all[item].text.strip())
        # print(item.text.strip())


print(key_info)
print(count_info)
print(len(key_info))
print(len(count_info))

data = []
for i in range(len(key_info)):
    data_set = {
        f'{key_info[i]}': f'{count_info[i]}'
    }
    data.append(data_set)

with open('fone.json', 'w', encoding='UTF-8')as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
