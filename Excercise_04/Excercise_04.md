# Excercise_04

标签（空格分隔）： 计算物理

---
[TOC]

---

#Abstract
In this program I provide a numerical methods(Euler method) to solve the problem in page 16, problem1.6 and give some discriptive words to my program, in which I use the `class` to create my own new object and use the methods of this `class` to solve the problem. It's the time that I get exposed to the object-oriented-programming paradigm.

---
#Background

We've learned to solve the decay problem of a single kind of nucleus in our last class. And in this problem we are faced with the decay of two kinds of nucleus.Moreover these two kind of nucleus can actually decay to the other kind of nucleus. However I think the essential part of the program does not change. So I imitate the teacher's program write my own. What's different is that I create two sets of tuples to get the numerical result.

---
#Main Text
##Part 1 - The Analytical solution
Firstly, let's take a look at the differential equations and its initial value.

The rate equations:
$$\frac{dN_A}{dt} = \frac{N_B}{\tau} - \frac{N_A}{\tau}\\
\frac{dN_B}{dt} = \frac{N_A}{\tau} - \frac{N_B}{\tau}$$

The initial value:$N_A = 100$, $N_B = 0$, and take $\tau = 1s$.

The solution to the differential equation is :
$$N_A = 50e^{-2t/\tau}+50\\
N_B = -50e^{-2t/\tau}+50$$
Although it's rather easy to get the analytical sultion for a student who has taken the course of ODE, I think it's also inspiring to use the Euler method to solve this problem, which leads to a universal method to solve the ordinary differential equation set of order 1.

##Part 2 - Numerical Method
Here is my program for this problem.
```python
import pylab as pl
import math

class duel_decay:
    """docstring for "duel decay". Programmed by Yuan Tian."""
    def __init__(self, number_of_nuclei_nA = 100, number_of_nuclei_nB = 0, time_costant = 1, time_of_duration = 5, time_interval = 0.05):
        self.nA = [number_of_nuclei_nA]
        self.nB = [number_of_nuclei_nB]
        self.t = [0]
        self.tau = time_costant
        self.dt = time_interval
        self.time = time_of_duration
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial number of type A nuclei ->', number_of_nuclei_nA)
        print('Initial number of type B nuclei ->', number_of_nuclei_nB)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
    def calculate(self):
        for i in range(self.steps):
            tmp_A = self.nA[i] + (self.nB[i] - self.nA[i]) / self.tau * self.dt
            tmp_B = self.nB[i] + (self.nA[i] - self.nB[i]) / self.tau * self.dt
            self.nA.append(tmp_A)
            self.nB.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.nA, 'b', label = 'Number of Nuclei A')
        pl.plot(self.t, self.nB, 'r', label = 'Number of Nuclei B')
        pl.title('Change of Nuclei Relative to the Time')
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc = 'best')
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.nA[i], self.nB[i], file = myfile)
        myfile.close()


a = duel_decay()
a.calculate()
a.show_results()
a.store_results()

class exact_result_check(duel_decay):
    def show_results(self):
        self.etA = []
        self.etB = []
        for i in range(len(self.t)):
            temp_A = 50 * math.exp(-2 * self.t[i] / self.tau) + 50
            temp_B = -50 * math.exp(-2 * self.t[i] / self.tau) + 50
            self.etA.append(temp_A)
            self.etB.append(temp_B)
        pl.plot(self.t, self.etA, 'b', label = 'A-analytical')
        pl.plot(self.t, self.nA, '*', label = 'A-numerical')
        pl.plot(self.t, self.etB, 'r', label = 'B-analytical')
        pl.plot(self.t, self.nB, 'x', label = 'B-numerical')
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)
        pl.legend(loc = 'best')
        pl.show()

b = exact_result_check(time_interval = 0.2)
b.calculate()
b.show_results()

class diff_step_check(duel_decay):
    def show_results(self, style):
        pl.plot(self.t, self.nA, style)
        pl.plot(self.t, self.nB, style)
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)

c = diff_step_check(time_interval = 0.05)
c.calculate()
c.show_results('b')

d = diff_step_check(time_interval = 0.1)
d.calculate()
d.show_results('g')

e = diff_step_check(time_interval = 0.2)
e.calculate()
e.show_results('y')

f = diff_step_check(time_interval = 0.25)
f.calculate()
f.show_results('m')
```
In this program I imitate teacher's program to use the `class` to solve the problem.This method feature the convenience of applying the methods defined for the class to manipulate the outcome and reuse the code.Aslo the inheritance function of the derived class is rather powerful to modify and facilitate the based class. So I spend some time to learn how to use the `class` and now I can some how grasp the feature of python.

In the class `duel_decay` I define three methods to solve the problem.

+ The initiation method:
```python
def __init__(self, number_of_nuclei_nA = 100, number_of_nuclei_nB = 0, time_costant = 1, time_of_duration = 5, time_interval = 0.05):
        self.nA = [number_of_nuclei_nA]
        self.nB = [number_of_nuclei_nB]
        self.t = [0]
        self.tau = time_costant
        self.dt = time_interval
        self.time = time_of_duration
        self.steps = int(time_of_duration // time_interval + 1)
        print('Initial number of type A nuclei ->', number_of_nuclei_nA)
        print('Initial number of type B nuclei ->', number_of_nuclei_nB)
        print('Time interval ->', time_interval)
        print('Total time ->', time_of_duration)
```
When you create a new instance of this class the program will automatically call the `_init_` function and this process is called the __instantation__.
We initiate the new instance by giving it the initial value of the calculation,including the number of nuclei of both kinds, the time constant,the time duration and the time interval.

