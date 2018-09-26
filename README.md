# dynflare
Cloudflare DNS record updater tool for dynamic DNS servers

This is a small Python tool to autoamtically update your Cloudflare DNS record for a subdomain with your current IP address every minute.
Great for home networks with dynamic IP addresses.

This is in beta and not reecommended for production usage. 

## Known Issues
* Only works with subdomains with single A records presently.
* Currently errors out if a record for that subdomain does nort already exist.
