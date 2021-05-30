#!/bin/bash

gnome-terminal -- python3 udp_server.py
gnome-terminal -- python3 convert.py
gnome-terminal -- python3 check_identity.py
