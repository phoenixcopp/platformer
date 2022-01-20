from os import walk
import pygame

# cycles through a folder and import image files
def import_folder(path):
  surface_list = []

  for _, __, img_files in walk(path):
    for img in img_files:
      full_path = path + '/' + img
      image_surf = pygame.image.load(full_path).convert_alpha()
      surface_list.append(image_surf)

  return surface_list
