import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player

class Level:
  def __init__(self, level_data, surface):
    self.display_surface = surface
    self.setup_level(level_data)
    self.world_shift = 0

  def setup_level(self, layout):
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()

    for row_index, row in enumerate(layout):
      for col_index, cell in enumerate(row):
        x = col_index * tile_size
        y = row_index * tile_size

        if cell == 'X':
          tile = Tile((x,y), tile_size)
          self.tiles.add(tile)

        if cell == 'P':
          player_sprite = Player((x, y))
          self.player.add(player_sprite)

  def scroll_X(self):
    player = self.player.sprite
    player_x = player.rect.centerx
    direction_x = player.direction.x

    if player_x < (screen_width / 4) and direction_x < 0:
      self.world_shift = 7
      player.speed = 0
    elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
      self.world_shift = -7
      player.speed = 0
    else:
      self.world_shift = 0
      player.speed = 7

  def horizontal_movement_collision(self):
    player = self.player.sprite
    player.rect.x += player.direction.x * player.speed  #apply horz movement

    # check through all sprite to see if collision
    for sprite in self.tiles.sprites():
      # if collision, determine what position player is moving to determine side of collision
      if sprite.rect.colliderect(player.rect):
        if player.direction.x < 0: # left col
          player.rect.left = sprite.rect.right
        elif player.direction.x > 0: # right col
          player.rect.right = sprite.rect.left

  def vertical_movement_collision(self):
    player = self.player.sprite
    player.apply_gravity()  #apply vert movement

    # check through all sprite to see if collision
    for sprite in self.tiles.sprites():
      # if collision, determine what position player is moving to determine side of collision
      if sprite.rect.colliderect(player.rect):
        if player.direction.y > 0:  # top col
          player.rect.bottom = sprite.rect.top
          player.direction.y = 0  # cancel gravity
        elif player.direction.y < 0:  #bottom col
          player.rect.top = sprite.rect.bottom
          player.direction.y = 0  # cancel jump (-y direction movement)

  def run(self):
    #player
    self.tiles.update(self.world_shift)
    self.tiles.draw(self.display_surface)
    self.scroll_X()

    #player
    self.player.update()
    self.horizontal_movement_collision()
    self.vertical_movement_collision()
    self.player.draw(self.display_surface)
