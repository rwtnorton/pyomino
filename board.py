# board.py -- Gameplay area.
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

import pile, utils, generator

class Board:
    """Generic, 2-dimensional, orthogonal game board.
    """

    DEFAULT_SIZE        = ( 22, 10 )
    DEFAULT_MIN_SIZE    = ( 4, 4 )

    def __init__(self, size=DEFAULT_SIZE):
        """Board([size]) -> New game board.

        Size should be given as (rows, cols).
        """
        rows, cols = size
        if rows < self.DEFAULT_MIN_SIZE[0]: rows = self.DEFAULT_MIN_SIZE[0]
        if cols < self.DEFAULT_MIN_SIZE[1]: cols = self.DEFAULT_MIN_SIZE[1]
        self._size = ( rows, cols )

        self._cleared   = 0
        self._pile      = pile.Pile(self)
        self._piece     = None
        self._next      = None
        self._gen       = generator.PieceGenerator(self)
        self._choose_next_piece()

    def lines_cleared(self):
        """Board.lines_cleared() -> Number of lines cleared.
        """
        return self._cleared

    def size(self):
        """Board.size() -> (rows, columns)
        """
        return self._size

    def rows(self):
        """Board.rows() -> Number of rows.
        """
        return self._size[0]

    def cols(self):
        """Board.cols() -> Number of columns.
        """
        return self._size[1]

    def piece(self):
        """Board.piece() -> Active piece on board.
        """
        return self._piece

    def pile(self):
        """Board.pile() -> Pile of junk blocks.
        """
        return self._pile

    def _inc_lines_cleared(self):
        """Board._inc_lines_cleared() -> None.

        Increments number of lines cleared.
        """
        self._cleared += 1

    def _p(self, block='E', blank=':'):
        """Board._p() -> None.

        Prints ascii rendition of game board to stdout.
        """
        data = sorted(self.piece().coordinates() + self.pile().coordinates())
        for row in range(self.rows()):
            for col in range(self.cols()):
                if (row, col) in data:
                    print block,
                else:
                    print blank,
            print

    def _choose_next_piece(self):
        if not self._next:
            self._next  = self._gen.next()(self)
        self._piece = self._next
        self._next  = self._gen.next()(self)

    def next_piece(self):
        return self._next

