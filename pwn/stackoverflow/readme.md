# stackoverflow

## Description
Welcome to Stack Overflow! Get answers to all your programming questions right here!

Attachments:
https://imaginaryctf.org/r/E795-stackoverflow 
```nc chal.imaginaryctf.org 42001```

## Solution 
From the title of the challenge, we know that it is going to be a buffer overflow challenge.

Let's first open the program with ghidra.

We see that our input variable has been assigned 40 buffer size so we can fill it up with A's.

Then we see that we will get a shell if we are able to get local_10 written to 0x69637466.

We will use pwntools to create the exploit.

Basically, we can receive a connection first, check for the line before input part, then send our payload.

Our payload will simply be ```b'A'*40 + p64(0x69637466)```

Run the program and do cat flag.txt, and we get our flag!

flag: ```ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}```



