#!/usr/bin/env python3
import re
abc = input()
pattern = r'A*B*C*'
if not(re.match(pattern, abc)) :
    print('No')
else :
    print('Yes' if re.search(pattern, abc).group(0) == abc else 'No')