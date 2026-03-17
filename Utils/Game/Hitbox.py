import pygame, Global

class hitbox(pygame.sprite.Sprite):
    def __init__(self, pos:pygame.Vector2, size:pygame.Vector2, lifetime=None, visualize=False, collisionGroup="default"):
        super().__init__()
        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.visualize = visualize
        self.lifetime = lifetime
        self.collisionGroup = collisionGroup

        # visualization surface
        self.surface = pygame.Surface((size.x, size.y), pygame.SRCALPHA)
        self.surface.fill((255, 0, 0, 128))

        self.image = pygame.Surface((size.x, size.y), pygame.SRCALPHA)
        self.image.fill((255, 0, 0, 0))

    def update(self, pos=None):
        if pos is not None:
            self.rect.topleft = pos

        if self.visualize:
            Global.screen.blit(self.surface, self.rect.topleft)

        if self.lifetime is not None:
            self.lifetime -= Global.dt
            if self.lifetime <= 0:
                self.kill()

    def isAlive(self):
        return self.lifetime is None or self.lifetime > 0

    def collide(self, other):
        # group rule
        if not (
            self.collisionGroup == other.collisionGroup
        ):
            return False

        return self.rect.colliderect(other.rect)
        

class Hitbox:
    def __init__(self):
        self.hitboxGroup = pygame.sprite.Group()

    def new(self, *args, **kwargs):
        newHB = hitbox(*args, **kwargs)
        self.hitboxGroup.add(newHB)
        return newHB
    
    def update(self):
        self.hitboxGroup.draw(Global.screen)
        self.hitboxGroup.update()

        collisions = pygame.sprite.groupcollide(
            self.hitboxGroup,
            self.hitboxGroup,
            False,
            False
        )

        checked = set()
        for hb, others in collisions.items():
            for other in others:
                if hb is other:
                    continue

                pair = tuple(sorted((id(hb), id(other))))
                if pair in checked:
                    continue
                checked.add(pair)

                if hb.collide(other):
                    if not (
                        self.collisionGroup == other.collisionGroup
                    ):
                        continue
                    print("collision detected")