from urllib.parse import urlparse


def split_s3_uri(uri: str) -> tuple:
    uri_parsed = urlparse(uri)
    scheme = uri_parsed.scheme
    bucket = uri_parsed.netloc
    key = uri_parsed.path.lstrip("/")
    return scheme, bucket, key


if __name__ == "__main__":
    foo = "s3://my-bucket/path/to/key"
    scheme, bucket, key = split_s3_uri(foo)
    print("# SCHEME:", scheme)
    print("# BUCKET:", bucket)
    print("# KEY   :", key)
