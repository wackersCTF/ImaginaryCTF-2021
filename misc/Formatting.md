# Formatting

## Description
Wait, I thought format strings were only in C???

Attachments:
https://imaginaryctf.org/r/14BD-stonks.py 
```nc chal.imaginaryctf.org 42014```

## Solution 
We automatically know that this is a python format strings challenge because of the title and description.

We search up on google ```python format string vulnerability```

This is the website we want: https://www.geeksforgeeks.org/vulnerability-in-str-format-in-python/

Looking through the website we see ```{people_obj.__init__.__globals__[CONFIG][KEY]}```

We change this to match our case and we have our payload: ```{a.__init__.__globals__[flag]}```

Input this payload intoi the netcat server provided and we get our flag!

flag: ```ictf{c4r3rul_w1th_f0rmat_str1ngs_4a2bd219}```



