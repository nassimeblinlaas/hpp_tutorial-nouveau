
from hpp.corbaserver import * 

from hpp.corbaserver.nassime import RobotStrange
robot = RobotStrange ('robot_strange', True)

robot.setJointBounds ("base_joint_xyz", [-2, 2, -1.5, 1.5, -3, 2])#pour les petits meshs
robot.tf_root = 'base_link'

from hpp.corbaserver import ProblemSolver
ps = ProblemSolver (robot)
from hpp.gepetto import Viewer
v = Viewer (ps)

q_init = robot.getCurrentConfig ()
q_goal = q_init [::]
#q_init [0:7] = [0, 0, 2, 0, 0, 0, 1]
q_init [0:3] = [0,0,2]
v (q_init)
#q_goal[0:7]=[0,0,-2,0,0,0,1]
q_goal [0:3] = [0,0,-2]
v (q_goal)
q_init [0:3] = [0,0,0]
v (q_init)

v.loadObstacleModel ("iai_maps", "env_tore", "simple")

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)
ps.clearRoadmap()

ps.selectPathPlanner("interactive")

white=[1.0,1.0,1.0,1.0]
brown=[0.85,0.75,0.15,0.5]
black=[0, 0, 0, 1]     
ps.addPathOptimizer ("RandomShortcut")
v.solveAndDisplay("rm1",1,white,0.00,1,black)
#ps.solve()

from hpp.gepetto import PathPlayer
pp = PathPlayer (robot.client, v)
v(q_goal)
pp (0)
#pp (1)