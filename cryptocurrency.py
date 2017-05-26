#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# <bitbar.title>Cryptocurrency rates in USD</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Jorge Ovalle</bitbar.author>
# <bitbar.author.github>lojals</bitbar.author.github>
# <bitbar.desc>Displays Cryptocurrency rates in USD</bitbar.desc>
# <bitbar.image>https://cloud.githubusercontent.com/assets/6756995/26512378/e4c0aa40-422b-11e7-98e0-f68619cf892a.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/lojals/CryptoBar</bitbar.abouturl>
#
import urllib2
from json import JSONDecoder

try:
    request = urllib2.Request(url="https://cryptomate.co.uk/api/all/USD/")
    response = urllib2.urlopen(request).read()

    decoded_response = JSONDecoder().decode(response)
    
    currencies = ["BTC", "ETH", "LTC", "DOGE", "ETC", "DASH", "XMR"]
    
    for item in currencies :
        value = float(decoded_response[item]['price'])
        if value > 1 :
            print('1 %s : {}'.format("%.3f" % value) % item)
        else:
            print('1 %s : {}'.format("%.5f" % value) % item)

except Exception as e:
    print('{}'.format(e))
