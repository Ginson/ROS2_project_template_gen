#!/bin/bash

mkdir -p $1
touch $1/CMakeLists.txt
touch $1/package.xml
mkdir -p $1/include
touch $1/include/$1.hpp
mkdir -p $1/src
touch $1/src/$1.cpp
mkdir -p $1/launch
touch $1/launch/launch_$1.py
