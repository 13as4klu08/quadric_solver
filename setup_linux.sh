#!/bin/bash
echo "Packages should be installed by default or may not install on raspberry pi devices, in that case, manually install packages by adding --break-system-packages at pip install [packages]"
echo "Waiting 6 seconds"
sleep 6
pip install numpy
pip install colorama
clear
python main.py
