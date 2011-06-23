# base_piece.py -- Base class for Piece's (polyominoes).
#
# Copyright (C) 2005 Richard Norton <rwtnorton@gmail.com>
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

import base_item, utils

class Piece(base_item.BoardItem):
    """Generic falling block piece.
    """

    def __init__(self, board, color):
        """Piece(board, color) -> New game piece.
        """
        base_item.BoardItem.__init__(self, board)
        self._color = color
        self._axis  = 0     # index to coordinate in self._coords

    def color(self):
        """Piece.color() -> RGB as tuple.
        """
        return self._color

    def axis(self):
        """Piece.axis() -> [x,y] for axis of rotation.
        """
        return self._coords[self._axis]

    def _calc_rotate_cw(self):
        """Piece._calc_rotate_cw() -> List of CW-rotated [x,y] coordinates.
        """
        return utils.calc_rotate_cw(self.coordinates(), self.axis())

    def _calc_rotate_ccw(self):
        """Piece._calc_rotate_cw() -> List of CCW-rotated [x,y] coordinates.
        """
        return utils.calc_rotate_ccw(self.coordinates(), self.axis())

    def _collision(self, coords):
        """Piece._collision(coords) -> bool.

        Returns True iff coords are out of board's boundaries or
        if coords would result in collision with pile.
        """
        return utils.collision(coords,
            self.board().pile().coordinates(),
            self.board().size())

    def _move(self, new_coords):
        """Piece._move(new_coords) -> bool.

        Attempts to move piece to the coordinates at new_coords.
        If the new_coords would result in a collision, no movement is
        performed and method returns False.
        Otherwise, the movement is performed and method returns True.
        """
        if self._collision(new_coords):
            return False
        self._coords = new_coords
        return True

    def rotate_cw(self):
        """Piece.rotate_cw() -> bool.

        Attempts to rotate piece once clockwise.
        If movement would be valid, movement is performed and returns True.
        Otherwise, movement is not performed and returns False.
        """
        return self._move(self._calc_rotate_cw())

    def rotate_ccw(self):
        """Piece.rotate_ccw() -> bool.

        Attempts to rotate piece once counter-clockwise.
        If movement would be valid, movement is performed and returns True.
        Otherwise, movement is not performed and returns False.
        """
        return self._move(self._calc_rotate_ccw())

    def move_r(self):
        """Piece.move_r() -> bool.

        Moves piece right if possible. Returns True iff moved.
        """
        return self._move(utils.calc_move_r(self.coordinates()))

    def move_l(self):
        """Piece.move_l() -> bool.

        Moves piece left if possible. Returns True iff moved.
        """
        return self._move(utils.calc_move_l(self.coordinates()))

    def move_d(self):
        """Piece.move_d() -> bool.

        Moves piece down if possible. Returns True iff moved.
        """
        return self._move(utils.calc_move_d(self.coordinates()))

    def free_fall(self):
        """Piece.free_fall() -> None.

        Moves piece all the way down to the pile.
        """
        self._coords = self.projection()
        self.board().pile().add_piece(self)

    def projection(self):
        """Piece.projection() -> List of [x,y] coordinates of fallen proj.
        """
        proj_coords = self.coordinates()
        while True:
            next_coords = utils.calc_move_d(proj_coords)
            if self._collision(next_coords):
                break
            proj_coords = next_coords
        return proj_coords

