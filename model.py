from pygame import image, draw, font
import game_confi as gc


def scoreboard(your,bot):
    your_score = font.SysFont('freesansbold.ttf',100)
    bot_score = font.SysFont('freesansbold.ttf',100)
    your_score = your_score.render('your score :  ' + str(your),True, (0,255,0))
    bot_score = bot_score.render("computer's score :  " + str(bot), True, (255,0,0))

    return your_score,bot_score

def block():
    return 

