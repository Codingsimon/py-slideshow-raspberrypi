==============================
py-slideshow - image slideshow
==============================

Random image slideshow in Python with OpenGL pan/zoom effects.

.. image:: icon.png

* Corey Goldberg, (c) 2013, (http://goldb.org)
* License: GNU GPLv3

----

**Requirements**:

* Python 2.7+ or 3.2+
* pyglet

**Command Line Help**::

    $ ./slideshow.py -h
    usage: slideshow.py dir

    positional arguments:
      dir              directory of images

**Example**::

    $ git clone https://github.com/cgoldberg/py-slideshow.git
    $ cd py-slideshow
    $ python slideshow.py /home/cgoldberg/images/


**Anaconda Problem solving**
$ cd /home/$USER/miniconda/lib
$ mkdir backup  # Create a new folder to keep the original libstdc++
$ mv libstd* backup  # Put all libstdc++ files into the folder, including soft links
$ cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6  ./ # Copy the c++ dynamic link library of the system here
$ ln -s libstdc++.so.6 libstdc++.so
$ ln -s libstdc++.so.6 libstdc++.so.6.0.19