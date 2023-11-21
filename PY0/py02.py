# -*- coding: utf-8 -*-

import string

alph =list(string.ascii_lowercase)

for idx in range(0, 26):
    print(alph[25 - idx], end="")
    