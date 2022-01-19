import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.Surface((32, 64))
    pygame.Surface.fill(self.image, (220, 0, 0))
    self.rect = self.image.get_rect(topleft = pos)

    # movement
    self.direction = pygame.math.Vector2(0, 0)
    self.speed = 7
    self.gravity = 0.8
    self.jump_speed = -16

  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y

  def get_input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      self.direction.x = 1
    elif keys[pygame.K_a]:
      self.direction.x = -1
    else:
      self.direction.x = 0

    if keys[pygame.K_SPACE]:
        self.jump()

  def jump(self):
    self.direction.y = self.jump_speed

  def update(self):
    self.get_input()
    self.rect.x += self.direction.x * self.speed
    self.apply_gravity()