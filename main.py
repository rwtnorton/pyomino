#! /usr/bin/env python
# main.py -- Driver program for game.
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

import board, pygame, pieces

class Square(pygame.sprite.Sprite):
    def __init__(self, pos, width, color):
        pygame.sprite.Sprite.__init__(self)
        self._coord = row, col = pos
        size = (width, width)
        self.image = pygame.Surface(size).convert()
        self.image.fill(color)
        self.rect  = pygame.Rect( (col * width, row * width), size )
        self._width = width

    def width(self):
        return self._width

    def _move(self, new_pos):
        self._coord = row, col = new_pos
        width = self.width()
        self.rect.topleft = (col * width, row * width)


BLACK            = (  0,   0,   0)
WHITE            = (255, 255, 255)
PROJECTION_COLOR = WHITE
PILE_COLOR       = (255,  85, 255)


def _map_coords_to_squares(coords, width, color):
    return [ Square(coord, width, color) for coord in coords ]

def map_piece_to_squares(piece, width):
    return _map_coords_to_squares(piece.coordinates(), width,\
        piece.color())

def map_projection_to_squares(piece, width):
    return _map_coords_to_squares(piece.projection(), width,\
        PROJECTION_COLOR)

def map_pile_to_squares(pile, width):
    return _map_coords_to_squares(pile.coordinates(), width, PILE_COLOR)

def map_next_piece_to_squares(piece, width, offset):
    squares = map_piece_to_squares(piece, width)
    for sq in squares:
        sq.rect.topleft = map(int.__add__, sq.rect.topleft, offset)
    return squares


#class sp_T(pieces.T):
#   def __init__(self, board):
#       pieces.T.__init__(self, board)
#       self._squares = self._init_squares()

#   def _init_squares(self):
#       return [ Square(coord, 25, self.color())\
#           for coord in self.coordinates() ]

#   def _move(self, new_coords):
#       if pieces.T._move(self, new_coords):
#           for i in range(len(new_coords)):
#               self._squares[i]._move(new_coords[i])
#           return True
#       return False

#   def squares(self):
#       return self._squares


def main():
    pygame.init()

    # Establish screen size.
#   SIZE = (800, 800)
    SIZE = (480, 480)
#   SIZE = (200, 200)
    screen = pygame.display.set_mode(SIZE)

    # Caption.
    pygame.display.set_caption('PyOmino')

    # Mouse.
    pygame.mouse.set_visible(False)

    # Background.
    bg_img = pygame.Surface(SIZE).convert()
    bg_img.fill(BLACK)
    screen.blit(bg_img, (0, 0))
    pygame.display.update()

    # Board.
#   b = board.Board((10, 5))
#   b = board.Board()
    b = board.Board((30, 12))
