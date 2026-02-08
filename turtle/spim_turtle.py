#!/usr/bin/env python3

import sys
from screen import Screen

def mainloop(screen: Screen) -> None:
    while True:
        cmd = input().split()   # Read a line from stdin and split it at whitespaces
        if not cmd:
            # Empty line
            continue

        match cmd[0]:
            case 'fd':
                if len(cmd) != 2:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 1, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                try:
                    screen.forward(int(cmd[1]))
                except ValueError:
                    print(f"spim_turtle.py: Error: Incorrect argument format for '{cmd[0]}'; expected integer, got {cmd[1]}", \
                          file=sys.stderr)
                    exit(-1)

            case 'bk':
                if len(cmd) != 2:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 1, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                try:
                    screen.backward(int(cmd[1]))
                except ValueError:
                    print(f"spim_turtle.py: Error: Incorrect argument format for '{cmd[0]}'; expected integer, got {cmd[1]}", \
                          file=sys.stderr)
                    exit(-1)

            case 'lt':
                if len(cmd) != 2:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 1, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                try:
                    screen.left(int(cmd[1]))
                except ValueError:
                    print(f"spim_turtle.py: Error: Incorrect argument format for '{cmd[0]}'; expected integer, got {cmd[1]}", \
                          file=sys.stderr)
                    exit(-1)

            case 'rt':
                if len(cmd) != 2:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 1, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                try:
                    screen.right(int(cmd[1]))
                except ValueError:
                    print(f"spim_turtle.py: Error: Incorrect argument format for '{cmd[0]}'; expected integer, got {cmd[1]}", \
                          file=sys.stderr)
                    exit(-1)

            case 'goto':
                if len(cmd) != 3:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 2, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                try:
                    screen.goto(int(cmd[1]), int(cmd[2]))
                except ValueError:
                    print(f"spim_turtle.py: Error: Incorrect argument format for '{cmd[0]}'; expected (integer, integer), got ({cmd[1]}, {cmd[2]})", \
                          file=sys.stderr)
                    exit(-1)

            case 'pu':
                if len(cmd) != 1:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 0, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                screen.penup()

            case 'pd':
                if len(cmd) != 1:
                    print(f"spim_turtle.py: Error: Invalid number of arguments for '{cmd[0]}'; expected 0, got {len(cmd) - 1}", \
                          file=sys.stderr)
                    exit(-1)

                screen.pendown()

            case 'exit':
                screen.finish()
                return

            case _:
                print(f"spim_turtle.py: Error: Invalid command {cmd[0]}", \
                      file=sys.stderr)
                exit(-1)

def main() -> None:
    screen = Screen()
    mainloop(screen)

if __name__ == '__main__':
    main()