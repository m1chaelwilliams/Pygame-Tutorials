import pygame

class EventHandler:
    def __init__(self) -> None:
        EventHandler.events = pygame.event.get()
    def run():
        EventHandler.events = pygame.event.get()
    def clicked() -> bool:
        for e in EventHandler.events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False