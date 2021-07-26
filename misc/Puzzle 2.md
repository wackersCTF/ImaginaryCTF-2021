# Puzzle 2

## Description
The evil presidential candidate Et3rnos is now forcing this poor game's players to vote on him in order to access the flag room. Can you teach him a lesson and get access to it without voting on him? The flag is in the format ICTF{[A-Z_]+}

Attachments:
https://imaginaryctf.org/r/64FA-puzzle_2.zip

## Solution 
First step is to unzip the file given and play the unity game.

We see that we can open 3 walls but the 4th pillar doesn't look like its going to drop without us changing something.

Now you want a unity disassembler  or a c# disassembler

Dnspy is a good one. Cheat engine also works

Import the Assembly-CSharp.dll file into dnspy.

Look through all the functions

I mainly looked at collision detection or mainly how to destroy wall/go through wall

```
private void OnCollisionEnter(Collision collision)
	{
		if (collision.gameObject.CompareTag("Solid"))
		{
			this.stopped = false;
		}
	}
```

All u had to do was delete the part next to collision.gameObject.CompareTag("Solid") since it checked the state of the pillar.

flag: ```ICTF{SPY_KIDS_ASSEMBLE}```


