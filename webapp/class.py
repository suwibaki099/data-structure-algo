# OOP
class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        """ info: This is how the character run """
        print('run')
        return 'done'


player1 = PlayerCharacter('Jandy')

print(player1.run())
