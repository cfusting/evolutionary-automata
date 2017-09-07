from abc import ABC, abstractmethod
import world
import utils
import numpy
import random


class Thing(ABC):
    def __init__(self, fitness, location, slot):
        self.fitness = fitness
        self.location = location
        self.slot = slot
        self.age = 0

    @abstractmethod
    def interact(self, other):
        pass


class Evolvable(ABC):
    @abstractmethod
    def try_mate(self):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, representation):
        pass


class Living(ABC):
    def __init__(self):
        self.maturity = 0
        self.lifespan = 0

    @abstractmethod
    def update(self, representation):
        self.maturity += world.TIME_UNIT
        self.lifespan -= world.TIME_UNIT


class Fire(Thing):
    def __init__(self, fitness, location, slot):
        super(Fire, self).__init__(fitness, location, slot)

    def interact(self, other):
        if isinstance(other, Individual):
            other.fitness -= world.FITNESS_UNIT


class Food(Thing, Living):
    def __init__(self, fitness, location, slot, maturity):
        super(Food, self).__init__(fitness, location, slot)
        Living.__init__(self)
        self.maturity = maturity
        self.active = True

    def interact(self, other):
        if isinstance(other, Individual) and self.active:
            other.fitness += world.FITNESS_UNIT
            self.active = False
            self.maturity = 0

    def update(self, representation):
        super(Food, self).update(representation)
        if self.maturity >= world.MATURITY:
            self.active = True


class Individual(Thing, Moveable, Living):
    def __init__(self, fitness, location, slot, lifespan):
        super(Individual, self).__init__(fitness, location, slot)
        Living.__init__(self)
        self.lifespan = lifespan

    def interact(self, other):
        pass

    def try_mate(self):
        pass

    def move(self, representation):
        super(Individual, self).move(representation)
        utils.move_in_matrix(self, representation.size, numpy.random.choice([0, 1]), numpy.random.choice([1, -1]))
        representation[self.location].append(self)
        self.slot = len(representation[self.location])
        del representation[self.location][self.slot]

    def update(self, representation):
        super(Individual, self).update(representation)
        if self.lifespan > world.LIFESPAN:
            del representation[self.location][self.slot]


class EvolvingIndividual(Individual, Evolvable):
    def __init__(self, fitness, location, slot, lifespan):
        super(EvolvingIndividual, self).__init__(fitness, location, slot, lifespan)
