import requests
import json
from time import strftime, sleep
def main():
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/8c23a726-ad0b-47b7-a809-5a5d364ae09c'
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    req=requests.get(url,headers=head)
    str1=json.loads(req.text)
    print('-----------商品：'+str1['data']['name']+'-----------')#商品名
    print('规格：'+str(int(str1['data']['price'])/100))
    print("原价/折扣价："+str(int(str1['data']['market_price'])/100)+'/'+str(int(str1['data']['price'])/100))
    print("详细内容:"+str1['data']['share_content'])
    print('-----------"' + str1['data']['name'] + '"的价格波动-----------')
    try:
        while (True):
            EndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + str(int(str1['data']['price'])/100))
            print(EndPrint)
            sleep(4)
    except:

        print("程序结束")
if __name__ == '__main__':
    main()