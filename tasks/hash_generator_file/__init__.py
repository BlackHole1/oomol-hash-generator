from oocana import Context
from src.hash import md5, sha1, sha256, sha224, sha384, sha512

def main(params: dict, context: Context):
    input_file = params['input']
    
    with open(input_file, 'rb') as file:
        md5_hash = md5(file)
        sha1_hash = sha1(file)
        sha224_hash = sha224(file)
        sha256_hash = sha256(file)
        sha384_hash = sha384(file)
        sha512_hash = sha512(file)

    return {
        "MD5": md5_hash,
        "SHA1": sha1_hash,
        "SHA224": sha224_hash,
        "SHA256": sha256_hash,
        "SHA384": sha384_hash,
        "SHA512": sha512_hash,
    }