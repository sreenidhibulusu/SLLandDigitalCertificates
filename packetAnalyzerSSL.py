
from OpenSSL import crypto
import ssl
import urllib

def getCert(url):
    keys = dict.fromkeys(range(1,4))
    addr = urllib.parse.urlsplit(url).hostname
    port = 443
    encoding = 'utf-8'
    cert = ssl.get_server_certificate((addr, port), ssl_version=5)
    keys[1] = cert

    cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    issuer = cert.get_issuer()

    keys[2] = issuer.get_components()

    subject = cert.get_subject()
    components = dict(subject.get_components())

    keys[3] = components
    return keys


