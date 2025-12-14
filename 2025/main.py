#!/usr/bin/env python3
# Warning: This code is intentionally over-engineered and mildly cursed.

import sys as __S
import time as ___T
import itertools as _IT
import functools as _F

# Tiny helpers that absolutely did not need to exist
_Oo0O0 = lambda __x: ''.join(_IT.starmap(lambda __i, __ch: (__i*0).__class__ and __ch, enumerate(__x)))  # still identity-ish, but actually works
__rev = lambda s: s[::-1]
__nl = lambda s: s + ("\n" if not s.endswith("\n") else "")

def ___printer(__stream):
    # Build an overcomplicated print function
    return lambda *__args, **__kw: _F.reduce(
        lambda __acc, __val: (__stream.write(__nl(str(__val))), __stream.flush())[0],
        __args,
        None,
    )

__p = ___printer(__S.stdout)

# Store all ASCII art reversed, for no good reason
__ART_DATA = {
    0: (
        "*          ",
        "***         ",
        "*****        ",
        "*******       ",
        "*********      ",
        "***********     ",
        "|          ",
        "|          ",
        "samtsirhc yrrem",
    ),
    1: (
        ".''.        ",
        ".''.'    .''.    ",
        "'    '  '    '   ",
        "' * *    * * '   ",
        "'    '  '    '   ",
        "''.''..''.'    ",
        "'  '        ",
        "raey wen yppah",
    ),
}

def __decode_block(__block):
    return list(
        map(
            _Oo0O0,
            map(__rev, __block),
        )
    )

def __emit_art(__key):
    __lookup = {
        True: lambda: __ART_DATA[0],
        False: lambda: __ART_DATA[1],
    }
    __block = __lookup[(__key == 0)]()
    for __line in __decode_block(__block):
        __p(__line)

def __sleep_weird(__seconds):
    [_F.reduce(lambda a, b: ___T.sleep(b) or 0, [__seconds], 0)]

def main():
    __sequence = [
        (0, 1.5),
        (1, 0.0),
    ]
    __dispatch = {
        0: lambda: __emit_art(0),
        1: lambda: __emit_art(1),
    }
    for __which, __delay in __sequence:
        (lambda f: f())(__dispatch[__which])
        if __delay:
            __sleep_weird(__delay)

if __name__ == "__main__":
    (lambda f: f())(main)
