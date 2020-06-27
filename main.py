import pygame
import sys
import settings
import bars
import random
import time


class Sorting:
    def __init__(self):
        self.settings = settings.Settings()

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("SortingAlgorithm")

        # initialize the bars
        self.bar_group = []
        self.create_bars()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # self.sort_everything()
                    self.heap_sort()
                    print('Space')

    def on_loop(self):
        pass

    def on_render(self):
        self.screen.fill(self.settings.bg_color)
        for bar in self.bar_group:
            bar.draw_bar()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def create_bars(self):
        height_track = []
        count = 0
        while len(self.bar_group) < self.settings.n_bars:
            height = random.randrange(100, self.settings.HEIGHT, 10)
            if height in height_track:
                while height in height_track:
                    height = random.randrange(10, self.settings.HEIGHT, 10)
            # else:
            height_track.append(height)
            bar = bars.Bars(self, height, self.settings.bar_width*count)
            self.bar_group.append(bar)
            count += 1

    def sort_everything(self):
        length = len(self.bar_group)
        for i in range(0, length - 1):
            for j in range(i+1, length):
                h1 = self.bar_group[i].height
                x1 = self.bar_group[i].x
                h2 = self.bar_group[j].height
                x2 = self.bar_group[j].x
                if h1 > h2:
                    self.bar_group[i].move_bar(x2)
                    self.bar_group[j].move_bar(x1)
                    temp_bar = self.bar_group[i]
                    self.bar_group[i] = self.bar_group[j]
                    self.bar_group[j] = temp_bar
            self.on_render()

    def heap_sort(self):
        # bar_already_sorted = []
        sorts = 0
        while sorts < self.settings.n_bars:
            min_height = 100000
            for i in range(sorts, len(self.bar_group)):
                h = self.bar_group[i].height
                if h < min_height:
                    short_bar = i
                    min_height = h
            x1 = self.bar_group[short_bar].x
            x2 = self.bar_group[sorts].x
            if x1 == x2:
                sorts += 1
                continue
            else:
                self.bar_group[short_bar].move_bar(x2)
                self.bar_group[sorts].move_bar(x1)
                temp = self.bar_group[sorts]
                self.bar_group[sorts] = self.bar_group[short_bar]
                self.bar_group[short_bar] = temp
            sorts += 1
            self.on_render()
            # time.sleep(.05)


if __name__ == "__main__":
    game = Sorting()
    game.on_execute()
