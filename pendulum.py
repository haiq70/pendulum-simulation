# representation of an (ideal) pendulum using VPython 3D graphics module   //haiq70
# vpython documentation: https://www.glowscript.org/docs/VPythonDocs/index.html

import numpy as np
import vpython as vp


# INITIALISE VARIABLES
isRunning = False                           # defines start/stop of the animation
g = 9.81                                    # gravitational acceleration
length = 3                                  # default length of the string (3 meters)
period = 2 * np.pi * np.sqrt(length / g)    # period of oscillation to be displayed
timer = 0                                   # total time (timer + dt) for computations


# DEFINE FUNCTIONS
def start_button_clicked():
    global isRunning
    isRunning = True
    return 0


def pause_button_clicked():
    global isRunning
    isRunning = False
    return 0


def get_theta(s):
    theta_output.text = s.value


def get_length(s):
    length_output.text = s.value


# SET THE SCENE AND 3D OBJECTS
scene = vp.canvas(width=500, height=400, userspin=False, userzoom=False,
                  title="Ideal Pendulum Simulation by haiq70", autoscale=False,
                  center=vp.vector(0, -3, 0))
bob = vp.sphere(pos=vp.vector(0, -length, 0), radius=0.5)
string = vp.cylinder(pos=vp.vector(0, 0, 0), axis=vp.vector(0, -length, 0), radius=0.02)

# BUTTONS
vp.button(bind=start_button_clicked, text='Start')
vp.button(bind=pause_button_clicked, text='Pause')
scene.append_to_caption('\n\n')

# SLIDER (SPATIAL DEVIATION)
scene.append_to_caption("Spatial deviation: ")
slider_sd = vp.slider(min=0.1, max=90, bind=get_theta, step=0.1, value=5)
theta_output = vp.wtext(text=slider_sd.value)
scene.append_to_caption(" \u00b0 \n")


# SLIDER (LENGTH OF THE STRING)
scene.append_to_caption("Length of the string: ")
slider_l = vp.slider(min=0.1, max=10, bind=get_length, step=0.1, value=3)
length_output = vp.wtext(text=slider_l.value)
scene.append_to_caption(" m\n\n")


# TEXT OUTPUT
# period
scene.append_to_caption("Period [T] = ")
period_output = vp.wtext(text=period)
scene.append_to_caption(" s\n")
# frequency
scene.append_to_caption("Frequency [f] = ")
f_output = vp.wtext(text=1/period)
scene.append_to_caption(" Hz\n")
# angular frequency
scene.append_to_caption("Angular frequency [\u03c9] = ")
ang_output = vp.wtext(text=(2*np.pi)/period)
scene.append_to_caption(" rad/s\n")


# MAIN PROGRAM LOOP
while True:
    theta = np.deg2rad(slider_sd.value)        # read the current value from the slider
    length = slider_l.value
    x_max = length * np.sin(theta)
    y_max = -length * np.cos(theta)
    period = 2 * np.pi * np.sqrt(length / g)
    period_output.text = '{:1.5f}'.format(period)         # update the: period output,
    f_output.text = '{:1.5f}'.format(1/period)            # frequency output,
    ang_output.text = '{:1.5f}'.format((2*np.pi)/period)  # angular frequency output.

    while bob.pos.x <= x_max and bob.pos.y <= y_max and isRunning:
        vp.rate(100)
        theta1 = theta * np.sin(np.sqrt(g/length) * timer)
        bob.pos.x = length * np.sin(theta1)
        string.axis.x = bob.pos.x
        bob.pos.y = -length * np.cos(theta1)
        string.axis.y = bob.pos.y
        timer = timer + 0.01

    # reset the coordinates
    bob.pos.x = 0
    string.axis.x = 0
    bob.pos.y = -length
    string.axis.y = -length
