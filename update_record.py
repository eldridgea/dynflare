import json
import requests

'''data={"type":"A","name":"python-test2.naphos.com","content":"104.191.246.32","ttl":120,"priority":10,"proxied":True}
d2 = json.dumps(data)
r = requests.post('https://api.cloudflare.com/client/v4/zones/d7714fed427cd5f67d30142b046d91bf/dns_records', headers=headers, data=data)
r.status_code = 200'''

def CreateRecord(subdomain, zone, origin, proxy):
	return None

def UpdateRecord(subdomain, zone, origin, proxy):
	return None

def GetSubdomainId(email, api_key, zone_id, subdomain):
	headers = {'X-Auth-Email': email, 'X-Auth-Key': api_key, 'Content-Type': 'application/json'}
	response = requests.get('https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records', headers=headers)
	for item in response.json()['result']:
		if item['name'] == subdomain:
			return item['id']


def GetZoneId(email, api_key, zone):
	headers = {'X-Auth-Email': email, 'X-Auth-Key': api_key, 'Content-Type': 'application/json'}
	response = requests.get('https://api.cloudflare.com/client/v4/zones?name=' + zone, headers=headers)
	x = response.json()
	return x['result'][0]['id']

def main():
	email = raw_input('What\'s your email: ')
	api_key = raw_input('API Key: ') 
	zone = raw_input('Which zone (domain) will you be using: ')
	subdomain = raw_input('Which subdomain: ')
	zone_id = GetZoneId(email, api_key, zone)
	print GetSubdomainId(email, api_key, zone_id, subdomain)



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()