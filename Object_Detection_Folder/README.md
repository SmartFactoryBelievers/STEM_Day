# Smart Rover Capstone Project #1: Object Detection
The following module will guide learners through the Deloitte Smart Rover Capstone Project #1: Object Detection. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Capstone 01: Object Detection](#1-Capstone-01-Object-Detection)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 01 Troubleshooting](#3-Project-01-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Capstone 01: Object Detection
### About Project 01

📸: **Objective:** To learn programming basics and make the rover follow them when they are in view of the rover's camera

In this project, students will learn about setting up their program, using object detection models, and using video hardware. Students will build a simple circuit to demonstrate their program. In the end, their program should produce a rover that follows them when they are in frame of the camera.

This activity will introduce students to higher levels of programming in Python using the Thonny Integrated Development Environment (IDE). This will allow students to modify the pre-loaded programs. Students will use Thonny in future activities to connect these skills to future skills.

### Required Components
Smart Module, Rover, Motor Control (U8), 1KΩ Resistor (x4), connector wiring (all colors), 3 snap connector (3), 2 snap connector (2) x 2.

In addition to the physical required components, be sure to install all of the dependencies by running "pip install -r requirements.txt" and making sure that you have the Object_Detection_Files Folder downloaded in the same repository as your code.

### Instructions
1. First, connect your Smart Module to a monitor or to a laptop (See note below).
2. Build the circuit as shown in the picture below
3. Once the circuit is created, open up Thonny and load Object_Detection.py into the code editor. The pre-loaded programs are ready to run, but you will learn by reviewing the language and completing the challenges.
4. Once you have completed the program, start the program by clicking the RUN button in Thonny to blink the LED.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Capstone 01 Build Video
### Capstone 01 Code-along Video

### Capstone 01 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing what the rover is trained to follow.

:two: Try making the rover look for multiple objects at once

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Capstone Project 01.  The key terms will help support you as you navigate the rover activity. 
- **Functions**: a block of organized, reusable code that is used to perform a single, related action.
- **Motor Control Module:** contains 16 transistors and resistors that are needed to control the motors of the rover.
- **Rover body:** has both motors that convert electrical energy into mechanical motion and a battery.

## 3. Capstone 01 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Capstone 01 Solution Code](../Resources/Solutions/Project04_ProgrammedDriving_Solution.py)

## Tips & Tricks
### :warning: **WARNING** :warning: 
Always check your wiring before turning on a circuit. Never leave a circuit unattended while the batteries are installed. Never connect additional batteries or any other power sources to your circuits. Discard any cracked or broken parts.
- Most circuit problems are due to incorrect assembly, always double-check that your circuit exactly matches the drawing for it especially the direction of arrows on the circuits. 
- Be sure that parts with positive/negative markings are positioned as per the build diagram.
- Be sure that all connections are securely snapped.
- Try replacing the batteries in the Rover body

### [Smart Module Pin Layout Guide](../Resources/smart-module-pinout.jpg)
### [Thonny Controls Overview](../Resources/introduction-to-raspberry-pi.pdf)
### [Debugging Python in Thonny](../Resources/introduction-to-raspberry-pi.pdf)

## 4. Additional Resources
- [The Smart Rover Project Manual](../Resources/Smart-Rover-Manual.pdf)
- [Snap Circuit Components list](../Resources/snap-circuit-components.pdf)
- [Circuit Troubleshooting](../Resources/introduction-to-electricity.pdf)
- [FAQ]()

✅ For a full list of additional resources, visit the [Resources Folder](../Resources/README.md)
