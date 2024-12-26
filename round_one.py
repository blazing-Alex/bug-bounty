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
    if random_program == "A number that is greater than 1 & divided by 1 or itself":
        print(prime_number)
    elif random_program == "Next number is the sum of given 2 numbers":
        print(factorial)
    elif random_program == "Number that is same even after reverse":
        print(palindrome)
    elif random_program == "A number that is sum of cubes of its number":
        print(armstrong)
    elif random_program == "A number is divisible by the sum of its digits":
        print(harshad)
    elif random_program == "Reverse a Number":
        print(reverse)
    elif random_program == "Sum of the factorial of the individual digits is equal to the number":
        print(strong)
    elif random_program == "Convert Decimal number into a Binary number":
        print(convert)
    elif random_program == "Print all natural numbers upto N without using a semicolon":
        print(natural_without_semicolon)
    elif random_program == "Positive integer which is equal to the sum of its positive divisors, excluding the number itself":
        print(perfect_number)



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
print()
print("Welcome " + team_name)
print()
print("Get ready to experience an event like never before...")
print()
print("Are you ready to begin Round 1 of 'Bug Bounty'?")
enter()
clear()
print("There are 10 programs in Round 1.\n\nEach team will be given a random program and the task is to hunt the bugs in order to win the 'BOUNTY'."
      "The Bounty on each bug in Round 1 is $500.\n\nYour program will contain three bugs.\n\nGood Luck\n\n")

round_one = ["A number that is greater than 1 & divided by 1 or itself", "Next number is the sum of given 2 numbers",
             "Number that is same even after reverse", "A number that is sum of cubes of its number",
             "A number is divisible by the sum of its digits", "Reverse a Number", "Sum of the factorial of the individual digits is equal to the number",
             "Convert Decimal number into a Binary number", "Print all natural numbers upto N without using a semicolon",
             "Positive integer which is equal to the sum of its positive divisors, excluding the number itself"]

random_program = random.choice(round_one)
#random_program = "A number that is greater than 1 & divided by 1 or itself"
print("Your program is: " + random_program)
print()
enter()
prime_number = ("""
    bool isPrime(int N) {
    if (N <= 1) {
        return false;
    }
    for (int i = 2; i < N; i++) {
        if (N % i == 0) {
            return false;
        }
    }
    return true;
}

    int main() {
        int N = 29;
        printf("Is %d prime?", N);
    
        if (isPrime(N)) {
            printf("Yes");
        }
        else {
            printf("No");
        }
    
        return 0;
}
""")

factorial = ("""
    #include<stdio.h>  
    int main()
    {
     int n1=0,n2=1,n3,i,number;
     printf(“Enter the number of elements:”);
     scanf(“%d”,&number);
     printf(“%d %d”,n1,n2);
     for(i=2;i<number;++i)
     {
      n3=n1+n2;
      printf(” %d”,n3);
      n1=n2;
      n2=n3;
     }
      return 0;
     }
""")

palindrome = ("""
    #include<stdio.h>
    int main()
    {
    int n,r,sum=0,temp;
    printf(“enter the number=”);
    scanf(“%d”,&n);
    temp=n;
    while(n>0)
    {
    r=n%10;
    sum=(sum*10)+r;
    n=n/10;
    }
    if(temp==sum)
    printf(“palindrome number “);
    else
    printf(“not palindrome”);
    return 0;
    }
""")

armstrong=("""
    #include<stdio.h>
     int main()
    {
    int n,r,sum=0,temp;
    printf(“enter the number=”);
    scanf(“%d”,&n);
    temp=n;
    while(n>0)
    {
    r=n%10;
    sum=sum+(r*r*r);
    n=n/10;
    }
    if(temp==sum)
    printf(“armstrong  number “);
    else
    printf(“not armstrong number”);
    return 0;
    }
""")

harshad=("""
    #include <stdio.h>  
    int main()
    {
        int num = 156;
        int rem = 0, sum = 0, n;  
        n = num;
        while(num > 0){
            rem = num%10;
            sum = sum + rem;
            num = num/10;
        }  
        if(n%sum == 0)
            printf(“%d is a harshad number”, n);
        else
            printf(“%d is not a harshad number”, n);
        return 0;
    }
""")

reverse=("""
    #include<stdio.h>
     int main()
    {
    int n, reverse=0, rem;
    printf(“Enter a number: “);
      scanf(“%d”, &n);
      while(n!=0)
      {
         rem=n%10;
         reverse=reverse*10+rem;
         n/=10;
      }
      printf(“Reversed Number: %d”,reverse);
    return 0;
    }
""")

strong = ("""
    #include <stdio.h>
    int main()
    {
        int n;
        int sum=0;
        printf(“Enter a number”);
        scanf(“%d”,&n);
        int k=n;
        int r;
        while(k!=0)
        {
            r=k%10;
            int f=fact(r);
            k=k/10;
            sum=sum+f;
        }
        if(sum==n)
        {
            printf(“Number is a strong”);
        }
        else
        {
            printf(“Number is not a strong”);
        }
        return 0;
    }
    int fact(int r)
    {
        int mul=1;
        for(int i=1;i<=r;i++)
        {
            mul=mul*i;
        }
        return mul;
    }
""")

convert = ("""
        #include<stdio.h>  
        #include<stdlib.h>
        int main(){
        int a[10],n,i;
        system (“cls”);
        printf(“Enter the number to convert: “);
        scanf(“%d”,&n);
        for(i=0;n>0;i++)
        {
        a[i]=n%2;
        n=n/2;
        }
        printf(“Binary of Given Number is=”);
        for(i=i-1;i>=0;i–)
        {
        printf(“%d”,a[i]);
        }
        return 0;
        }
""")

natural_without_semicolon = ("""
        #include<stdio.h>
        #define N 10
         
        int main(int num)
        {
            if (num <= N && printf("%d ", num) && main(num + 1))
            {
            }     
        }
""")

perfect_number = ("""
        #include<stdio.h>
        #include<conio.h>
        void main()
        {
        int i = 1, num, Sum = 0;
        printf(” Enter any number to check Perfect Number”);
        scanf(“%d”, &num);
        while(i < num )
                  {
                     if(num % i == 0)
                     Sum = Sum + i;
                     i++;
                  }
                   if(Sum == num)
                     printf(“%d is Perfect Number”, num);
                   else
                   printf(“%d is not a Perfect Number”, num);
        getch();
        }
""")
display()
countdown(3600)




