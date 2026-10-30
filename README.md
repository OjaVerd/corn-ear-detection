# Corn Ear Detection

A deep-learning system that detects corn ears (and the ear-to-stalk region) in field videos. 

## Overview

Corn plants are usually inspected by hand. This project automates part of that: given a corn-field video, the system finds the target in each frame and outputs an annotated video.

The course provided 40 unlabeled videos (20 shot at about 2 ft, 20 at about 4 ft). I sampled frames from them, labeled my own dataset, and trained a model on it.

**Pipeline:** raw videos → frame sampling → annotation → training → video detection

