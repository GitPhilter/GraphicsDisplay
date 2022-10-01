"""
A class that has a small and simple API for displaying images on the screen.
Uses pygame-lib for simple 2D graphics.
"""

import pygame
import logging


def _init_pygame(width, height, window_caption):
    (modules_success, modules_fail) = pygame.init()
    if modules_fail > 0:
        logging.error("%d pygame modules could not be loaded!", modules_fail)
        return None
    else:
        logging.debug("All pygame modules loaded successfully")
        # create window
        win = pygame.display.set_mode((width, height), pygame.NOFRAME)
        pygame.display.set_caption(window_caption)
        return win


class Display:
    background_color = (0, 0, 0)  # black as default background color
    image_dict = {}
    logger = logging.getLogger(__name__)

    def __init__(self, width, height, window_caption):
        self.logger.setLevel(logging.INFO)
        self.width = width
        self.height = height
        self.win = _init_pygame(width, height, window_caption)
        if self.win is None:
            self.logger.critical("pygame window could not be initialized!")

    def clear(self):
        self.logger.debug("Filling the screen with background_color: {}".format(self.background_color))
        self.win.fill(self.background_color)

    def add(self, image_path, image_key):
        self.logger.debug(("Adding image to the image_dict: {}, with image_key '{}'".format(image_path, image_key)))
        if image_key in self.image_dict.keys():
            logging.warning("The image_key '{}' already exists in the image_dict, "
                            "and cannot be added again.".format(image_key))
            return
        self.image_dict[image_key] = pygame.image.load(image_path)

    def put(self, image_key, x_pos, y_pos):
        self.logger.debug(("Putting image '{}' to position ({}, {})".format(image_key, x_pos, y_pos)))
        self.win.blit(self.image_dict[image_key], (x_pos, y_pos))

    def refresh(self):
        self.logger.debug("Refreshing the screen.")
        pygame.event.pump()
        pygame.display.update()

    def get_image_dict(self):
        return self.image_dict

    def image_key_exists(self, image_key):
        if image_key in self.image_dict.keys():
            return True
        return False

    def set_log_level(self, log_level):
        self.logger.info("Setting log-level to {}".format(log_level))
        self.logger.setLevel(log_level)

    def get_events(self):
        return pygame.event.get()

