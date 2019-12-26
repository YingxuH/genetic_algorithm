from genetic_algorithm import GeneticAlgorithm
# import genetic_algorithm

# from genetic_algorithm import genetic_optimization
#


def func(a,b,c,d):
    return -(a-1)**2 - (b-3)**2 - (c-5) ** 2 - len(d)


def fitness(params):
    return func(**params)


param_space = {"a": {'type': 'float', 'range':[0, 2]},
               "b": {'type': 'float', 'range':[1, 5]},
               "c": {'type': 'int', 'range':[3, 7]},
               "d": {'type': 'object', 'range':['qwe', 'qw', 'a', '234r']}}
#
# ga = genetic_optimization(input_model=fitness, param_space=param_space, pop_size=100, num_parents=3,
#                      max_num_generations=100, mutation_prob=0.2, stoping_rounds=5, integer_params=[])['best params']
# print(ga)
# from genetic_algorithm.Individual import Individual
#
# ind_1 = Individual(fitness=1)
# ind_2 = Individual(fitness=20)
# ind_lst = [ind_2, ind_1]
#
# ind_lst.sort(reverse=True)
#
# print([x.get_fitness() for x in ind_lst])

ga = GeneticAlgorithm(model=fitness,
                      param_space=param_space,
                      pop_size=100,
                      parent_pool_size=5,
                      max_iter=100,
                      mutation_prob=0.2,
                      max_stop_rounds=5)

ga.evolve()
