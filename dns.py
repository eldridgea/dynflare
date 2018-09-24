#!/usr/bin/env python

import sys
import CloudFlare

def main():
    zone_name = 'eldrid.ge'
    cf = CloudFlare.CloudFlare()
    zone_info = cf.zones.post(data={'jump_start':False, 'name': zone_name})
    zone_id = zone_info['id']

    dns_records = [
        {'name':'python-really.eldrid.ge', 'type':'AAAA', 'content':'2001:d8b::1'},
    ]

    for dns_record in dns_records:
        r = cf.zones.dns_records.post(zone_id, data=dns_record)
    exit(0)

if __name__ == '__main__':
    main()
