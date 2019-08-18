"""
Problem 1: fireworks.py

This module implements a fireworks that is drawn onto a tkinter canvas.

Authors:
    Lennart Elbe <lenni.elbe@gmail.com>

.. _`Python Standard Library`:
    https://docs.python.org/3.7/library
    _Lecture
    https://proglang.informatik.uni-freiburg.de/teaching/info1/2018/lecture/infoI12.pdf

Authors:
    Tim Schulte
    Thorsten Engesser

With modifications by: Lennart Elbe (Student)

Version:
    WS 2018/19

"""


import tkinter
from sys import modules
from math import sin, cos
from random import choice, uniform
from time import time, sleep

GRAVITY = 30  # you can play around with this if you want


class Particle:
    """Generic class for particles.

    Particles can be emitted by Fireworks objects. They are displayed for a
    specified lifespan and then removed from the canvas.

    Attributes:
        cv (Tk.canvas): the canvas in which the particle is drawn.
        cid (Tk.canvas): the tkinter canvas id for the particle.
        x (float): x-coordinate of the particle.
        y (float): y-coordinate of the particle.
        vx (float): x-velocity of the particle (in pixels per second).
        vy (float): y-velocity of the particle (in pixels per second).
        color (str): color of the particle.
        age (float): age of the particle.
        lifespan (float): lifespan of the particle (in seconds).

    """

    def __init__(self, cv=None, color='white', x=0., y=0.,
                 vx=0., vy=0., lifespan=5.):
        """Init Particle objects.

        Args:
            cv (Tk.canvas): the canvas in which the particle is drawn.
            x (float): x-coordinate of the particle.  Defaults to 0.0.
            y (float): y-coordinate of the particle.  Defaults to 0.0.
            vx (float): x-velocity of the particle (in pixels per second).
                Defaults to 0.0.
            vy (float): y-velocity of the particle (in pixels per second).
                Defaults to 0.0.
            color (str): color of the particle.  Defaults to 'white'.
            lifespan (float): lifespan of the particle (in seconds).
                Defaults to 5.0.

        """
        self.cv = cv
        self.cid = None
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.color = color
        self.age, self.lifespan = 0, lifespan

    def update(self, dt):
        """Update position and velocity after dt seconds have passed.

        Args:
            dt (float): the time that has passed after the last update (in s).

        """
        self.age += dt
        if self.alive():
            self.vy += GRAVITY * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.cv.move(self.cid, self.vx * dt, self.vy * dt)
        elif self.cid is not None:
            cv.delete(self.cid)
            self.cid = None

    def alive(self):
        """Check if particle is still within its lifespan."""
        return self.age <= self.lifespan


