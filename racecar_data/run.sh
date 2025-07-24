#!/usr/bin/env sh

rocker --devices /dev/dri --x11 --volume ./data:/data -- ghcr.io/robinlabuji/ros2rep/racecar_data:jazzy

