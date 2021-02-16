import math
from .circle import Circle

def distance(pos1, pos2):
    return (math.sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2))

def check_collisions(obj, balls):
    for ball in balls:
        if obj is not ball:
            if distance(ball.pos, obj.pos) <= obj.radius + ball.radius:
                if (ball.radius > obj.radius):
                    on_collision(ball, obj)
                else:
                    on_collision(obj, ball) 

def on_collision(ball1, ball2):
    length = distance(ball1.pos, ball2.pos)

    m1 = ball1.mass
    m2 = ball2.mass

    r2new = (length - math.sqrt(length * length - 4 * ((pow(ball1.radius, 3) + pow(ball2.radius, 3) - pow(length, 3)) / (-3 * length)))) / 2
    r1new = (length - r2new)

    ball1.radius = r1new
    ball2.radius = r2new

    m1new = ball1.mass
    m2new = ball2.mass

    m3 = m1new - m1

    v1 = ball1.velocity
    v2 = ball2.velocity

    v2new = v2
    v1new = (m1 * v1 + m3 * v2) / m1new

    ball1.velocity = v1new
    ball2.velocity = v2new