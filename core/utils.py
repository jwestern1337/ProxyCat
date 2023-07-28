def construct_http_request(
        method: str='GET',
        url: str='/',
        headers: dict={},
        body: bytes=b''
    ) -> bytes:
    request = f'{method} {url} HTTP/1.1\r\n'
    for header, value in headers.items():
        request += f'{header}: {value}\r\n'
    request += '\r\n'
    request = request.encode() + body
    return request

def parse_http_response(response: bytes) -> tuple:
    status_code = 0
    body = b''
    try:
        response = response.decode()
        status_code = int(response.split(' ')[1])
        body = response.split('\r\n\r\n')[1].encode()
        headers = {}
        for header in response.split('\r\n')[1:]:
            header = header.split(': ')
            headers[header[0]] = header[1]
    except:
        pass # Invalid response
    return status_code, body, headers