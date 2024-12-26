import os
import sys,subprocess
import random
import time
from itertools import count


def clear():
    os=sys.platform

    if os == 'win32':
        subprocess.run('cls',shell=True)

def enter():
    while True:
        print("Type 'y' and hit enter to continue")
        yes=str(input()).lower()
        if yes == 'y':
            print()
            break
        else:
            print("Please hit 'y' only")


def countdown(a):
    while a:
        mins, secs = divmod(a, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        a -= 1

    print('Your time is up!')

def display():
    if random_program == "Butterfly Star Pattern":
        print(butterfly)
        print(butterfly_code)
    elif random_program == "Number Changing Pyramid Pattern":
        print(number_changing_pyramid)
        print(number_changing_pyramid_code)
    elif random_program == "Square Hollow Pattern":
        print(Square_Hollow_Pattern)
        print(Square_Hollow_Pattern_code)
    elif random_program == "Zero-One Triangle Pattern":
        print(Zero_One_Triangle_Pattern)
        print(Zero_One_Triangle_Pattern_code)
    elif random_program == "Mirror Image Triangle Pattern":
        print(mirror_image_triangle)
        print(mirror_image_triangle_code)
    elif random_program == "X Pattern":
        print(x)
        print(x_code)



clear()
print("""
     ------BUG BOUNTY------
 
         ,__                   __
    '~~****Nm_    _mZ*****~~
            _8@mm@K_
           W~@`  '@~W
          ][][    ][][
    gz    'W'W.  ,W`W`    es
  ,Wf    gZ****MA****Ns    VW.
 gA`   ,Wf     ][     VW.   'Ms
Wf    ,@`      ][      '@.    VW
M.    W`  _mm_ ][ _mm_  'W    ,A
'W   ][  i@@@@i][i@@@@i  ][   W`
 !b  @   !@@@@!][!@@@@!   @  d!
  VWmP    ~**~ ][ ~**~    YmWf
    ][         ][         ][
  ,mW[         ][         ]Wm.
 ,A` @  ,gms.  ][  ,gms.  @ 'M.
 W`  Yi W@@@W  ][  W@@@W iP  'W
d!   'W M@@@A  ][  M@@@A W`   !b
@.    !b'V*f`  ][  'V*f`d!    ,@
'Ms    VW.     ][     ,Wf    gA`
  VW.   'Ms.   ][   ,gA`   ,Wf
   'Ms    'V*mmWWmm*f`    gA`
   
     ------BUG BOUNTY------
""")

print("Welcome to Bug Bounty!")
print("Check your ability to hunt all the bugs and win the bounty!")
print()
enter()
clear()
print("""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗███████╗ █████╗ ███╗   ███╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   █████╗  ███████║██╔████╔██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                      
""")
print("Before we begin, we would like to know more about you....")
print()
team_name=input("Enter your team name: ")
print("Welcome " + team_name)
print()
print("Your teammates belonging to 'Group A' have completed Round 1 and you are up next to finish the final round which is 'Round 2'.")
print()
print("Buckle up as we dial the difficulty from 'Normal Mode' to 'Hard Mode'.")
print()
print("Are you ready to begin Round 2 of 'Bug Bounty'?")
enter()
clear()
print("There are 6 programs in Round 2.\n\nEach team will be given a random program and the task is to hunt all the bugs in order to win the 'BOUNTY'."
      "\n\nThe Bounty on each bug in Round 2 is $1000.\n\nYour program will contain three bugs.\n\nGood Luck\n\n")

round_one = ["Butterfly Star Pattern", "Number Changing Pyramid Pattern",
             "Square Hollow Pattern", "Zero-One Triangle Pattern",
             "Mirror Image Triangle Pattern", "X Pattern"]

random_program = random.choice(round_one)
#random_program = "A number that is greater than 1 & divided by 1 or itself"
print("Your program is: " + random_program)
print()
enter()

butterfly = ("""
    *          *
    **        **
    ***      ***
    ****    ****
    *****  *****
    ************
    ************
    *****  *****
    ****    ****
    ***      ***
    **        **
    *          *
""")

butterfly_code = ("""
        import java.util.*;
        public class Butterfly {

    public static void printPattern(int n)
    {
        int i, j;
        int num = 1;

        for (i = 1; i <= n; i++) {
            
            for (j = 1; j <= i; j++) {
                System.out.print("*");
            }

            int spaces = 2 * (n - i);
            for (j = 1; j <= spaces; j++) {
                System.out.print(" ");
            }
            
            for (j = 1; j <= i; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        for (i = n; i >= 1; i--) {
            for (j = 1; j <= i; j++) {
                System.out.print("*");
            }

            int spaces = 2 * (n - i);
            for (j = 1; j <= spaces; j++) {
                System.out.print(" ");
            }

            for (j = 1; j <= i; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
    
    public static void main(String args[])
    {
        int n = 6;
        printPattern(n);
    }
}
""")

number_changing_pyramid = ("""
        1 
        2 3 
        4 5 6 
        7 8 9 10 
        11 12 13 14 15 
        16 17 18 19 20 21
""")

number_changing_pyramid_code = ("""
    import java.util.*;

    public class Numberchangepyramid {
   
    public static void printPattern(int n)
    {
        int i, j;
        int num = 1;
      
        for (i = 1; i <= n; i++) {
           
            for (j = 1; j <= i; j++) {
                System.out.print(num + " ");
                num++;
            }
            System.out.println();
        }
    }
    
    public static void main(String args[])
    {
        int n = 6;
        printPattern(n);
    }
}
""")

Square_Hollow_Pattern = ("""
        ******
        *    *
        *    *
        *    *
        *    *
        ******
""")

Square_Hollow_Pattern_code = ("""
        import java.util.*;

    public class Squarehollow {
    public static void printPattern(int n)
    {
        int i, j;
        for (i = 0; i < n; i++) {

            for (j = 0; j < n; j++) {
                if (i == 0 || j == 0 || i == n - 1
                    || j == n - 1) {
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String args[])
    {
        int n = 6;
        printPattern(n);
    }
}
""")

Zero_One_Triangle_Pattern = ("""
        1 
        0 1 
        1 0 1 
        0 1 0 1 
        1 0 1 0 1 
        0 1 0 1 0 1 
""")

Zero_One_Triangle_Pattern_code = ("""
        import java.util.*;

    public class Zeroone {
    public static void printPattern(int n)
    {
        int i, j;
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= i; j++) {
                if ((i + j) % 2 == 0) {
                    System.out.print(1 + " ");
                }
                else {
                    System.out.print(0 + " ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String args[])
    {
        int n = 6;
        printPattern(n);
    }
}
""")

mirror_image_triangle = ("""
    1 2 3 4 5 6 
     2 3 4 5 6 
      3 4 5 6 
       4 5 6 
        5 6 
         6 
        5 6 
       4 5 6 
      3 4 5 6 
     2 3 4 5 6 
    1 2 3 4 5 6
""")

mirror_image_triangle_code = ("""
    import java.util.*;

    public class Mirrorimage {
    public static void printPattern(int n)
    {
        int i, j;
        for (i = 1; i <= n; i++) {
            for (j = 1; j < i; j++) {
                System.out.print(" ");
            }
            for (j = i; j <= n; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
        
        for (i = n - 1; i >= 1; i--) {
            for (j = 1; j < i; j++) {
                System.out.print(" ");
            }
            for (j = i; j <= n; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
    public static void main(String args[])
    {
        int n = 6;
        printPattern(n);
    }
}
""")

x = ("""
    *   *
     * *
      *
     * *
    *   *
""")

x_code = ("""
    public class CrossStarPattern {
    public static void main(String[] args) {
        int size = 5;
        for (int i = 1; i <= size; ++i) {
            for (int j = 1; j <= size; ++j) {
                if (j == i || j == size - i + 1)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }
    }
}
""")

display()
countdown(3600)




