# Frog generator

# Requirements
Python3 and some modules:
* PIL
* random
* glob
* time

a love of frogs

# API version

I've got a bonus API version available: [here](https://unicolo.re/api/frog)
![It's a frog](https://unicolo.re/api/frog)

# Idea

I came across a very simplistic frog generator (in terms of the generator and design: [here](https://frogitivity2.tumblr.com/post/185637054685/ready-to-start-yes-no)) and I thought I wanted the same thing! But I don't know how to draw...

2 days later I had a version 1 that gave me some ugly frogs.

In the version I present here, the parameters are mostly adjusted according to empirical intervals. I generated some frogs before making a git repository...

# Generation

The generation is done in python from a set of classes. The generator takes into account the `seed' to have a unique frog. It handles: shape, color, eyes, nose, mouth and hat.

the generation can be done in different sizes (default 1000×1000)

I'm not promising anything but I'll try to do some documentation in the code of `frog.py`.

the `generator.py` file makes a grid of X×Y frogs with a transparent background AND a gif with a black background of said frogs

# Art
For mouths and hats, the shapes are too complex to generate mathematically, so I call upon the work of a friend!

From kalitey's job: I order you to go and have a look!

unicolor-dream:
* [ tumblr gallery ](https://unicolor-dream.tumblr.com/)
* [ unicolo.re gallery ](https://gallery.unicolo.re)
