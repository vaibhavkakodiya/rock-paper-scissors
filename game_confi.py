import os
from pygame import image, transform

ASSET_DIR = os.path.join('assets','hands')
display_size = screen_size = 1200
# Margines
MARGINE = 10

#images
rock_path = os.path.join(ASSET_DIR,'rock.jpg')
rock = image.load(rock_path)
rock = transform.scale(rock,(display_size//3,display_size//6))

paper_path = os.path.join(ASSET_DIR,'paper.jpg')
paper = image.load(paper_path)
paper = transform.scale(paper,(display_size//3,display_size//6))

scissors_path = os.path.join(ASSET_DIR,'scissors.jpg')
scissors = image.load(scissors_path)
scissors = transform.scale(scissors,(display_size//3,display_size//6))

images = [rock,paper,scissors]

# win, lost, draw
win = image.load(os.path.join(ASSET_DIR,'win.png'))
#win = transform.scale(win,())
lost = image.load(os.path.join(ASSET_DIR,'lost.png'))
draw = image.load(os.path.join(ASSET_DIR,'draw.png'))