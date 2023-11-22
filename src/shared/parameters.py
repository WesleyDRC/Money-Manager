class Parameters:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Criando a instância Singleton de Parameters")
            cls._instance = super(Parameters, cls).__new__(cls)
            cls._instance.screen_width = 100
            cls._instance.screen_height = None
        return cls._instance

    @staticmethod
    def getScreenWidth():
        return Parameters._instance.screen_width

    @staticmethod
    def setScreenWidth(width):
        Parameters._instance.screen_width = width

    @staticmethod
    def getScreenHeight():
        return Parameters._instance.screen_height

    @staticmethod
    def setScreenHeight(height):
        Parameters._instance.screen_height = height
