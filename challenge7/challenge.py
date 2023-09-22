import urllib3 as ur3
import ssl as sss

import socket
import ssl

hostname = 'www.example.com'
context = sss.create_default_context()

pool = ur3.connection_from_url('someurl', cert_reqs='NONE')
pool = ur3.proxy_from_url('someurl', cert_reqs="NONE")