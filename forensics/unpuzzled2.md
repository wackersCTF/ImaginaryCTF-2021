# Unpuzzled 2
by Eth007

## Description
Puzzler7's evil twin is hiding one more secret. Find it for us. (Note: the flag for this challenge ends with 6148}.)

Note: DO NOT stalk/OSINT puzzler7#7657. This will not help you solve this challenge, and will only lead you away from the right solution.

## Solution (by xenonminer)
Searching up unpuzzler7's username on https://instantusername.com/#/, we see that a few sites have this username. If we look through them we see a repl account.

<img src="https://user-images.githubusercontent.com/86171033/126881860-034511cc-ed2a-42d8-80e7-c21025866ab5.PNG" alt="image" width=600/>

https://replit.com/@unpuzzler7 

There's quite a few projects, but if we look at the discord bot, we can see that there is a sequence of base64.

<img src="https://user-images.githubusercontent.com/86171033/126882206-2a415372-0beb-4bc1-8d1b-a694f6f71203.png" alt="DiscordBot code image" widht=600/>

Decode that base64 and we get the flag!

flag: ```ictf{r3pl1t_1snt_th3_pl4c3_t0_st0r3_s3cr3ts_1cb26148}```
