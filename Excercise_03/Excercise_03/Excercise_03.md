# Excercise_03

标签（空格分隔）： 计算物理

---
#Abstract
In this program  I use a `loop` structure to realize the horizontal movement of my name pattern.

---
#Background
In last assignment I realize printing my name on the screen, this time we're going to try to move the name pattern

---
#Main Text
I used a simple `loop` structure to achieve this purpose.

- Part 1 Method 1

```python
import os
import time

s1 = ('#######         #               ')
s2 = ('#      #        #      #        ')
s3 = ('#      #        #               ')
s4 = ('#######   ####  ####   #   #####')
s5 = ('#   #    #    # #   #  #   #   #')
s6 = ('#    #   #    # #   #  #   #   #')
s7 = ('#      #  ####  ####   #   #   #')

for j in range(5) :
    os.system('cls')
    print s1
    print s2
    print s3
    print s4
    print s5
    print s6
    print s7
    l1 = list(s1)
    l2 = list(s2)
    l3 = list(s3)
    l4 = list(s4)
    l5 = list(s5)
    l6 = list(s6)
    l7 = list(s7)
    l1.insert(0, "  ")
    l2.insert(0, "  ")
    l3.insert(0, "  ")
    l4.insert(0, "  ")
    l5.insert(0, "  ")
    l6.insert(0, "  ")
    l7.insert(0, "  ")
    s1 = "".join(l1)
    s2 = "".join(l2)
    s3 = "".join(l3)
    s4 = "".join(l4)
    s5 = "".join(l5)
    s6 = "".join(l6)
    s7 = "".join(l7)
    time.sleep(1)
```
- Part 1 Method 2
```python
import os
import time
s1 = ('#######         #               ')
s2 = ('#      #        #      #        ')
s3 = ('#      #        #               ')
s4 = ('#######   ####  ####   #   #####')
s5 = ('#   #    #    # #   #  #   #   #')
s6 = ('#    #   #    # #   #  #   #   #')
s7 = ('#      #  ####  ####   #   #   #')
for j in range(10) :
    os.system('cls')
    print (s1)
    print (s2)
    print (s3)
    print (s4)
    print (s5)
    print (s6)
    print (s7)
    s1 = ' ' + s1
    s2 = ' ' + s2
    s3 = ' ' + s3
    s4 = ' ' + s4
    s5 = ' ' + s5
    s6 = ' ' + s6
    s7 = ' ' + s7
    time.sleep(1)
```
- Part 2 
```python
import os
import time
s1 = ('#######         #               ')
s2 = ('#      #        #      #        ')
s3 = ('#      #        #               ')
s4 = ('#######   ####  ####   #   #####')
s5 = ('#   #    #    # #   #  #   #   #')
s6 = ('#    #   #    # #   #  #   #   #')
s7 = ('#      #  ####  ####   #   #   #')

def b() :
    print (s1)
    print (s2)
    print (s3)
    print (s4)
    print (s5)
    print (s6)
    print (s7)

def a() :
    print (s7)
    print (s6)
    print (s5)
    print (s4)
    print (s3)
    print (s2)
    print (s1)

for i in range(1):
    os.system('cls')
    b()
    time.sleep(1)
    os.system('cls')
    a()  
```

---
#Conclusion
- This simple structure can achieve the requirement of the assignment, yet it could only move the same name pattern.
- I don't know how to rotate the name pattern. I think the ways to achieve this must be fantastic.

---
#Acknowledgements
Thanks to the hint from the assignment discription.
Thanks to my friend Shijie Ni, who help me to use the `time.sleep` to achieve the movement.




