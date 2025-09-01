#!/usr/bin/env python3
import re
s = input()
print("Yes" if re.search('<=*>',s) is not None and re.search('<=*>',s).group() == s else "No")
