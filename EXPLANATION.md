Explanation for data types:

There were many different types of data I chose to send to the publisher. I chose simple GPS coordinates, battery level, obstacle distance, 
internal and external temperature, communication signal strength, and some basic  motor feedback (commanded speed vs measured speed. These represent some essential 
information I believe a rover would need to continuously generate and share.

All of this data can contribute greatly to the essential functions of a robotics system. GPS coordinates help support navigation, and help with path planning. 
Obstacle distance (distance of an object from where object is moving towards) can help avoid collisions. Monitoring battery is essential for a robot, so that it knows how long 
it will last as this can indicate it needing to be charged or self charged if it has the ability to do so (i.e  through solar panels, and the robot would cease all movements to 
preserve power). Temperature readings can help give data to avoid over heating, and can indicate any cooling processes (i.e fans) or to move to a cooler location. Knowing signal
strength is essential to prevent the robot from leaving the area where it can be detected or to prevent it from moving towards locations where it would lose connection. 
Simple motor feedback data I used was commanded speed, so this is the desired speed of the robot at some point of time while measured speed is how much speed the robot is actually
achieving, this is useful to know as a robot may not reach desired speeds due to rough terrain or a problem in its build that needs to be solved. Togther these data types
are essential to contribute to a robtics system to avoid large errors/mistakes/problems from occurring. 
