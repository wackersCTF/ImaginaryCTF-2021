# Hidden

## Description
Oh no, someone hid my flag behind a giant red block! Please help me retrieve it!!

Attachments:
https://imaginaryctf.org/r/10C4-challenge.psd

## Solution 
First, trying to run file on the file that they gave us, we see that it is a Adobe Photoshop Image.

Trying to open it with gimp, it gives us an error.

So since this is a 50 point challenge, it shouldn't be as hard as figuring out how to remove the red block.

So let's check the file with strings!

running strings challenge.psd | grep ictf gets us the flag!

flag: ```ictf{wut_how_do_you_see_this}```

