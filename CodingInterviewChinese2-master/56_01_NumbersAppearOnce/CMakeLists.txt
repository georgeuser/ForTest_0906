cmake_minimum_required(VERSION 3.14)
project(56_01_NumbersAppearOnce)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(56_01_NumbersAppearOnce
        BinaryTree.cpp
        BinaryTree.h
        NumbersAppearOnce.cpp)
