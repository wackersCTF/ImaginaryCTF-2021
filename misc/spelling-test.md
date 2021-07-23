# Spelling Test
I made a spelling test for you, but with a twist. There are several words in words.txt that are misspelled by one letter only. Find the misspelled words, fix them, and find the letter that I changed. Put the changed letters together, and you get the flag. Make sure to insert the "{}" into the flag where it meets the format.

NOTE: the words are spelled in American English

https://imaginaryctf.org/r/CBC8-words.txt

# Solution

I plugged the words into a new grammarly document (free account) for it to find mispelled words. It also counts non-capitalized proper nouns however, which meant that I couldn't do it from the grammarly interface itself. Instead, I inspected the webpage and searched for "correct your spelling". I found 24 instances of mispelled words (25 results but one didn't count as it was part of the website itself) and wrote down each incorrect character.

Originally, I ended up with ```ctfyoupassedthespelling``` which was missing a few characters. However, I could guess what they were and fill in the rest.

flag: ```ictf{youpassedthespellingtest}```
