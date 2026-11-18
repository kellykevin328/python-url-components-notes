import urllib.parse

def solve(value):
    return (lambda u: {"scheme": u.scheme, "host": u.hostname, "path": u.path, "query": u.query, "fragment": u.fragment})(urllib.parse.urlsplit(value))
