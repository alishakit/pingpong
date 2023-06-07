from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = (transform.scale (image.load (player_image), (size_x,size_y)))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def player_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def player_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed



window = display.set_mode((700,500))
display.set_caption("Пин-понг :)")
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('647a5f52eae92.jpg'),(700,500))

platform_1 = Player("PicsArt_06-02-11.34.11.png",0,0,5,50,150)
platform_2 = Player("PicsArt_06-02-11.34.11.png",650,0,5,50,150)
tumbleweed = Player("647a5f4f7fb8c.png",350,0,2,85,65)

game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        platform_1.reset()
        platform_1.player_1()
        platform_2.reset()
        platform_2.player_2()
        tumbleweed.reset()
        tumbleweed.player_1()
        
    clock.tick(FPS)
    display.update()
