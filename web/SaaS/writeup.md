# SaaS

## Description
Welcome to Sed as a Service! Now you can filter lorem ipsum to your heart's desire!

Attachments:
https://imaginaryctf.org/r/C279-app.py 
http://saas.chal.imaginaryctf.org

## Solution 
Taking a look at the description of the challenge, we know that we have to use sed to filter lorem ipsum.

Now let's check app.py.

In app.py, we see that there a blacklist of the characters/strings we can not use.

We can bypass that blacklist for "cat" and "flag", because we can do "ca"t and "fla"g, and it will read it normally.

now on the bottom of app.py, we see that it runs sed for us on the file stuff.txt.

So basically, we want to format in some way where we can print out a flag. 

In sed, there is a way to execute code and that way is to put e in front of what u want to execute.

So inputting els, we see that there is a flag.txt as a file stored.

Now we just have to output that file. 

Using the technique from before to bypass the blacklist, our payload will be e"ca"t "fla"g.txt.

We get the flag!!

flag: ```ictf{:roocu:roocu:roocu:roocu:roocu:roocursion:rsion:rsion:rsion:rsion:rsion:_473fc2d1}```

Note: ```You can also just use head to read the file and do * to read all the files if you didn't know how to bypass the blacklist. In that case, this would be our payload: ehead *```



