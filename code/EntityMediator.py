from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:

    @staticmethod
    #Veiricar limite da tela e destruir as naves que sairem (OPTIMIZATION)
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0




    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_test = entity_list[i]
            EntityMediator.__verify_collision_window(entity_test)


    # destruction entity
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <=0:
                entity_list.remove(ent)