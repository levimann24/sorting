class Settings:
    def __init__(self):
        # Screen settings
        self.WIDTH = 1500
        self.HEIGHT = 1000
        self.bg_color = (100, 100, 100)

        # Bar settings
        self.bar_width = 20
        self.bar_color = (100, 0, 0)
        self.n_bars = self.WIDTH/self.bar_width
