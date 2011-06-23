# utils.py -- Collection of utility functions.
#
# Copyright (C) 2005 Richard Norton <rwtnorton@earthlink.net>
#
# This file is part of PyOmino, a "falling blocks" game, written in Python,
# where blocks are polyominoes of size 3 or more.
#
# PyOmino is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# 
# PyOmino is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# 
# You should have received a copy of the GNU General Public License along with
# PyOmino; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA 02110-1301, USA.

import random

# Package-wide functions for calculating affine transformations on a
# 2-dimensional array.

def calc_rotate_cw(coords, axis):
    """calc_rotate_cw(coords, axis) -> List of CW-rotated [x,y]
    coordinates about axis.
    """
    h, k = axis
    return [ (h - k + coord[1], h + k - coord[0]) for coord in coords ]

def calc_rotate_ccw(coords, axis):
    """calc_rotate_ccw(coords, axis) -> List of CCW-rotated [x,y]
    coordinates about axis.
    """
    h, k = axis
    return [ (h + k - coord[1], -h + k + coord[0]) for coord in coords ]

def calc_move_l(coords):
    """calc_move_l(coords) -> List of [x,y] coordinates, translated
    down one column left.
    """
    return [ (coord[0], coord[1] - 1) for coord in coords ]

def calc_move_r(coords):
    """calc_move_r(coords) -> List of [x,y] coordinates, translated
    down one column right.
    """
    return [ (coord[0], coord[1] + 1) for coord in coords ]

def calc_move_d(coords):
    """calc_move_d(coords) -> List of [x,y] coordinates, translated
    down one row.
    """
    return [ (coord[0] + 1, coord[1]) for coord in coords ]

def collision(subject, environ, boundary):
    """collision(subject, environ, boundary) -> bool.

    Returns True iff coordinates in subject are outside of boundary or
    if coordinates in subject would result in collision with the
    coordinates in environ.
    Here, subject and environ are a sequence of [x,y] coordinates.
    The subject argument is the subject of collision-detection.
    The environ argument corresponds with what subject might collide with.
    The boundary argument delimits the boundary of consideration,
    described by [rows,cols].
    """
    rows, cols = boundary
    # check for boundary violation
    if [ coord for coord in subject\
    if coord[0] < 0 or coord[0] >= rows\
    or coord[1] < 0 or coord[1] >= cols ]:
        return True
    # check for pile collision
    if reduce(int.__add__,
    [ environ.count(coord) for coord in subject ]) > 0:
        return True
    return False

def random_color():
    MINIMUM = 80
    r = random.Random()
    return ( r.randint(MINIMUM, 255),
             r.randint(MINIMUM, 255),
             r.randint(MINIMUM, 255) )

def full_rows(size, coords):
    rows, cols = size
    count = [ 0 for row in range(rows) ]
    for coord in coords:
        row, col = coord
        count[row] += 1
    return [ i for i in range(rows) if count[i] == cols ]
