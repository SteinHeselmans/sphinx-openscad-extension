Welcome to Example's documentation!
===================================

A 2D donut projection with Vector camera up on Z-axis, left aligned.

.. cad::
    :caption: simple example CAD
    :align: left
    :camera: 0,0,100,0,0,0

    difference() {
        circle(r=8);
        circle(r=5);
    }

A 3D example with default camera, right aligned.

.. cad::
    :caption: 3D example CAD
    :align: right

    difference() {
        cube(12, center=true);
        sphere(8);
    }

A 3D construction with Vector camera, center aligned, colored.

.. cad::
    :caption: another 3D example CAD
    :align: center
    :camera: 15000,15000,8000,3000,2000,0

    for(i=[0:1:10]) {
        color("red") cube(size=[6000,35,175]);
        translate([0, 4000, 0]) color("red") cube(size=[6000,35,175]);
        translate([i*600,0,0]) {
            color("blue") cube(size=[35,4000,175]);
        }
    }

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
