from hpp.corbaserver import * 

from hpp.corbaserver.nassime import RobotChaine
robot = RobotChaine ('robot_chaine', True)

robot.setJointBounds ("base_joint_xyz", [-4, 12, -4, 12, -2, 4])
robot.tf_root = 'base_link'

from hpp.corbaserver import ProblemSolver
ps = ProblemSolver (robot)
from hpp.gepetto import Viewer
v = Viewer (ps)

q_init = robot.getCurrentConfig ()
q_goal = q_init [::]
q_init [0:3] = [1, 2, 1]
q_goal [0:3] = [9.15, 7.5, 0.5]

v.loadObstacleModel ("iai_maps", "env_simple", "simple")

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)
ps.clearRoadmap()

ps.selectPathPlanner("interactive")

white=[1.0,1.0,1.0,1.0]
brown=[0.85,0.75,0.15,0.5]
ps.addPathOptimizer ("RandomShortcut")
v.solveAndDisplay("rm1",50,white,0.05,1,brown)
#ps.solve()

from hpp.gepetto import PathPlayer
pp = PathPlayer (robot.client, v)
v(q_goal)
pp (0)
pp (1)


