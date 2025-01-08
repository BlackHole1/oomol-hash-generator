from oocana import Context
from src.hash import md5, sha1, sha256, sha224, sha384, sha512

def main(params: dict, context: Context):
    input_str = params['input']
    hash_funcs = {
        "MD5": md5,
        "SHA1": sha1,
        "SHA224": sha224,
        "SHA256": sha256,
        "SHA384": sha384,
        "SHA512": sha512
    }

    results = {
        name: func(input_str) for name, func in hash_funcs.items()
    }

    if not params['lowercased']:
        results = {k: v.upper() for k, v in results.items()}

    return results
