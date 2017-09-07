import random
import thing
import numpy

TIME_UNIT = 1
FITNESS_UNIT = 1
MATURITY = TIME_UNIT * 50
LIFESPAN = TIME_UNIT * 50
BASE_FITENESS = FITNESS_UNIT * 10


class World:
    def __init__(self, iterations):
        self.iterations = iterations
        self.representation = None

    def from_configs(self, size, numindividuals, numfoods, numfires):
        self.representation = numpy.empty(size**2, dtype=object)
        i = 0
        while i < self.representation.size:
            self.representation[i] = []
            i += 1
        self.add_stuff(numindividuals, numfoods, numfires)

    def add_stuff(self, numindividuals, numfoods, numfires):
        sample = random.sample([x for x in range(len(self.representation))], numindividuals + numfoods + numfires)
        random.shuffle(sample)
        slot = 0
        i = 0
        while i < numindividuals:
            location = sample[i]
            self.representation[location].append(thing.Individual(BASE_FITENESS, location, slot, LIFESPAN))
            i += 1
        while i < numindividuals + numfoods:
            location = sample[i]
            self.representation[location].append(thing.Food(BASE_FITENESS, location, slot, MATURITY))
            i += 1
        while i < numindividuals + numfoods + numfires:
            location = sample[i]
            self.representation[location].append(thing.Fire(BASE_FITENESS, location, slot))
            i += 1

    def visualize(self):
        pass

    def run(self):
        i = 0
        while i < self.iterations:
            j = 0
            while j < self.representation.size:
                for resident in self.representation[j]:
                    if isinstance(resident, thing.Food):
                        resident.update(self.representation)
                    if isinstance(resident, thing.Individual):
                        resident.update(self.representation)
                    if isinstance(resident, thing.Moveable):
                        resident.move(self.representation)
                    if isinstance(resident, thing.Evolvable):
                        resident.try_mate(self.representation)
                j += 1
            i += 1

