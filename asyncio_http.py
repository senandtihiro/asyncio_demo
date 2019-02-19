import asyncio

from urllib.parse import urlparse


async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode('utf8')
        all_lines.append(data)
    html = '\n'.join(all_lines)
    return html

