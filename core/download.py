import requests, json
from .logging import log

def download_proxies() -> bool:
    paths = [
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://www.proxy-list.download/api/v1/get?type=http',
        'https://www.proxy-list.download/api/v1/get?type=https',
        'https://proxylist.geonode.com/api/proxy-list'
    ]
    proxies = []
    for path in paths:
        log(f'Downloading proxies from {path.split("/")[2]}...', end='\r')
        response = requests.get(path)
        if response.status_code == 200:
            proxies += response.text.split('\r\n')
            log(f'Downloaded proxies from {path.split("/")[2]}                   ', level='success')
        # Check if it is the proxylist.geonode.com API (JSON)
        if path == paths[-1]:
            for proxy in json.loads(response.text)['data']:
                proxies.append(f"{proxy['ip']}:{proxy['port']}")
    
    if proxies:
        unique_proxies = []
        for proxy in proxies:
            if len(proxy) > 21:
                # Invalid proxy (longer than 255.255.255.255:65535)
                continue
            if proxy not in unique_proxies:
                unique_proxies.append(proxy)
        with open('proxies.txt', 'w', encoding='utf-8') as file:
            for proxy in unique_proxies:
                file.write(proxy + '\n')
    return True