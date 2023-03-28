import numpy as np
from spatialmath import *
import roboticstoolbox as rtb
from roboticstoolbox.tools.trajectory import *
from roboticstoolbox.backends.swift import Swift

def zadanie_3():
    robot= rtb.models.Panda()
    tab=[[0,0,0,0,0,0,0]]
    T1 = SE3(0.75, 0.2, 0.15)* SE3.OA([1, 0, 0], [0, 0, -1])
    x=0.75
    y=0.2
    solution = robot.ikine_LM(T1)
    while(x>0.65):

        T = SE3(x,y, 0.15)* SE3.OA([1, 0, 0], [0, 0, -1])
        solution=robot.ikine_LM(T)
        #print(solution.q)
        tab.append(solution.q)
        x = x-0.01
        y = math.sqrt(0.01-(x-0.65)**2)+0.2
        x**2+y**2-0.01

    x=0.65
    y=0.3
    while(x>0.56):
        T = SE3(x,y, 0.15)* SE3.OA([1, 0, 0], [0, 0, -1])
        solution=robot.ikine_LM(T)
        #print(solution.q)
        tab.append(solution.q)
        x = x-0.01
        y = math.sqrt(0.01-(x-0.65)**2)+0.2

    x=0.55
    y=0.2
    while (x < 0.74):
        T = SE3(x, y, 0.15) * SE3.OA([1, 0, 0], [0, 0, -1])
        solution = robot.ikine_LM(T)
        #print(solution.q)
        tab.append(solution.q)
        x = x + 0.01
        y = -(math.sqrt(0.01 - (x - 0.65) ** 2)) + 0.2

    T1 = SE3(0.75, 0.2, 0.15)* SE3.OA([1, 0, 0], [0, 0, -1])
    solution = robot.ikine_LM(T1)
    tab.append(solution.q)

    via_pt = np.array(tab)
    traj = mstraj(via_pt, dt=0.02, tacc=0.01, qdmax=5.0)
    #rtb.xplot(traj.q, block=True)
    robot.plot(traj.q,backend='swift',loop=True)


if __name__ == '__main__':
    zadanie_3()