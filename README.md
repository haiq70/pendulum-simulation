# pendulum-simulation
This project is my, rather casual, attempt at simulating the motion of an ideal pendulum.
It utlizes VPython, a 3D graphics module for Python.

To compute the motion, the following parametric equations were used:

x = L*sin(theta)
y = -L*cos(theta)

where L is the length of the string (input by the user) and theta is the current spatial deviation:

theta = theta0 * sin(sqrt(g/l) * t)

where theta0 is the maximum spatial deviation (input by the user) and t is time.

The numerical solution required employing a time step (dt). I opted for a 0.01 interval, which combined with
VPython's rate() function, which defines how many times an operation can be performed per second. 
rate(100) gives 100 times/s, which yields real-time for the animation:

100 * 0.01 (dt) = 1 [s]


//Jakub Kwaśniak (haiq70)
