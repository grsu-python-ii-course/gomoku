from game2dboard import Board

# Global consts
FIELD_WIDTH = 25
FIELD_HEIGHT = 20
BLOCK_SIZE = 25

# Global vars
snake = []
lastkey = ""


def setup():
    global snake, lastkey
    w2 = FIELD_WIDTH // 2  # field center
    h2 = FIELD_HEIGHT // 2
    field.fill(None)
    snake = [(h2, w2), (h2, w2 + 1)]  # Initial snake position
    for pos in snake:
        field[pos[0]][pos[1]] = 'SOME'  # Draw the snake
    lastkey = "Left"  # starts moving to the left


field = Board(FIELD_HEIGHT, FIELD_WIDTH)
field.cell_size = BLOCK_SIZE
field.title = "TEST BOARD"
field.cursor = None  # Hide the cursor
field.margin = 10
setup()
field.show()
