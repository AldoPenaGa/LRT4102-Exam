<p align="center">
  <h2 align="center"> Design of Robotics Systems (LRT4102): Exam </h2>

  <p align="justify">
  The "Exam on the Design of Robotic Systems" (LRT4102) is presented. The exam will utilize methods and tools employed throughout the course and will be carried out within the Robot Operating System (ROS) environment. "Turtlesim" will be used, where turtles will appear randomly, with one following the other.
    
  <br>Universidad de las Américas Puebla (UDLAP) - Guided by professor Dr. César Martínez Torres. "https://www.linkedin.com/in/c%C3%A9sar-martinez-torres-617b5347/?originalSubdomain=mx>" 
  </p>
</p>
<be>

## Table of contents
- [Introduction](#introduction)
- [Problems](#problems)
- [Codes](#codes)
- [Results](#results)
- [Conclusion](#conclusion)
- [Contributors](#codes)

<div align= "justify">

### Introduction

The exam was developed by Aldo Peña, Charbel Breidy, Enrique Rocha, and Joan Monfil, students of Robotics and Telecommunications Engineering at Universidad de las Américas Puebla (UDLAP). It presents a general overview of ROS for hardware and software management, using algorithms designed to use Euclidean geometry approach with a certain defined distance and angles. This enables the random spawning of turtles using the "Turtlesim" tool. One turtle will follow the other turtle to its spawning position once it reaches the target position, the static turtle is killed and another one appears in another random position so the process can be repeated. The Turtlesim and PID control tools are used to study the complex process of guiding a robotic structure to its chosen destination with precision and speed, while employing Euclidean distances to ensure the robot can accomplish this with minimal difficulties.

**ROS** 

ROS is an open-source platform designed for robots, simplifying the development of robotic applications. Its primary function is to manage hardware, execute control algorithms, and facilitate communication between different software components. Additionally, it utilizes various tools, including "Turtlesim".


**Turtlesim**

A simulation software extension that presents a turtle-shaped robot. This robot can be controlled with Python scripts or the command line. It allows for assigning specific positions, creating shapes, and tracing routes towards points of interest.


**Euclidean Distances**

Euclidean distances are a measure of the distance between two points in a predetermined Euclidean space. Essentially, it is the length of the straight line between points "A" and "B" where the aim is to join these two points on a plane. In a two-dimensional Euclidean space, such as an XY plane, the Euclidean distance between two points:

P1 (x1, y1)
P2 (x2, y2)

...is calculated using the Pythagorean theorem:

C = √ (x2-x1)² + (y2-y1)²

This can be generalized to Euclidean spaces of any number of dimensions. This method is used in data science, computer science, physics, and engineering.

**DTG**

Refers to the direct Euclidean distance from a robot's current position to a point of interest. It is the length of the straight line connecting the current point with the desired point, all within the Euclidean space.

**ATG**

The angle required for the robot to orient itself from its current position toward the target point of interest, used to determine the angle between the line connecting the current position and the target, and the robot's reference axis.


### Problem

A turtle is spawned at a random location within the Euclidean space, with randomized X, Y. Similarly, another turtle will appear at the center and will attempt to reach the location of the second turtle. Upon arrival, the first turtle is killed. Then a new turtle will spawn at a random position and the task will be repeated.


### Code

The exame.py contains the code for the exam. It has to be run with:

`roscore`

`rosrun turtlesim turtlesim_node`

Then go to the location where the python script was downloaded and execute:

`python3 exame.py`

One important aspect to mention is that even though it is done in loop, after some repetitions (generally three), any key except `e` will let it continue. 

### Conclusion
In short, we have used the Turtlesim spawn service to implement a system where a turtle appears randomly within the workspace. The desired goals and objectives were achieved.

### Contributors

| Name                          | Github                               |
|-------------------------------|--------------------------------------|
| Aldo Oziel Peña Gamboa        | https://github.com/AldoPenaGa        |
| Charbel Breydy Torres         | https://github.com/Buly1601          |
| Joan Carlos Monfil Huitle     | https://github.com/JoanCarlosMonfilHuitle|
| Enrique Rocha Espinoza        | https://github.com/Enrique-Rocha-Espinoza|

