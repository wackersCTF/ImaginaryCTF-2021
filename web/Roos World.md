# Roos World

## Description
Somebody hid Roo's flag on his website. Roo really needs some help.

Attachments:
http://roos-world.chal.imaginaryctf.org

## Solution 
Look at the website, it talks about inspecting the website better.

It's obviously hinting us at inspecting the elements or reading source code with Ctrl + U.

Looking at the source code, we see some comments that are rickroll links, and the other one telling us that it's not that easy to get the flag.

Looking through the rest of the source code, we see that there is a script that is obfuscated in jsfuck.

We put in the script to a jsfuck deobfuscator like https://enkhee-osiris.github.io/Decoder-JSFuck/.

We are given: ```console.log(atob("aWN0ZnsxbnNwM2N0MHJfcjAwX2cwZXNfdGgwbmt9"));```

Well let's analyze what this does.

console.log just prints out the text to the screen.
atob is a function to turn a base64 string into normal

So let's try putting that string in a base64 decoder like https://www.base64decode.org/.

We get our flag!!

flag: ```ictf{1nsp3ct0r_r00_g0es_th0nk}```


