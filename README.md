# dynflare
Cloudflare DNS record updater tool for dynamic DNS servers

This is a small Python script that automatically updates Cloudflare DNS records.
This is good for servers that are on home ISPs or other connections with a dynamic IP address.

## Known Issues
* This currently only deals with a subdomain with one A record.
* The script will break if the subdomain doesn't already have an A record.
* This script will always enable Cloudflare proxying.
