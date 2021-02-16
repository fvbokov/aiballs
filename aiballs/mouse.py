from pygame import mouse

class Mouse:
    def update(self):
        if mouse.get_pressed()[0] is True:
            if self.state == 'pressing':
                self.state = 'pressed'
            if self.state == 'released':
                self.state = 'pressing'
        else:
            if self.state == 'releasing':
                self.state = 'released'
            if self.state == 'pressed':
                self.state = 'releasing'

    def __init__(self):
        self.state = 'released'