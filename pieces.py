# pieces.py -- Actual Piece's are fleshed out here.
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

import base_piece, utils

DEFAULT_COLORS = {
    'tri_I': utils.random_color(),
    'tri_V': utils.random_color(),
    'tetr_T': (200, 200,  10),
    'tetr_I': ( 10, 200, 200),
    'tetr_O': (200,  10, 200),
    'tetr_L': (200,  10,  10),
    'tetr_J': ( 10, 200,  10),
    'tetr_S': ( 10,  10, 200),
    'tetr_Z': (150, 150, 150),
    'pent_W': utils.random_color(),
    'pent_Z': utils.random_color(),
    'pent_S': utils.random_color(),
    'pent_L': utils.random_color(),
    'pent_J': utils.random_color(),
    'pent_I': utils.random_color(),
    'pent_T': utils.random_color(),
    'pent_U': utils.random_color(),
    'pent_P': utils.random_color(),
    'pent_D': utils.random_color(),
    'pent_F': utils.random_color(),
    'pent_7': utils.random_color(),
    'pent_Y': utils.random_color(),
    'pent_R': utils.random_color(),
    'pent_N': utils.random_color(),
    'pent_M': utils.random_color(),
    'pent_V': utils.random_color(),
    'pent_X': utils.random_color()
}

class tri_I(base_piece.Piece):
    """Triomino I piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tri_I']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 )
        ]
        self._axis = 1


class tri_V(base_piece.Piece):
    """Triomino V piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tri_V']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 1, mid - 1 )
        ]
        self._axis = 0


class tetr_I(base_piece.Piece):
    """Tetromino I piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_I']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 )
        ]
        self._axis = 1


class tetr_J(base_piece.Piece):
    """Tetromino J piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_J']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid + 1 )
        ]
        self._axis = 1


class tetr_L(base_piece.Piece):
    """Tetromino L piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_L']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid - 1 )
        ]
        self._axis = 1


class tetr_O(base_piece.Piece):
    """Tetromino O piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_O']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid     ),
            ( 1, mid + 1 )
        ]
        self._axis = 2

    def _calc_rotate_cw(self):
        return self.coordinates()

    def _calc_rotate_ccw(self):
        return self.coordinates()


class tetr_S(base_piece.Piece):
    """Tetromino S piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_S']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid - 1 ),
            ( 1, mid     )
        ]
        self._axis = 3


class tetr_T(base_piece.Piece):
    """Tetromino T piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_T']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 1, mid - 1 ),
            ( 1, mid     ),
            ( 1, mid + 1 )
        ]
        self._axis = 2


class tetr_Z(base_piece.Piece):
    """Tetromino Z piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['tetr_Z']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 1, mid     ),
            ( 1, mid + 1 )
        ]
        self._axis = 2

class pent_W(base_piece.Piece):
    """Pentomino W piece.
    """
    def __init__(self, board, color=DEFAULT_COLORS['pent_W']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 1, mid     ),
            ( 1, mid + 1 ),
            ( 2, mid + 1 )
        ]
        self._axis = 2

class pent_X(base_piece.Piece):
    """Pentomino T piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_X']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 1, mid - 1 ),
            ( 1, mid     ),
            ( 1, mid + 1 ),
            ( 2, mid     )
        ]
        self._axis = 2

class pent_Z(base_piece.Piece):
    """Pentomino Z piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_Z']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 1, mid     ),
            ( 2, mid     ),
            ( 2, mid + 1 )
        ]
        self._axis = 2

class pent_S(base_piece.Piece):
    """Pentomino S piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_S']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid     ),
            ( 2, mid - 1 ),
            ( 2, mid     )
        ]
        self._axis = 2

class pent_L(base_piece.Piece):
    """Pentomino L piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_L']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 ),
            ( 1, mid - 1 )
        ]
        self._axis = 1

class pent_J(base_piece.Piece):
    """Pentomino J piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_J']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 ),
            ( 1, mid + 2 )
        ]
        self._axis = 2

class pent_I(base_piece.Piece):
    """Pentomino I piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_I']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 2 ),
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 )
        ]
        self._axis = 2

class pent_T(base_piece.Piece):
    """Pentomino T piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_T']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid     ),
            ( 2, mid     )
        ]
        self._axis = 3

class pent_U(base_piece.Piece):
    """Pentomino U piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_U']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid - 1 ),
            ( 1, mid + 1 )
        ]
        self._axis = 1

class pent_F(base_piece.Piece):
    """Pentomino F piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_F']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid - 1 ),
            ( 1, mid     ),
            ( 2, mid     )
        ]
        self._axis = 3

class pent_Y(base_piece.Piece):
    """Pentomino Y piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_Y']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 ),
            ( 1, mid     )
        ]
        self._axis = 1

class pent_R(base_piece.Piece):
    """Pentomino R piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_R']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 ),
            ( 1, mid + 1 )
        ]
        self._axis = 2

class pent_7(base_piece.Piece):
    """Pentomino 7 piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_7']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 1, mid     ),
            ( 1, mid + 1 ),
            ( 2, mid     )
        ]
        self._axis = 2

class pent_N(base_piece.Piece):
    """Pentomino N piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_N']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid + 1 ),
            ( 1, mid + 2 )
        ]
        self._axis = 2

class pent_M(base_piece.Piece):
    """Pentomino M piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_M']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 0, mid + 2 ),
            ( 1, mid - 1 ),
            ( 1, mid     )
        ]
        self._axis = 0

class pent_P(base_piece.Piece):
    """Pentomino P piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_P']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid     ),
            ( 1, mid + 1 )
        ]
        self._axis = 1

class pent_D(base_piece.Piece):
    """Pentomino D piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_D']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid - 1 ),
            ( 1, mid     )
        ]
        self._axis = 1

class pent_V(base_piece.Piece):
    """Pentomino V piece.
    """

    def __init__(self, board, color=DEFAULT_COLORS['pent_V']):
        base_piece.Piece.__init__(self, board, color)
        mid = board.cols() / 2 - 1
        self._coords = [
            ( 0, mid - 1 ),
            ( 0, mid     ),
            ( 0, mid + 1 ),
            ( 1, mid - 1 ),
            ( 2, mid - 1 )
        ]
        self._axis = 2

    def axis(self):
        return ( self._coords[3][0], self._coords[1][1] )



# lists of constructors

TRIOMINO_LIST  = [ tri_I, tri_V ]
TETROMINO_LIST = [ tetr_T, tetr_I, tetr_O, tetr_L, tetr_J, tetr_S, tetr_Z ]
PENTOMINO_LIST = [
    pent_W, pent_X, pent_Z, pent_S, pent_L, pent_J, pent_I,
    pent_T, pent_U, pent_P, pent_D, pent_F, pent_7, pent_Y, pent_R,
    pent_N, pent_M, pent_V
]
PIECE_LIST = TRIOMINO_LIST + TETROMINO_LIST + PENTOMINO_LIST
