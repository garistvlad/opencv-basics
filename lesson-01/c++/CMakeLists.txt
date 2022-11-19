cmake_minimum_required(VERSION 2.8)
project(lesson01)

set(CMAKE_CXX_STANDARD 14)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(lesson01 lesson01.cpp)

target_link_libraries(lesson01 ${OpenCV_LIBS})