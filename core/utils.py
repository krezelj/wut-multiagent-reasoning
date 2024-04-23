def enc2values(enc: int, literals: list[str]) -> dict:
    values = {}
    for l in literals[::-1]:
        values[l] = (enc & 1) == 1
        enc >>= 1
    return values



def values2enc(values: dict, literals: list[str]) -> int:
    enc = 0
    for l in literals:
        enc <<= 1
        enc |= values[l]
    return enc


def is_strict_subset(a: int, b: int) -> bool:
    return (a | b == b) and (a != b)


def is_subset(a: int, b: int) -> bool:
    return a | b == b