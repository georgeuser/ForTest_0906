cmake_minimum_required(VERSION 3.14)
project(55_02_BalancedBinaryTree)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(55_02_BalancedBinaryTree
        BalancedBinaryTree.cpp
        BinaryTree.cpp
        BinaryTree.h)
