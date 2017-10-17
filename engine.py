# engine.py
# A game engine class to help speed up coding

class engine(object):
    """ A Game Engine for Pygame games """

    @classmethod
    def load_png(name):
        """ Load image and return image object """
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as msg:
            print("Cannot load image: ", fullname)
            raise(SystemExit, message)
        return cls.image, cls.image.get_rect()
