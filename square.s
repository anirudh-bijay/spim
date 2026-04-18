# File: square.s
# 
# Description:
#   Example program to draw a square using turtle graphics.

        .data
msg1:   .asciiz "This program draws a square of side 100.\n"
msg2:   .asciiz "Done!\n"

        .text
        .globl  main
main:
#
# Description:
#   Entry point into the program.
#
# Calling convention:
#   System V
#
# Parameters:
#   None
#
# Returns:
#   Zero
#
######################################### int main(void) {
        li              $v0, 4          #
        la              $a0, msg1       #
        syscall                         #   puts(msg1);
                                        #
        li              $t0, 4          #   int i = 4;
loop:                                   #   do {
        li              $v0, 33         #     
        li              $a0, 100        #
        syscall                         #     turtle_fd(100);
                                        #
        li              $v0, 35         #
        li              $a0, 90         #
        syscall                         #     turtle_lt(90);
                                        #
        addiu           $t0, $t0, -1    #     i--;
        bnez            $t0, loop       #   } while (i);
                                        #
        li              $v0, 4          #
        la              $a0, msg2       #
        syscall                         #   puts(msg2);
                                        #
        li              $v0, 0          #
        jr              $ra             #   return 0;
######################################### }
