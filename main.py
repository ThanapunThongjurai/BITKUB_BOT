from bitkub import Bitkub
import time
import datetime
import math
import json
from array import *
# TODO __init__.py this way to accase var folder
#     root
#         main.py <-- this file
#         var <-- folder
#             > __init__.py //just create
#             > configUserInfo.py // crate
#                 API_KEY = 'UserKEYAPI'
#                 API_SECRET = 'UserSECERTKEYAPI'
import var.configUserInfo as apiUser

#!Connect BitKub
API_KEY = apiUser.API_KEY
API_SECRET = apiUser.API_SECRET
bitkub = Bitkub(api_key=API_KEY, api_secret=API_SECRET)

#!
coinType = "THB_DOGE"


# TODO GET STATUS
# TODO เทพยากรณ์
# TODO สั่งศื้อ


# user to format json data
def json_formatted_str(open_order):
    json_object = open_order
    return json.dumps(json_object, indent=2)



#!percenCalculater
def percentCalculater(price, percentWant):
    return float(price/100 * percentWant)

#!!! vargobal
basePrice = 1000000
bathGet = 10000
fee = 0.25

#!get wallet
# wallet = bitkub.wallet()
# print(wallet["result"]["BTC"])

#!get MyOrder Current
# myorder =  bitkub.my_open_orders(sym='THB_BTC')
# print (json_formatted_str(myorder))
# for i in range(len(myorder)):
#    print (myorder["result"][i]["side"])

#!buyorder
# byorder = bitkub.place_bid(sym='THB_BTC', amt=20, rat=1040000, typ='limit')


#!price
# n = 10
# allprice = [[0] * n for i in range(n)]

# for i in range(n):
#     display=str(i)+'%  '
#     for j in range(n):
#         #print(str()+str("{:.2f}".format(i+(j*0.1)))+" " +str(1030000+percentCalculater(1030000, i+(j*0.1))))
#         allprice[i][j] = basePrice+percentCalculater(basePrice, i+(j*0.1))
#         display= display + (str(allprice[i][j])+'['+str("{:.1f}".format(i+(j*0.1)))+']'+", ")
#     print(display)



#TODO Main(){}
# i = 0
# while i == 0:
#     myorder =  bitkub.my_open_orders(sym='THB_BTC')
#     statusOfOrder = []

#     if myorder["error"] == 0 :
#         print(len(myorder["result"]))
#         for i in range(len(myorder["result"])):
#             statusOfOrder.append(myorder["result"][i]["side"])
#             print (statusOfOrder[i])

#     i = i+ 1
#     statusOfOrder.clear()

#basecoase of display
# for row in allprice:
#       print('   '.join([str(elem) for elem in row]))
#       print(str(i)+'%  '+'   '.join([str(elem)+'['+str(j*0.1)+']' for elem in allprice[i]]))

#!GetPriceFormBitkub


print(bitkub.ticker(sym=coinType)[coinType]["last"])
CurrentPrice = bitkub.ticker(sym=coinType)
#print (CurrentPrice[coinType]["last"])
basePrice = CurrentPrice[coinType]["last"];

print(bitkub.ticker(sym='THB_DOGE')["THB_DOGE"]["last"])
print(basePrice+percentCalculater(basePrice, 1.5))

#!!!MAIN 
print("-----START-----")
n = 10
allprice = [[0] * n for i in range(n)]

for i in range(n):
    display=""#str(i)+'%  '
    for j in range(n):
        #print(str()+str("{:.2f}".format(i+(j*0.1)))+" " +str(1030000+percentCalculater(1030000, i+(j*0.1))))
        allprice[i][j] = basePrice+percentCalculater(basePrice, i+(j*0.1))
        display= display + (str("{:.1f}".format(allprice[i][j]))+'['+str("{:.1f}".format(i+(j*0.1)))+']'+", ")
    print(display)

bathAllPrice = [[0] * n for i in range(n)]
for i in range(n):
    display=""#str(i)+'%  '
    for j in range(n):
        #print(str()+str("{:.2f}".format(i+(j*0.1)))+" " +str(1030000+percentCalculater(1030000, i+(j*0.1))))
        bathAllPrice[i][j] = bathGet+percentCalculater(bathGet, i+(j*0.1))
        display= display + (str("{:.1f}".format(bathAllPrice[i][j]))+'['+str("{:.1f}".format(i+(j*0.1)))+']'+", ")
    print(display)
print ("ราคาตอนนี้ : "+str(basePrice))
print ("ขายตอน 1% BTC "+str(allprice[1][0]+percentCalculater(allprice[1][0],0.5)))
print ("ขายตอน 1% BATH "+str(bathAllPrice[1][0]-percentCalculater(bathAllPrice[1][0],0.5)))