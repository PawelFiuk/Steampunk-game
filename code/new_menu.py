from settings import *
import button
import sound


class Menu:
    def __init__(self):
        self.running_menu = True
        self.bg_menu = pygame.image.load("assets/graphics/menu_bg.png").convert_alpha()
        self.main_text = pygame.image.load("assets/graphics/steampunk_text.png").convert_alpha()
        self.bg_menu = pygame.transform.scale(self.bg_menu, (SCREEN_WIDTH +300, SCREEN_HEIGHT +300)).convert_alpha()
        pygame.display.set_caption("Steampunk")
        self.delay = 0
        try:
            sound.main_menu_music()
        except:
            pass

    def draw(self):
        self.running_menu = True
        button_start = button.Button(0, 500, start_button_img, 0.8)
        button_quit = button.Button(60, 900, exit_button_img, 0.025)

        while self.running_menu:
            self.delay += 0.05
            screen_menu.blit(self.bg_menu, (0 + self.delay, 0 ))
            screen_menu.blit(self.main_text, (600, 100))
            button_start.draw()
            button_quit.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_menu = False
                    pygame.quit()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.running_menu = False

            if button_start.draw():
                self.running_menu = False
                return True

            if button_quit.draw():
                self.running_menu = False
                pygame.quit()

            pygame.display.flip()
