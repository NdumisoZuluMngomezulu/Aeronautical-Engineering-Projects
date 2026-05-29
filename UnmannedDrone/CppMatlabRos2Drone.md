🚁 Simple Controlled Drone Project using C++, MATLAB, and ROS2
Overview

This project demonstrates how to build a simple autonomous drone control system using:

C++ → low-level drone control logic
MATLAB → simulation, visualization, and controller tuning
ROS2 → communication framework between drone components

The goal is to teach you:

Object-Oriented Programming in C++
Robotics communication using ROS2
PID control systems
Sensor simulation
Drone movement and navigation
MATLAB plotting and simulation
🧠 What You Will Build

You will create a drone system that can:

Take off
Land
Move forward/backward
Rotate
Maintain altitude automatically
Simulate sensor readings
Communicate through ROS2 topics
Be visualized in MATLAB


🏗️ Project Architecture
+-------------------+
| MATLAB Simulator  |
|  (Graphs/Plots)   |
+---------+---------+
          |
          | Sensor Data
          v
+-------------------+
| ROS2 Topics       |
| Publisher/Sub     |
+---------+---------+
          |
          v
+-------------------+
| C++ Drone Control |
| PID + Movement    |
+---------+---------+
          |
          v
+-------------------+
| Virtual Drone     |
| Position Updates  |
+-------------------+
📂 Project Structure

simple-drone-project/
│
├── ros2_ws/
│   └── src/
│       └── drone_control/
│           ├── include/
│           │   └── Drone.hpp
│           ├── src/
│           │   ├── Drone.cpp
│           │   ├── main.cpp
│           │   └── PIDController.cpp
│           ├── package.xml
│           └── CMakeLists.txt
│
├── matlab/
│   ├── drone_simulation.m
│   ├── pid_visualization.m
│   └── altitude_response.m
│
└── README.md
⚙️ Technologies Used
Technology	Purpose
C++	Drone control system
ROS2	Communication middleware
MATLAB	Simulation and graphs
PID Controller	Stabilization
OOP	System design


Install ROS2

Recommended:

Ubuntu 22.04
ROS2 Humble

Useful links:

ROS2 Installation Guide
Colcon Build Tool
Install MATLAB

Install these toolboxes:

Control System Toolbox
Robotics System Toolbox
Simulink (optional)
Install C++ Tools