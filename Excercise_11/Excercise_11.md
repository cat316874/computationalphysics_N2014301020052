# Excercise_11

标签（空格分隔）： 计算物理

---

#Abstract
This is a project that uses a simple approximation of the spin motion of the Saturn's moon Hyperion.
Due to it's special shape and mass distribution, the spin motion of Hyperion exhibit the chaotic feature and thus the spin and orbital motion are not sychronized.

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/saturn.jpg)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/hyperion.jpg)

---
#Background
Hyperion is the largest of Saturn's irregular, nonspherical moons. Hyperion's mean radius is 83.9 miles (135 km), but since Hyperion is rather potato-shaped, its shape can be described in terms of its diameter along its three axes: 255 x 163 x 137 miles (410 x 260 x 220 km, respectively). Considering its odd shape, Hyperion is probably a remnant of a larger moon that was destroyed by a major impact.

Hyperion's density is slightly more than half that of water. This could be due to water ice with gaps (porosity) of more than 40 percent. Also, lighter materials, such as frozen methane or carbon dioxide, could make up part of Hyperion. This is consistent with the concept of Hyperion accreting from a number of smaller ice and rock bodies, but not having enough gravity to compact them. Thus, Hyperion might be similar to a large rubble pile.

##Orbit
Hyperion rotates chaotically, tumbling unpredictably through space as it orbits Saturn. Hyperion orbits at a mean distance of 933,000 miles (1,500,000 km) from Saturn in an eccentric orbit. This contributes to variations in the spin or rotation of Hyperion. A stronger effect on Hyperion's rotation is that it is in resonance with Saturn's largest moon, Titan, which orbits at 759,200 miles (1,221,850 km). Thus, the two objects speed up and slow down as they pass each other in a complex set of variations. Because Hyperion is much smaller than Titan, its rotation and orbit are affected vastly more than the larger moon, and Titan apparently keeps the Hyperion orbit eccentric rather than growing more circular over time.

The great distance from Saturn and resonance with Titan has also kept Hyperion from becoming tidally locked facing Saturn. Hyperion rotates roughly every 13 days during its 21-day orbit.

##Surface Features
The most noticeable close-up feature of Hyperion is its deeply cratered surface. Hyperion and its sister outer moons, Phoebe and Iapetus, all show extensive cratering because they are Saturn's most distant moons and have experienced very little tidal warming that might blur or erase earlier features. However, the Hyperion craters are particularly deep and do not have significant rays of ejecta (although there appears to have been slumping or landslides inside many of the bigger craters). The result is a curiously punched-in look, somewhat like the surface of a sponge or a wasp nest. Planetary geologists have theorized that Hyperion's high-porosity and low density would crater more by compression than excavation.

Many of the crater walls on Hyperion are bright, which suggests an abundance of water ice. The crater floors are mostly the areas of the lowest albedo (a measure of how reflective the surface is) and greatest red coloration. This may be because the average temperature of roughly -300 degrees Fahrenheit (-180 degrees Celsius) might be close enough to a temperature that would cause volatiles to sublimate, leaving the darker materials accumulated on the crater floors. This scenario fits with some of the newer crater floors being bright water ice.

##Discovery
William Lassell discovered Hyperion in 1848. That same year William Cranch Bond, with his son George Phillips Bond, independently discovered the moon. All three men are jointly credited with the discovery.

##How Hyperion Got its Name
John Herschel suggested that the moons of Saturn be associated with the mythical brothers and sisters of Kronus. (Kronus is the equivalent of the Roman god Saturn in Greek mythology.)

The name Hyperion comes from the Greek god (or Titan) Hyperion (he who watches over). Hyperion, the son of Uranus and Gaia, is a brother of Kronus and the husband of Thea. The children of Hyperion and Thea include Helios (the sun), Eos (the dawn) and Selene (the Moon).

Astronomers also refer to Hyperion as Saturn VII. The International Astronomical Union now controls the naming of astronomical bodies.

![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/hyperion_surface.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/hyperion_parameter.png)

---
#Main text
First we treat the mass distribution of the Hyperion as the dumbbell, and the spin motion is due to the gravity exerted on the two ball,so we have:

---
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Comega%7D%7Bdt%7D%5Capprox%20-%20%5Cfrac%7B3GM_%7BSat%7D%7D%7Br_c%5E5%7D%28x_csin%5Ctheta-y_ccos%5Ctheta%29%28x_ccos%5Ctheta&plus;y_csin%5Ctheta%29)

---
combined with

---
![](http://latex.codecogs.com/gif.latex?v_1%3D%5Csqrt%7B%5Cfrac%7BGM_%7BSat%7D%281-e%29%7D%7Ba%281&plus;e%29%7D%7D%3D%5Csqrt%7BGM_%7BSat%7D%281-e%29%7D)

---
We can construct our program using the Euler-Cromer method.

Here are the out comes:

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/1.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/2.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/3.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/4.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/5.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/6.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/7.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/8.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/9.png)

---
+ For different initial value, the motion of the circular orbit is regular and non-chaotic.
+ For different initial value, the motion of the elliptical orbit is irregular and chaotic.

---
Also, the chaotic feature of the motion of elliptical orbit can be shown by calculation the angle difference for two motions with an initial angle difference of merely 0.01.

Here are the result for differnt eccentricity:

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-1.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-2.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-3.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-35.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-36.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-37.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-38.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-39.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-4-10.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-4-3.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-5-10.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-5-25.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/e-6.png)

---
+ It is easy to notice that for low eccentricities, the motion resembles the circular motion and the re are no Lyapunov exponent to be calculated.
+ For the case of eccentricity - 0.35~0.4 , the exponential increasing area is rather obvious and we can calculated them.
+ But there is no certain ditermination relationship between the eccentricity and the Lyapunov exponent.
+ Also, the motion exhibit a chaotic feature starting from the eccentricity of 0.3.

---
Following the path developped in the earlier chapter, we can plot the curves in the phase space and construct the Poincare section by selecting the points in the phase space near the period of the orbital motion.

Here are the results:

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-001.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-003.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-01.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-02.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-03.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-0355.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-0357.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-036.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-04.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-05.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-06.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-07.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-08.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-09.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/ps-099.png)

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/poincare-03.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/poincare-0355.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/poincare-0357.png)
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/poincare-099.png)

---
+ The phase space for different value of eccentricity exhibit a grudual change process.
+ For high value of the eccentricity the points in the phase space concentrate on several lines, this maybe means that certain value of the angular velocity are in priority.
+ It is rather interesting that the Poincare section for certain value of the eccentricity is rather ragular in an oval shape, however, I'm not able to explain why.

---
#When talking about Hyperion...
##I will first think about _the Hyperion Cantos_:

---
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/hyperion_cantos.gif)

First published in 1989, Hyperion has the structure of a frame story, similar to Geoffrey Chaucer's Canterbury Tales and Giovanni Boccaccio's Decameron. The story weaves the interlocking tales of a diverse group of travelers sent on a pilgrimage to the Time Tombs on Hyperion. The travelers have been sent by the Church of the Final Atonement, alternately known as the Shrike Church, and the Hegemony (the government of the human star systems) to make a request of the Shrike. As they progress in their journey, each of the pilgrims tells their tale.

---
##And maybe think of this...
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/hyperion_computer.jpg)

---
##Or this?...
![](https://github.com/Rob1nTian/computationalphysics_N2014301020052/blob/master/Excercise_11/hyperion_ship.jpg)

---
#Acknowledgement
+ Thank Kang Yu for a very helpful guidance.
+ Thank the author for the systematic guidance.




