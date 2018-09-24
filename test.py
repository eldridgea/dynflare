import CloudFlare

def main():
    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print zone_id, zone_name

if __name__ == '__main__':
    main()
