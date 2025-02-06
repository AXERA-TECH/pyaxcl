#!/bin/bash

cur_path=$(cd "$(dirname $0)";pwd)
cd $cur_path

if [ -d "dist" ]; then
rm -rf dist
fi

if [ -d "build" ]; then
rm -rf build
fi

if [ -d "pyAXCL.egg-info" ]; then
rm -rf "pyAXCL.egg-info"
fi


python3 setup.py bdist_wheel --dist-dir ./out


if [ -d "build" ]; then
rm -rf build
fi

if [ -d "pyAXCL.egg-info" ]; then
rm -rf "pyAXCL.egg-info"
fi


