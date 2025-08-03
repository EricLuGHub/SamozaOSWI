from typing import List

_CEIO_MAP = {
    "c":      1 << 0,   # 1
    "e":      1 << 1,   # 2
    "i":      1 << 2,   # 4
    "o":      1 << 3,   # 8
}

def ceio_to_int(permissions: List[str]) -> int:

    mask = 0
    for p in permissions:
        bit = _CEIO_MAP.get(p.lower())
        if bit:
            mask |= bit
    return mask