#   b = board.Board((30, 20))

    WIDTH = SIZE[0] / b.rows()

    group = pygame.sprite.OrderedUpdates()

    # Draw piece and pile.
    group.add(map_piece_to_squares(b.piece(), WIDTH)\
        + map_pile_to_squares(b.pile(), WIDTH)\
        + map_projection_to_squares(b.piece(), WIDTH))
    pygame.display.update(group.draw(screen))

    PLAY_AREA_WIDTH = WIDTH * b.cols()

    # Display lines cleared.
    lines = pygame.font.Font(None, 36)
    lines_img = lines.render("Lines: %d" % b.lines_cleared(), 1, WHITE)
    lines_pos = lines_img.get_rect(left=PLAY_AREA_WIDTH+5)
    screen.blit(lines_img, lines_pos)

    LINES_HEIGHT = lines_pos.bottom
    next_img = lines.render("Next:", 1, WHITE)
    next_pos = next_img.get_rect(left=PLAY_AREA_WIDTH+5, top=LINES_HEIGHT)
    NEXT_OFFSET = (PLAY_AREA_WIDTH+5, next_pos.bottom)
    next_squares = map_next_piece_to_squares(b.next_piece(), WIDTH,
        NEXT_OFFSET)
    group.add(next_squares)
    pygame.display.update(group.draw(screen))
    screen.blit(next_img, next_pos)

    # Display dividing line between gameplay area and statistics.
    dividor = pygame.Surface( (1, SIZE[1]) ).convert()
    dividor.fill(WHITE)
    screen.blit(dividor, (PLAY_AREA_WIDTH, 0))
    pygame.display.update()

    # Load game sounds.
    sound = pygame.mixer.Sound('ting.aif')

    t = pygame.time.Clock()
    FPS = 1
    while True:
        # Base piece fall speed off of lines cleared.
        t.tick(FPS + b.lines_cleared() / 10)
        cur_piece = b.piece()

        # Check for game over condition.
        if [ coord for coord in b.pile().top()\
        if coord in cur_piece.coordinates() ]:
            finito = pygame.font.Font(None, 60)
            game_over = finito.render("Game Over", 1, (255, 0, 0))
            screen.blit(game_over, (0, SIZE[1] / 2))
            pygame.display.update()
            pygame.event.wait()
            print "\nLines: %s" % b.lines_cleared()
            return

        # Deal with user input.
        for e in pygame.event.get():
            has_key  = hasattr(e, 'key')
            has_type = hasattr(e, 'type')

            if has_key  and e.key  == pygame.K_ESCAPE\
            or has_key  and e.key  == pygame.K_q\
            or has_type and e.type == pygame.QUIT:
                print "\nLines: %s" % b.lines_cleared()
                return
            elif has_key  and e.key  == pygame.K_UP\
            and  has_type and e.type == pygame.KEYDOWN:
                cur_piece.free_fall()
                sound.play()
                cur_piece = b.piece()
            elif has_key  and e.key  == pygame.K_DOWN\
            and  has_type and e.type == pygame.KEYDOWN:
                cur_piece.move_d()
            elif has_key  and e.key  == pygame.K_LEFT\
            and  has_type and e.type == pygame.KEYDOWN:
                cur_piece.move_l()
            elif has_key  and e.key  == pygame.K_RIGHT\
            and  has_type and e.type == pygame.KEYDOWN:
                cur_piece.move_r()
            elif has_key  and e.key  == pygame.K_a\
            and  has_type and e.type == pygame.KEYDOWN:
                cur_piece.rotate_cw()
            elif has_key  and e.key  == pygame.K_b\
            and  has_type and e.type == pygame.KEYDOWN:
                cur_piece.rotate_ccw()
            elif has_key  and e.key  == pygame.K_p\
            and  has_type and e.type == pygame.KEYDOWN:
                while True:
                    paused_event = pygame.event.wait()
                    if hasattr(paused_event, 'key')\
                    and paused_event.key == pygame.K_p:
                        break

        # Move piece down one. If it collides with pile, add to pile.
        if not cur_piece.move_d():
            cur_piece.free_fall()
            sound.play()

        # Text-only game display. Well, I like it.
        b._p('E','.')
        print

        # Update screen with current board state.
        # This is inefficient and kludgy, but it works for now.
        group.clear(screen, bg_img)
        group.empty()
        group.add(map_piece_to_squares(b.piece(), WIDTH)\
            + map_pile_to_squares(b.pile(), WIDTH)\
            + map_projection_to_squares(b.piece(), WIDTH)\
            + map_next_piece_to_squares(b.next_piece(), WIDTH, NEXT_OFFSET))
        pygame.display.update(group.draw(screen))

        # Update screen with game statistics.
        screen.blit(bg_img, lines_pos)
        pygame.display.update(lines_pos)
        screen.blit(next_img, next_pos)
        pygame.display.update(next_pos)
        lines_img = lines.render("Lines: %d" % b.lines_cleared(), 1, WHITE)
        lines_pos = lines_img.get_rect(left=PLAY_AREA_WIDTH+5)
        screen.blit(lines_img, lines_pos)
        pygame.display.update(lines_pos)

if __name__ == '__main__':
    main()

