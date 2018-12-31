from random import *
from math import cos, pi, sin, sqrt, expm1, e
from itertools import permutations, combinations, product


def make_combinations(size, species):
    combs1, combs2, sub_pops = [], [], []
    combs1 = [x for x in range(size)]
    combs2 = [combs1 for y in range(species)]
    sub_pops = [list(tup) for tup in product(*combs2)]

    return sub_pops


def gen_idx(start, stop):
    x = randrange(start, stop)
    return x


def gen_individual(target):
    new_sample = []
    for i in range(len(target)):
        new_sample.append(str(randrange(0, 2)))

    return new_sample


def init_sub_population(size, target):
    sub_population = []
    for i in range(size):
        sub_population.append(gen_individual(target))

    return sub_population


def init_population(size, target):
    population = []
    for i in range(size):
        population.append(init_sub_population(size, target))

    return population


def mutate(subject):
    if len(subject) <= 0:
        print('error, subject length not valid')
    else:
        for i in range(len(subject)):
            if randrange(0, len(subject)+1) == 1:
                subject[i] = randrange(0, 2)
            else:
                pass

    return subject


def to_decimal(subject):
    return int(''.join(str(s) for s in subject), 2)


def crossover(parent1, parent2):
    child = []
    if len(parent1) and len(parent2) <= 0:
        raise Exception('error, subject length not valid')
    else:
        for i in range(len(parent1)):
            if randrange(0, 2) == 0:
                child.append(parent1[i])
            else:
                child.append(parent2[i])

    return child


def crossover_2pt(parent1, parent2):
    child = []
    length = min(len(parent1), len(parent2))
    cxpt1 = randrange(0, length+1)
    cxpt2 = randrange(0, length+1)
    if cxpt2 == cxpt1:
        cxpt2 += 1
        parent1[cxpt1:cxpt2], parent2[cxpt1:cxpt2] = parent2[cxpt1:cxpt2], parent1[cxpt1:cxpt2]

    elif cxpt2 > cxpt1:
        parent1[cxpt1:cxpt2], parent2[cxpt1:cxpt2] = parent2[cxpt1:cxpt2], parent1[cxpt1:cxpt2]

    else:
        parent1[cxpt2:cxpt1], parent2[cxpt2:cxpt1] = parent2[cxpt2:cxpt1], parent1[cxpt2:cxpt1]


def scaling(subjects, mode):
    dec_subjects = []
    for subject in subjects:
        dec_subjects.append(to_decimal(subject))

    if mode == 'R':
        for i in subjects:
            dec_subjects.append(((i*5.12*2)/65536)-5.12)

        return dec_subjects

    elif mode == 'S':
        for i in subjects:
            dec_subjects.append(((i*1000)/65536)-500)

        return dec_subjects

    elif mode == 'G':
        for i in subjects:
            dec_subjects.append(((i*1200)/65536)-600)

            return dec_subjects

    elif mode == 'A':
        for i in subjects:
            dec_subjects.append(((i*60)/65536)-30)

            return dec_subjects

    else:
        raise Exception('Wrong mode selected')


def Rastringin(subjects):
    fitness = 0
    for i in subjects:
        fitness = fitness + i**2 - 3.0*cos(2*pi*i)

    fitness += 60

    return fitness


def Schwefel(subjects):
    fitness = 0
    for i in subjects:
        fitness = fitness + i * sin(sqrt(i))

    fitness += 4189.829

    return fitness


def Griewank(subjects):
    fitness, a, b = 0, 0, 0
    for i in subjects:
        a += (i**2)/4000
        b *= cos(i/sqrt(i))

    fitness = 1 + a - b

    return fitness


def Ackley(subjects):
    fitness, a, b = 0, 0, 0
    for i in subjects:
        a += i**2
        b += cos(2*pi*i)

    fitness = 20 + e - 20*expm1(-0.2*sqrt(a/30)) - expm1(b/30)

    return fitness


def evaluate_pop(population, combs, mode):
    for i in range(len(combs)):
        subjects = []
        for count, idx in enumerate(combs[i]):
            subjects.append(population[count][idx])
        if mode == 'R':
            for i in subjects:
                dec_subjects.append(((i * 5.12 * 2) / 65536) - 5.12)

            return dec_subjects

        elif mode == 'S':
            for i in subjects:
                dec_subjects.append(((i * 1000) / 65536) - 500)

            return dec_subjects

        elif mode == 'G':
            for i in subjects:
                dec_subjects.append(((i * 1200) / 65536) - 600)

                return dec_subjects

        elif mode == 'A':
            for i in subjects:
                dec_subjects.append(((i * 60) / 65536) - 30)

                return dec_subjects

        else:
            raise Exception('Wrong mode selected')


def CCGA(size, num_species, mode):
    population = []