class SquareParticle(Particle):
    """A Particle with a quadratic shape"""

    def __init__(self, x=0., y=0., size=2., **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.cid = self.cv.create_polygon(
            x - size, y - size, x + size, y - size,
            x + size, y + size, x - size, y + size,
            fill=self.color)


class TriangleParticle(Particle):
    """A Particle with a triangular shape"""

    def __init__(self, x=0., y=0., size=2., **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.cid = self.cv.create_polygon(
            x - size, y - size, x + size,
            y - size, x, y + size,
            fill=self.color)


class CircularParticle(Particle):
    """A Particle with a circular shape."""

    def __init__(self, x=0., y=0., size=2., **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color)


class Fireworks:
    """Generic class for fireworks.

    The main "behavior" of a fireworks is specified via its update method.
    E.g., new particles can be emitted and added to the particle list. The
    Fireworks base class automatically updates all particles from the particle
    list in its update method.

    Attributes:
        cv (Tk.canvas): the canvas in which the fireworks is drawn.
        age (float): age of the fireworks.
        particles (list of Particle): list of generated particles.

    """

    def __init__(self, cv=None):
        """Init Fireworks objects.

        Args:
            cv (Tk.canvas): the canvas in which the particle is drawn.

        """
        self.cv = cv
        self.age = 0
        self.particles = []

    def update(self, dt):
        """Update the fireworks' particles and remove dead ones.

        Args:
            dt (float): the time that has passed after the last update (in s).

        """
        self.age += dt
        for p in self.particles:
            p.update(dt)
        for i in range(len(self.particles) - 1, -1, -1):
            if not self.particles[i].alive():
                del self.particles[i]


class Rocket(Fireworks):
    #  rocket objects need position, speed, and time

    def __init__(self, cv, x, pps, colors, pos, speed, timer, angle=0.25):
        """Shoots a rocket into the sky which then explodes.
        
        Arguments:
            cv {idontknow} -- the canvas upon which this wonderful display
                is painted
            x {int} -- the position of the rocketrocket
            pps {int} -- pixels per second (the speed of the particles)
            colors {str} -- the color of the particles
            pos {int} -- the position of the new rocket from the old rocket
            speed {int} -- used to help calculate the x and y velocities of
                the particles
            timer {int} -- the length of time which passes before a rocket
                explodes!!!

        Keyword Arguments:
            angle {float} -- [The angle at which the rocket particles are
                ejected] (default: {0.25})
        """

        super().__init__(cv)
        #self.cid = cv.create_polygon(x - 12, 530,  # size and color are fixed
        #                             x + 12, 530,  # (could be parametrized)
        #                            x 500,
        #                           fill="red")
        self.y = 500
        if isinstance(x, list) and len(x) > 1:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
        self.pps = pps
        self.colors = colors
        self._tospawn = 0
        self._pos = pos
        self._speed = speed
        self._timer = timer
        self._time = 0
        self._done = False
        self._doneDone = False
        self._angle = angle

    def update(self, dt):
        """Continuously emits new random particles and updates them.

        Args:
            dt (float): the time that has passed after the last update (in s).

        """
        super().update(dt)
        self._tospawn += self.pps * dt
        color = self.colors[int(self.age*20) % len(self.colors)]
        #print(int(self.age*20) % len(self.colors))
        #print(self._time)
        self._time += dt
        
        ptype = TriangleParticle
        angle = uniform(-self._angle, self._angle)
        speed = -uniform(120.0, 150.0)
        vx = sin(angle) * speed
        vy = cos(angle) * speed
        if not self._done:
            self.particles.append(
                ptype(cv=self.cv, x=self.x, y=self.y, color=color, vx=vx, vy=vy))
            self._done = True
        #print("TIME IS: " + str(self._time) + "AND TIMER IS: " + str(self._timer))
        if (self._time > self._timer) and not self._doneDone:
            #print("ASDKLJHDKJSHLGJKAHGLKFAJHGKLJFDHG;FKLJHAFDGS;KL")
            xt = self.particles[0].x
            yt = self.particles[0].y
            self._doneDone = True
            for i in range(int(self._tospawn)):
                ptype = choice(
                    [SquareParticle, TriangleParticle, CircularParticle])
                angle = uniform(-3.14, 3.14)
                speed = -uniform(80.0, 120.0)
                vx = sin(angle) * speed
                vy = cos(angle) * speed
                self.particles.append(
                    ptype(cv=self.cv, x=xt, y=yt, color=color, vx=vx, vy=vy, lifespan=1))
        self._tospawn -= int(self._tospawn)


class RocketRocket(Fireworks):
    #  rocket objects need position, speed, and time

    def __init__(self, cv, x, pps, colors, pos, speed, timer):
        """A rocketrocket shoots a rocket and explodes and then those
        particles are in and of themselves also rockets!
        
        Arguments:
            cv {idontknow} -- the canvas upon which this wonderful display
            is painted
            x {int} -- the position of the rocketrocket
            pps {int} -- pixels per second (the speed of the particles)
            colors {str} -- the color of the particles
            pos {int} -- the position of the new rocket from the old rocket
            speed {int} -- used to help calculate the x and y velocities of
            the particles
            timer {int} -- the length of time which passes before a rocket explodes!!!
        """


        super().__init__(cv)
        
        self.x = x
        self.pps = pps
        self.colors = colors
        self._tospawn = 0
        self._pos = pos
        self._speed = speed
        self._timer = timer
        self._time = 0
        self._done = False
        self._doneDone = False

    def update(self, dt):
        """Continuously emits new random particles and updates them.
        
        Unique to RocketRocket because instead of emmiting particles
            it emmits more rockets!!! EXPLOSIONS!!!
        Args:
            dt (float): the time that has passed after the last update (in s).

        """
        super().update(dt)
        self._tospawn += self.pps * dt
        color = self.colors[int(self.age*20) % len(self.colors)]
        #print(int(self.age*20) % len(self.colors))
        #print(self._time)
        self._time += dt

        ptype = TriangleParticle
        angle = uniform(-0.25, 0.25)
        speed = -uniform(120.0, 150.0)
        vx = sin(angle) * speed
        vy = cos(angle) * speed
        if not self._done:
            self.particles.append(
                ptype(cv=self.cv, x=self.x, y=500, color=color, vx=vx, vy=vy))
            self._done = True
        #print("TIME IS: " + str(self._time) + "AND TIMER IS: " + str(self._timer))
        if (self._time > self._timer) and not self._doneDone:
            # now explode
            xt = self.particles[0].x
            yt = self.particles[0].y
            self._doneDone = True
            for i in range(int(self._tospawn)):
                r = Rocket(self.cv, [xt, yt], 1000, [
                           'red', 'blue', 'yellow', 'chartreuse2'], [500, 500], 3, 1.5, 3.14)
                entities.append(r)
        self._tospawn -= int(self._tospawn)


class RocketRocketLauncher(Fireworks):
    def __init__(self, cv, pos):
        """Barrages the skies with a relentless series of badass explosions.
        (repetadly executes RocketRocket)
        
        Arguments:
            cv {idontknow} -- the canvas upon which this wonderful display
            pos {int} -- the position of the new rocket from the old rocket
        """

        super().__init__(cv)
        # we want a new rocket after that many seconds
        self._nextrocket = 0
        self._time = 0
        self._cv = cv
        self._pos = pos

    def update(self, dt):
        """adds RocketRocket objects to entities list and executes update(dt)
        which makes the rockets all move.
        
        Arguments:
            dt {int} -- Change in time.
        """

        super().update(dt)
        self._time = self._time + dt
        if self._time > self._nextrocket:
            # feuere eine neue Rackte ab
            r = RocketRocket(self._cv, self._pos, 1000, [
                       'red', 'blue', 'yellow', 'chartreuse2'], [500, 500], 3, 3)
            entities.append(r)
            self._nextrocket = self._time + uniform(1, 5)


class RocketLauncher(Fireworks):
    def __init__(self, cv, pos):
        """Used to fire rockets into the sky at random intervals.
        
        Arguments:
            cv {idontknow} -- the canvas upon which this wonderful display
            pos {int} -- the position of the new rocket from the old rocket
        """

        super().__init__(cv)
        # we want a new rocket after that many seconds
        self._nextrocket = 0
        self._time = 0
        self._cv  = cv
        self._pos = pos

    def update(self, dt):
        """Adds rocket objects to the entities list which causes them to be
            updated when update is executed.
        
        Arguments:
            dt {int} -- change in time
        """

        super().update(dt)
        self._time = self._time + dt
        if self._time > self._nextrocket:
            # feuere eine neue Rackte ab
            r = Rocket(self._cv, self._pos, 1000, ['red', 'blue', 'yellow', 'chartreuse2'], [500, 500], 3, 3)
            entities.append(r)
            self._nextrocket = self._time + uniform(1,2)


class Volcano(Fireworks):
    """A volcano that continuously emits colored particles.

    Attributes:
        x (float): x-coordinate of the volcano.
        pps (float): the number of particles to spawn per second.
        colors (list of string): the colors of the particles to spawn.

    """

    def __init__(self, cv, x, pps, colors):
        """Init Volcano objects.

        Args:
            cv (Tk.canvas): the canvas in which the particle is drawn.
            x (float): x-coordinate of the volcano.
            pps (float): the number of particles to spawn per second.
            colors (list of string): the colors of the particles to spawn.

        """
        super().__init__(cv)
        self.cid = cv.create_polygon(x - 12, 530,  # size and color are fixed
                                     x + 12, 530,  # (could be parametrized)
                                     x, 500,
                                     fill="red")
        self.x = x
        self.pps = pps
        self.colors = colors
        self._tospawn = 0

    def update(self, dt):
        """Continuously emits new random particles and updates them.

        Args:
            dt (float): the time that has passed after the last update (in s).

        """
        super().update(dt)
        self._tospawn += self.pps * dt
        color = self.colors[int(self.age / 3) % len(self.colors)]
        for i in range(int(self._tospawn)):
            ptype = choice(
                [SquareParticle, TriangleParticle, CircularParticle])
            angle = uniform(-0.25, 0.25)
            speed = -uniform(80.0, 120.0)
            vx = sin(angle) * speed
            vy = cos(angle) * speed
            self.particles.append(
                ptype(cv=self.cv, x=self.x, y=500, color=color, vx=vx, vy=vy))
        self._tospawn -= int(self._tospawn)


def mainloop(cv, entities):
    """Fireworks main loop."""
    t, dt = time(), 0
    while running:
        sleep(max(0.01 - dt, 0))
        tnew = time()
        t, dt = tnew, tnew - t
        for e in entities:
            e.update(dt)
        cv.update()


def close(*ignore):
    """Stops simulation loop and closes the window."""
    global running
    running = False
    root.destroy()


if __name__ == '__main__':
    root = tkinter.Tk()
    cv = tkinter.Canvas(root, height=600, width=800)
    cv.create_rectangle(0, 0, 800, 600, fill="midnight blue")
    cv.create_rectangle(0, 450, 800, 600, fill="gray11")
    cv.pack()

    entities = [
        Volcano(cv, 400, 100, ['red', 'orange', 'yellow', 'chartreuse2']),
        Rocket(cv, 200, 100, ['red', 'blue', 'yellow', 'chartreuse2'], [500, 500], 2, 3),
        RocketLauncher(cv, 200),
        RocketRocket(cv, 500, 100, ['red', 'blue',
                                     'yellow', 'chartreuse2'], [500, 500], 3, 3),
        RocketRocketLauncher(cv, 500),
    ]
    # close window with [ESC] or (x) button
    root.bind('<Escape>', close)
    root.protocol("WM_DELETE_WINDOW", close)
    running = True
    root.after(300, mainloop, cv, entities)
    if 'idlelib' not in modules:
        root.mainloop()