import json
from os.path import expanduser, exists
import requests
import shelve

def UpdateRecord(email, api_key, zone_id, subdomain_id, subdomain, zone, origin, proxy):
	"""Updates DNS record at Cloudflare sith supplied info. Record must already exist."""
	url = 'https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records/' + subdomain_id
	headers = {'X-Auth-Email': email, 'X-Auth-Key': api_key, 'Content-Type': 'application/json'}
	data = {"type":"A","name":subdomain,"content":origin, "proxied":proxy}
	data = json.dumps(data)
	response = requests.put(url, headers=headers, data=data)
	if response.status_code == 200:
		return 'Success'
	else:
		return 'Error'

def GetIp():
	"""Gets publically facing IP address."""
	return requests.get('https://api.ipify.org').content

def GetSubdomainId(email, api_key, zone_id, subdomain):
	"""Get Cloudflare's Subdomain ID with supplied subdomain."""
	headers = {'X-Auth-Email': email, 'X-Auth-Key': api_key, 'Content-Type': 'application/json'}
	response = requests.get('https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records', headers=headers)
	for item in response.json()['result']:
		if item['name'] == subdomain:
			return item['id']


def GetZoneId(email, api_key, zone):
	"""Get Cloudflare's zone ID for supplied zone name."""
	headers = {'X-Auth-Email': email, 'X-Auth-Key': api_key, 'Content-Type': 'application/json'}
	response = requests.get('https://api.cloudflare.com/client/v4/zones?name=' + zone, headers=headers)
	x = response.json()
	return x['result'][0]['id']

def ShelveVariables(config_location, email, api_key, zone, subdomain, zone_id, subdomain_id):
	"""Store variables on disk."""
	shelf = shelve.open(config_location)
	shelf['email'] = email
	shelf['api_key'] = api_key
	shelf['zone'] = zone
	shelf['subdomain'] = subdomain
	shelf['zone_id'] = zone_id
	shelf['subdomain_id'] = subdomain_id
	shelf.close()

def RetrieveVariables(config_location):
	"""Retrieve stored variables from disk."""
	shelf = shelve.open(config_location)
	email = shelf['email']
	api_key = shelf['api_key']
	zone = shelf['zone']
	subdomain = shelf['subdomain']
	zone_id = shelf['zone_id']
	subdomain_id = shelf['subdomain_id']
	vars = [email, api_key, zone, subdomain, zone_id, subdomain_id]
	shelf.close()
	return vars

def main():
	"""Gets info and stores it at first run, otherwise updates DNS record."""
	homedir = expanduser("~")
	config_location = (homedir + '/.dynflare')
	if exists(config_location + '.db'):
		email, api_key, zone, subdomain, zone_id, subdomain_id = RetrieveVariables(config_location)
		ip = GetIp()
		print UpdateRecord(email, api_key, zone_id, subdomain_id, subdomain, zone, ip, True)
	else:
		email = raw_input('What\'s your email: ')
		api_key = raw_input('API Key: ') 
		zone = raw_input('Which domain will you be using (e.g. "example.com"): ')
		subdomain = raw_input('Which subdomain should I update (e.g. "app.example.com"): ')
		zone_id = GetZoneId(email, api_key, zone)
		subdomain_id = GetSubdomainId(email, api_key, zone_id, subdomain)
		ShelveVariables(config_location, email, api_key, zone, subdomain, zone_id, subdomain_id)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()