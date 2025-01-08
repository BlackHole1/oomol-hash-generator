import hashlib
from typing import Union, BinaryIO, Callable

def _hash_file(file_obj: BinaryIO, hash_func: callable) -> str:
    while chunk := file_obj.read(8192):  # 每次读取 8KB
        hash_func.update(chunk)
    return hash_func.hexdigest()

def _create_hash(val: Union[str, bytes, BinaryIO], hash_func: Callable) -> str:
    hash_obj = hash_func()
    
    if isinstance(val, (str, bytes)):
        if isinstance(val, str):
            val = val.encode('utf-8')
        hash_obj.update(val)
        return hash_obj.hexdigest()

    val.seek(0)
    return _hash_file(val, hash_obj)

def md5(val: Union[str, bytes, BinaryIO]) -> str:
    return _create_hash(val, hashlib.md5)

def sha1(val: Union[str, bytes, BinaryIO]) -> str:
    return _create_hash(val, hashlib.sha1)

def sha224(val: Union[str, bytes, BinaryIO]) -> str:
    return _create_hash(val, hashlib.sha224)

def sha256(val: Union[str, bytes, BinaryIO]) -> str:
    return _create_hash(val, hashlib.sha256)

def sha384(val: Union[str, bytes, BinaryIO]) -> str:
    return _create_hash(val, hashlib.sha384)

def sha512(val: Union[str, bytes, BinaryIO]) -> str:
    return _create_hash(val, hashlib.sha512)
