# pile.py -- Pile of junk blocks.
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

import base_item, utils

class Pile(base_item.BoardItem):
    """Pile of junk blocks.
    """

    def __init__(self, board):
        """Pile(board) -> New pile on board.
        """
        base_item.BoardItem.__init__(self, board)

    def top(self):
        """Pile.top() -> List of tallest [x,y] coordinates.
        """
        return [ coord for coord in self.coordinates()\
            if coord[0] == reduce(min, [ x[0] for x in self.coordinates() ]) ]

    def remove_row(self, row):
        """Pile.remove_row(row) -> List of [x,y] coords removed.
        
        Remove row, move higher rows down.
        """
        at_row = [ coord for coord in self.coordinates() if coord[0] == row ]
        above  = [ coord for coord in self.coordinates() if coord[0] <  row ]
        below  = [ coord for coord in self.coordinates() if coord[0] >  row ]
        self._coords = below + utils.calc_move_d(above)
        return at_row

    def add_piece(self, piece):
        """Pile.add_piece(piece) -> None.

        Adds dead piece to pile; handles any resulting full lines.
        """
        b = self.board()
        b._choose_next_piece()
        self._coords.extend(piece.coordinates())
        for row in self.full_rows():
            self.remove_row(row)
            b._inc_lines_cleared()

    def full_rows(self):
        return utils.full_rows(self.board().size(), self.coordinates())

