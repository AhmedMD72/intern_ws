# Arabian Robot Workspace

## Clone the repository ##
```bash
git clone https://github.com/AhmedMD72/intern_ws.git
```

## Create workspace ##
```bash
mkdir -p ~/intern_ws/src
cd ~/intern_ws
```
## Initialize workspace ##
```bash
colcon build
source install/setup.bash
```

## Create ROS2 package ##
```bash
cd src
ros2 pkg create --build-type ament_python arabian_robot
cd ..
```
## Copy all the contents of the arabian_robot package from the repository.

## Build workspace again ##
```bash
colcon build
source install/setup.bash
```
## Launch Gazebo ##
```ros2 launch arabian_robot gazebo.launch.py```

## Launch RViz2 ## 
ros2 launch arabian_robot rviz.launch.py

