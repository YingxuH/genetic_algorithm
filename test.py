from genetic_algorithm.main import genetic_optimisation

def func(a,b,c):
    return -(a-1)**2 - (b-3)**2 - (c-5) ** 2

def fitness(params):
    return func(**params)

param_space = {"a": [0, 2], "b": [1, 5], "c": [3,7]}

genetic_optimisation(input_model=fitness, param_space=param_space, pop_size=100, num_parents=3,
                     max_num_generations=100, mutation_prob=0.2, stoping_rounds=5, integer_params=[])