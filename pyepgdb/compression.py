import gzip


def parse (f):
    f.read(12)
    return gzip.GzipFile(fileobj=f)
