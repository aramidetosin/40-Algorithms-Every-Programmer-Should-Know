try:
    import msvcrt


    def getkey():
        return msvcrt.getch()
except ImportError:
    import os, sys, tty, termios


    def getkey():
        fd = sys.stdin.fileno()
        original_attr = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attr)
        return ch
