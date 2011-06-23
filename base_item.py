# base_item.py -- Base class for items on a Board.
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

import board

class BoardItem:
    """Superclass for items on a board.
    """
    def __init__(self, board):
        self._board = board
        self._coords = []

    def board(self):
        """BoardItem.board() -> Board associated with this piece.
        """
        return self._board

    def coordinates(self):
        """BoardItem.coordinates() -> List of [x,y] coordinates on board.
        """
        return self._coords

