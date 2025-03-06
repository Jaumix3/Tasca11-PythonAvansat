import pygame
import random

# Configuració de la pantalla
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Inicialitzar pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()

# Carregar imatges
PADDLE_IMG = pygame.image.load("paddle.png")
BALL_IMG = pygame.image.load("ball.png")
BRICK_IMG = pygame.image.load("brick.png")

# Classe de la raqueta
class Paddle:
    def __init__(self):
        self.image = PADDLE_IMG
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
        self.speed = 7
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

# Classe de la pilota
class Ball:
    def __init__(self):
        self.image = BALL_IMG
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = -4
        self.active = False
    
    def move(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.speed_x *= -1
            if self.rect.top <= 0:
                self.speed_y *= -1

    def draw(self):
        screen.blit(self.image, self.rect)

# Classe dels maons
class Brick:
    def __init__(self, x, y):
        self.image = BRICK_IMG
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Crear objectes
paddle = Paddle()
ball = Ball()
bricks = [Brick(x * 64, y * 32) for x in range(10) for y in range(5)]

# Bucle principal
running = True
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ball.active = True

    paddle.move(keys)
    ball.move()
    
    # Col·lisions
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1
    
    for brick in bricks[:]:
        if ball.rect.colliderect(brick.rect):
            bricks.remove(brick)
            ball.speed_y *= -1
            break
    
    # Si la pilota cau
    if ball.rect.bottom >= HEIGHT:
        ball = Ball()
    
    # Dibuixar elements
    paddle.draw()
    ball.draw()
    for brick in bricks:
        brick.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
