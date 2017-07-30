#!/usr/bin/env python3

import math
import sys

import direct.showbase.ShowBase
import direct.task
import direct.actor.Actor
import direct.interval.IntervalGlobal
from panda3d.core import Point3
from p3id import streambuffer

class MyApp(direct.showbase.ShowBase.ShowBase):
    def __init__(self):
        # Squalch libpanda.so stderr writes
        with streambuffer.StreamBuffer(sys.stderr) as streambuf:
            super(MyApp, self).__init__()

        self.__init_scene__()
        self.__init_camera__()


    def __init_scene__(self):
        """ Load the environment model.
        """
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.__init_actors__()


    def __init_actors__(self):
        self.__init_actor_panda__()


    def __init_actor_panda__(self):
        """ Load and transform the panda actor.
        """
        self.panda_actor = direct.actor.Actor.Actor(
            "models/panda-model",
            {"walk": "models/panda-walk4"}
        )
        self.panda_actor.setScale(0.005, 0.005, 0.005)
        self.panda_actor.reparentTo(self.render)
        # Loop its animation.
        self.panda_actor.loop("walk")

        """ Create the four lerp intervals needed for the panda to
            walk back and forth.

            Create and play the sequence that coordinates the intervals.
        """
        self.panda_pace = direct.interval.IntervalGlobal.Sequence(
            self.panda_actor.posInterval(13, Point3(0, -10, 0), startPos=Point3(0, 10, 0)),
            self.panda_actor.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0)),
            self.panda_actor.posInterval(13, Point3(0, 10, 0), startPos=Point3(0, -10, 0)),
            self.panda_actor.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0)),
            name="panda_pace"
        )
        self.panda_pace.loop()


    def __init_camera__(self):
        """ Add the spinCameraTask procedure to the task manager.
        """
        self.taskMgr.add(self.spin_camera_task, "spin_camera_task")


    def spin_camera_task(self, task):
        """ Define a procedure to move the camera.
        """
        angle_degrees = task.time * 1.0
        angle_radians = angle_degrees * (math.pi / 180.0)
        self.camera.setPos(
            20 * math.sin(angle_radians),
            -20.0 * math.cos(angle_radians),
            3,
        )
        self.camera.setHpr(angle_degrees, 0, 0)
        return direct.task.Task.cont


    @staticmethod
    def __main__(argp=None):
        self = MyApp()
        self.run()


main = MyApp.__main__


if __name__ == '__main__':
    main()


