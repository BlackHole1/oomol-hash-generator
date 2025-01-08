from oocana import Context
from src.hash import md5, sha1, sha256, sha224, sha384, sha512

def main(params: dict, context: Context):
    input_str = params['input']
    
    md5_hash = md5(input_str)
    sha1_hash = sha1(input_str)
    sha224_hash = sha224(input_str)
    sha256_hash = sha256(input_str)
    sha384_hash = sha384(input_str)
    sha512_hash = sha512(input_str)

    return {
        "MD5": md5_hash,
        "SHA1": sha1_hash,
        "SHA224": sha224_hash,
        "SHA256": sha256_hash,
        "SHA384": sha384_hash,
        "SHA512": sha512_hash,
    }