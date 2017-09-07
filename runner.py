import world as w

SIZE = 10
NUMINDIVIDUALS = 10
NUMFOODS = 20
NUMFIRES = 20


def main():
    world = w.World(10)
    world.from_configs(SIZE, NUMINDIVIDUALS, NUMFOODS, NUMFIRES)
    world.run()

main()