+ The Calculation method
```python
def calculate(self):
        for i in range(self.steps):
            tmp_A = self.nA[i] + (self.nB[i] - self.nA[i]) / self.tau * self.dt
            tmp_B = self.nB[i] + (self.nA[i] - self.nB[i]) / self.tau * self.dt
            self.nA.append(tmp_A)
            self.nB.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
```
In this method we invoke the `loop` function and use the Euler method.It's because the __next__ value of the number of nuclei is deternmined by the __previous__ one that we can use the Euler method provided the initial value is known.

In this problem we are faced with a set of ODE of __order 1__.So for approximation we only need to consider the first order.That's why the Euler method is appropriate for this problem.

Also notice that we use the `.append` method to add new value to the tuple so that we can make a plot using the data from these tuples in the third step.

+ The Plot Method
```python
def show_results(self):
        pl.plot(self.t, self.nA, 'b', label = 'Number of Nuclei A')
        pl.plot(self.t, self.nB, 'r', label = 'Number of Nuclei B')
        pl.title('Change of Nuclei Relative to the Time')
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc = 'best')
        pl.show()
```
In this part I use the module from the matplotlib to show the numerical results of the calculation which is rather intuative to examine the results.

+ The Store Method
```python
def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.nA[i], self.nB[i], file = myfile)
        myfile.close()
```
Actually I don't understand the meaning of this part of program.

The Numerical results:![Numerical solution](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_04/excercise_04_01.jpg)
(If the picture is broken,please view it in my repository documents @ https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_04/excercise_04_01.jpg)
This picture gives us an intuative impression on how the result should be looked like.

## Part 3 - Comparison to the Analytical Results
```python
class exact_result_check(duel_decay):
    def show_results(self):
        self.etA = []
        self.etB = []
        for i in range(len(self.t)):
            temp_A = 50 * math.exp(-2 * self.t[i] / self.tau) + 50
            temp_B = -50 * math.exp(-2 * self.t[i] / self.tau) + 50
            self.etA.append(temp_A)
            self.etB.append(temp_B)
        pl.plot(self.t, self.etA, 'b', label = 'A-analytical')
        pl.plot(self.t, self.nA, '*', label = 'A-numerical')
        pl.plot(self.t, self.etB, 'r', label = 'B-analytical')
        pl.plot(self.t, self.nB, 'x', label = 'B-numerical')
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)
        pl.legend(loc = 'best')
        pl.show()
```
In this part of program I plot the analytical results and numerical results in one coordinate, and the plot are as followed:

![Comparison](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_04/excercise_04_02.jpg)
(If the picture is broken,please view it in my repository documents at https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_04/excercise_04_02.jpg)

Notice that I change the time interval to a greater one in order to make the information of the image more clear.

It's obvious that the value we got deviate a little from the accurate result, this is the same situation that we met in the class and it shows that the approximation do bring about the deviation.

```python
class diff_step_check(duel_decay):
    def show_results(self, style):
        pl.plot(self.t, self.nA, style)
        pl.plot(self.t, self.nB, style)
        pl.xlabel('time $s$')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)

c = diff_step_check(time_interval = 0.05)
c.calculate()
c.show_results('b')

d = diff_step_check(time_interval = 0.1)
d.calculate()
d.show_results('g')

e = diff_step_check(time_interval = 0.2)
e.calculate()
e.show_results('y')

f = diff_step_check(time_interval = 0.25)
f.calculate()
f.show_results('m')

g = diff_step_check(time_interval = 0.5)
g.calculate()
g.show_results('k')
```
In the part I create a derived class based on the former class to make use of the former methods.In this class I redefine the `show_result()`function in order to compare results of different time interval. We can see from the image that smaller interval leads to more accurate result.

Pay close attention to the black line with time interval of 0.5s(which is 1/10 of the whole time).It's shape is distorted and is obvious different from other strings. This is because the time interval is so large that even the first step deviate from the accurate result obviously, so the following steps of value go straight to the equilibrium line and stay unchanged.

![different intervals](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_04/excercise_04_03.jpg)
(https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_04/excercise_04_03.jpg)

---

#Conclusion(Result Analysis)
+ The numerical results are not absolutely the same with the analytical results.

+ However the numerical results are highly consistant with the analytical results or they're very good approximation of the analytical results.

+ The existence of the deviation from the analytical ones shows that after all we use the method of approximation and the higher terms are omiited for the convenience of calculation.

+ We can reserve the higher terms and also use the `loop` structure to do the approximation and this time maybe much smaller deviation.

+ __I think we can differentiate both sides of the rate equation and get the second order approximation to get more accurate results. I think this method will be rather effective(for more accurate result), but in this problem the initial value of the first order is redundant and obey the physical starting opion of the problem. So I think higher approximation is more suitable to differential equations of higher oders.__

+ Answer to "How do we know that the erros introduced by this discreteness are negligible?":Because we are solving the first order differential equations and the higher terms is negligibly small.

+ Answer to "How do we choose the value of such a step size for a calculation?":On the one hand small step means small interval, __small deviation from the accurate result and more data__,so probably the smaller the better. On the other hand, too much small step will cause the efficiency to decrease rapidly yet sufficiently small step may probably suffice to approximate to a decent degree.

+ I learn from the source code of some modules that the source code is mainly written in an object-oriented-programing manner, i.e. using the class and define its methods.So I find it fascinating and powerful to get familiar with this kind of paradigm of programming.

---

#Acknowledgements
Thanks to the teacher's program in the lecture notes.
Thanks to the documentations in website of python and matplotlib