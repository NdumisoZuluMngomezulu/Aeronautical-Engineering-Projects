cmake_minimum_required(VERSION 3.8)
project(drone_control)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(drone_node src/main.cpp)

ament_target_dependencies(drone_node
  rclcpp
  std_msgs
)

install(TARGETS
  drone_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()