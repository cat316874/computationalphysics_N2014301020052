# Excercise_09

标签（空格分隔）： 计算物理

---

[TOC]

---
#Abstract
In this program I construct a program for the stadium billiard using the Euler method.Then I calculate the natural logarithms of the separation of two billiards which are separated only a tiny distance at the beginning of the motion.This shows the sensitivity of initial value of the system, and obliquely prove that this system is a chaotic system.

---
#Background
A billiard is a dynamical system in which a particle alternates between motion in a straight line and specular reflections from a boundary. When the particle hits the boundary it reflects from it without loss of speed. Billiard dynamical systems are Hamiltonian idealizations of the game of billiards, but where the region contained by the boundary can have shapes other than rectangular and even be multidimensional. Dynamical billiards may also be studied on non-Euclidean geometries; indeed, the very first studies of billiards established their ergodic motion on surfaces of constant negative curvature. The study of billiards which are kept out of a region, rather than being kept in a region, is known as outer billiard theory.

The motion of the particle in the billiard is a straight line, with constant energy, between reflections with the boundary (a geodesic if the Riemannian metric of the billiard table is not flat). All reflections are specular: the angle of incidence just before the collision is equal to the angle of reflection just after the collision. The sequence of reflections is described by the billiard map that completely characterizes the motion of the particle.

Billiards capture all the complexity of Hamiltonian systems, from integrability to chaotic motion, without the difficulties of integrating the equations of motion to determine its Poincaré map. Birkhoff showed that a billiard system with an elliptic table is integrable.

.
![1](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/Excercise_08_additional_pics/1.png)
![2](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/Excercise_08_additional_pics/2.png)
![3](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/Excercise_08_additional_pics/3.png)
![4](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/Excercise_08_additional_pics/4.jpg)
![5](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/Excercise_08_additional_pics/5.jpg)

---
##Main text
The trajectories of the billiard are calculated by the formula:
![6](http://latex.codecogs.com/gif.latex?v_%7Bi%2C%5Cperp%20%7D%3D%28v_i%20%5Ccdot%20%5Chat%20n%29%5Chat%20n%20%5C%5C%20v_%7Bi%2C%5Cparallel%20%7D%20%3D%20v_i%20-%20v_%7Bi%2C%5Cperp%7D%20%5C%5C%20v_%7Bf%2C%5Cperp%7D%3D-v_%7Bi%2C%5Cperp%20%7D%5C%5C%20v_%7Bf%2C%5Cparallel%20%7D%20%3Dv_%7Bi%2C%5Cparallel%20%7D)

Then I calculated the natural logarithms of the separation of the positions of the two billiard for different alpha.
![7](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/1.png)
![8](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/2.png)
![9](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/3.png)
![10](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/4.png)
![11](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/5.png)
![12](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/6.png)
.
![13](http://latex.codecogs.com/gif.latex?%5Calpha%20%3D%200.01%20%5Cquad%20%5Clambda%20%3D%200.051)
.
![14](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/7.png)
![15](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/8.png)
![16](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/9.png)
![17](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/10.png)
![18](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/11.png)
![19](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/12.png)
.
![20](http://latex.codecogs.com/gif.latex?%5Calpha%20%3D%200.001%20%5Cquad%20%5Clambda%20%3D%200.000479)
.
![21](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/13.png)
![22](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/14.png)
![23](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/15.png)
![24](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/16.png)
![25](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/17.png)
![26](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_09/18.png)
.
![27](http://latex.codecogs.com/gif.latex?%5Calpha%20%3D%200.05%20%5Cquad%20%5Clambda%20%3D%200.0600)

We can see from the plots that:

+ For different alpha, the spaces between the two dips are different.Lower alpha, minor spaces.
+ For different initial distance, the curves are also different. And so the Lyapunov exponent are also different.

---
##Acknowledgement
+ Thanks for the author's systematic guidence in the book.
+ Thanks for the Bing search engine for providing the image in this assignment.




