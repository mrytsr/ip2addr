#!/usr/bin/env python2
import maxminddb
import sys
import os
reader = maxminddb.open_database(os.path.dirname(sys.argv[0]) + '/GeoLite2-City.mmdb')
arr = []
ip = sys.argv[1]
try:
    arr = reader.get(ip)
except:
    pass
country = '-'
city = '-'
try:
    if 'country' in arr:
        if 'zh-CN' in arr['country']['names']:
            country = arr['country']['names']['zh-CN']
        else:
            country = arr['country']['names']['en']
    if 'city' in arr:
        if 'zh-CN' in arr['city']['names']:
            city = arr['city']['names']['zh-CN']
        else:
            city = arr['city']['names']['en']
except:
    print arr
print ip + ': ' + country + ' ' + city
reader.close()
