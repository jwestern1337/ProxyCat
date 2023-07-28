import argparse
import socket
import threading
import time
from typing import List

from core.utils import construct_http_request, parse_http_response
from core.download import download_proxies
from core.logging import log

BUFFER_SIZE = 4096

class ProxyChecker:
    def __init__(self, filename: str, timeout: float, retries: int) -> None:
        self.filename = filename
        self.timeout = timeout
        self.retries = retries
        self.good_proxies: List[str] = []

    def read_proxies_from_file(self) -> List[str]:
        """
        Read proxies from the file and return a list of proxies.

        Returns:
            List[str]: List of proxies in the format 'ip:port'.
        """
        proxies = []
        with open(self.filename, 'r') as file:
            for line in file:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
        return proxies

    def check_proxy(self, proxy: str) -> None:
        """
        Check the given proxy for connectivity and response validity.

        Params:
            proxy (str): The proxy to be checked in the format 'ip:port'.
        """
        try:
            ip, port = proxy.split(':')
            for _ in range(self.retries):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(self.timeout)
                    sock.connect((ip, int(port)))
                    request = construct_http_request(
                        'GET',
                        f'http://{ip}:{port}',
                        {
                            'Host': 'www.google.com',
                            'Connection': 'close',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                            'Accept': '*/*'
                        },
                        b''
                    )
                    sock.send(request)
                    response = sock.recv(BUFFER_SIZE)
                    if response:
                        status_code, body, headers = parse_http_response(response)
                        if status_code != 0:
                            log(f'Good proxy: {proxy} ({status_code})', 'success')
                            with threading.Lock():
                                self.good_proxies.append(proxy)
                            break
                        else:
                            log(f'Bad proxy: {proxy}', 'error')
                    else:
                        log(f'Bad proxy: {proxy}', 'error')
        except:
            pass

    def check_all_proxies(self) -> None:
        """
        Check all proxies read from the file in a multithreaded manner.
        """
        proxies = self.read_proxies_from_file()
        threads = []
        for proxy in proxies:
            thread = threading.Thread(target=self.check_proxy, args=(proxy,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def write_proxies_to_file(self, filename: str) -> None:
        """
        Write the good proxies to a file.

        Params:
            filename (str): The name of the file to write the good proxies to.
        """
        self.good_proxies.sort()
        with open(filename, 'w') as file:
            for proxy in self.good_proxies:
                file.write(proxy + '\n')

def main():
    print('''
 ____  ____   __  _  _  _  _     ___   __  ____ 
(  _ \(  _ \ /  \( \/ )( \/ )   / __) / _\(_  _)
 ) __/ )   /(  O ))  (  )  /   ( (__ /    \ )(    v1.0.0
(__)  (__\_) \__/(_/\_)(__/     \___)\_/\_/(__) 
''')
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Text file containing proxies (ip:port) on each line")
    parser.add_argument("timeout", type=float, help="Timeout duration in seconds")
    parser.add_argument("retries", type=int, help="Number of times to retry a proxy")
    download_proxies()
    args = parser.parse_args()

    proxy_checker = ProxyChecker(args.filename, args.timeout, args.retries)
    proxy_checker.check_all_proxies()
    proxy_checker.write_proxies_to_file("good.txt")

if __name__ == "__main__":
    main()
