#!/usr/bin/env python
#
#  Copyright (c) 2013, 2015, Corey Goldberg
#
#  Dev: https://github.com/cgoldberg/py-slideshow
#  License: GPLv3


import argparse
import random
import os
import pyglet
import configparser

from numpy import size

speed = 0
subfolder = "random"
images_size = 0
image_paths = []

def import_config():
    parser = configparser.ConfigParser()
    parser.read('config.txt')
    global speed 
    speed = float(parser.get('Konfiguration', 'geschwindigkeit'))
    global subfolder 
    subfolder = parser.get('Konfiguration', 'bilderpfad')


def update_pan_zoom_speeds():
    global _pan_speed_x
    global _pan_speed_y
    global _zoom_speed
    _pan_speed_x = random.randint(-8, 8)
    _pan_speed_y = random.randint(-8, 8)
    _zoom_speed = random.uniform(-0.02, 0.02)
    return _pan_speed_x, _pan_speed_y, _zoom_speed


def update_pan(dt):
    sprite.x += dt * _pan_speed_x
    sprite.y += dt * _pan_speed_y


def update_zoom(dt):
    sprite.scale += dt * _zoom_speed


def update_image(dt):
    try:
        img = pyglet.image.load(random.choice(image_paths))
    except:
        print("Exception image file not found.")

    sprite.image = img
    scale_factor = get_scale(window, img)
    sprite.scale = scale_factor

    #set image x position
    x_offset = (window.width - img.width*scale_factor) / 2
    if x_offset > 0 :
        sprite.x = x_offset
    else:
        sprite.x = 0

    sprite.y = 0
    update_pan_zoom_speeds()
    window.clear()


def get_image_paths(input_dir='.'):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'gif')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return paths

def get_scale(window, image):
    if image.width > image.height:
        scale = float(window.width) / image.width
    else:
        scale = float(window.height) / image.height
    return scale


window = pyglet.window.Window(fullscreen=True)


@window.event
def on_draw():
    sprite.draw()

def load_images():
    global image_paths
    if subfolder == 'random':
        image_paths = get_image_paths(args.dir + "/images")
    else:
        image_paths = get_image_paths(args.dir + "/images/" + subfolder)



if __name__ == '__main__':

    import_config()

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='directory of images', nargs='?', default=os.getcwd())
    args = parser.parse_args()

    load_images()

    img = pyglet.image.load(random.choice(image_paths))
    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img)

    pyglet.clock.schedule_interval(update_image, speed)
    pyglet.app.run()
