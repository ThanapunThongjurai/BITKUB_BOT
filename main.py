from bitkub import Bitkub
import time 
import datetime
import math
import json

# TODO __init__.py this way to accase var folder
#     root
#         main.py <-- this file
#         var <-- folder
#             > __init__.py //just create
#             > configUserInfo.py // crate
#                 API_KEY = 'UserKEYAPI'
#                 API_SECRET = 'UserSECERTKEYAPI'
import var.configUserInfo as apiUser

#TODO เทพยากรณ์
#TODO สั่งศื้อ


#!Connect BitKub 
API_KEY = apiUser.API_KEY
API_SECRET = apiUser.API_SECRET
bitkub = Bitkub(api_key=API_KEY, api_secret=API_SECRET)

#user to format json data
def json_formatted_str(open_order):
    json_object = open_order 
    return json.dumps(json_object, indent=2)
#!percenCalculater
def percentCalculater (price, percentWant):
    return (price/100 *percentWant)

#!get wallet 
#wallet = bitkub.wallet()
#print(wallet["result"]["BTC"])

#!get MyOrder Current
#myorder =  bitkub.my_open_orders(sym='THB_BTC')
#print (json_formatted_str(myorder))
#for i in range(len(myorder)):
#    print (myorder["result"][i]["side"])

#!buyorder
#byorder = bitkub.place_bid(sym='THB_BTC', amt=20, rat=1040000, typ='limit')



#!percenCalculater
for i in range (10):
    for j in range (10):
        print(str()+str("{:.2f}".format(i+(j*0.1)))+" "+str(1000000+percentCalculater(1000000,i+(j*0.1))))

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

    
        


 



