import random
import numpy as np
import pandas as pd

# genetic algorithm utils
def genetic_optimisation(input_model, param_space, integer_params, pop_size, num_parents, max_num_generations,
                         mutation_prob, stoping_rounds):
    """
    Args:
        param_space: dictionary with key as the parameter name and value as the space for optimisation.
    """

    arg_lst = list(param_space.keys())

    def populate_first_gen(param_space, pop_size, integer_params):
        new_generation = []
        for i in range(pop_size):
            new_individual = {}
            for key, value in param_space.items():
                # TODO: fix the sudo handling
                if not isinstance(value, list):
                    new_individual[key] = value
                elif len(value) == 1:
                    new_individual[key] = value[0]
                if all((isinstance(x, int) or isinstance(x, float)) for x in value):
                    if key in integer_params:
                        new_individual[key] = random.randint(min(value), max(value))
                    else:
                        new_individual[key] = np.random.uniform(min(value), max(value))
                elif all(isinstance(x, str) for x in value):
                    new_individual[key] = np.random.choice(value)
            new_generation.append(new_individual)
        return new_generation

    def crossover(parents, offspring_size):
        offspring = []

        for k in range(offspring_size):
            # First parent to mate.

            parent1 = parents[k % len(parents)]
            # randomly select half of the parameters and set to zeros.
            args_parent1_gene = random.sample(arg_lst, len(arg_lst) // 2)
            parent1_gene = {key: value for key, value in parent1.items() if key in args_parent1_gene}

            # Index of the second parent to mate.
            parent2 = parents[(k + 1) % len(parents)]
            # randomly select half of the parameters and set to zeros.
            args_parent2_gene = [x for x in arg_lst if x not in args_parent1_gene]
            parent2_gene = {key: value for key, value in parent2.items() if key in args_parent2_gene}

            # create current offsprint as the summation of the two parents.
            current_offspring = {**parent1_gene, **parent2_gene}

            offspring.append(current_offspring)
        return offspring

    def mutation(offspring_crossover):
        # Out of mutation_prob, pick one parameter from the param dictionary and alter it by +-10% of its value
        # Mutation changes a single gene in each offspring randomly.
        for idx in range(len(offspring_crossover)):
            # print(offspring_crossover[idx])
            random_signal = random.random()
            if random_signal <= mutation_prob:

                # print('pre mutation: {}'.format(offspring_crossover[idx]))
                random_key = np.random.choice(arg_lst)
                current_value = offspring_crossover[idx][random_key]
                if isinstance(current_value, float) or isinstance(current_value, int):
                    upper_bound = max(param_space[random_key])
                    lower_bound = min(param_space[random_key])
                    if random_key in integer_params:
                        all_values = list(range(min(param_space[random_key]), max(param_space[random_key]) + 1))
                        if len(all_values) > 1:
                            # hard coding avoid error
                            all_values.remove(int(current_value))

                        mutated_value = int(np.random.choice(all_values))
                    else:
                        mutated_value = current_value * (1 + np.random.uniform(-1, 1))

                    mutated_value = min(upper_bound, max(lower_bound, mutated_value))
                elif isinstance(current_value, str):
                    all_choices = param_space[random_key].copy()
                    if len(all_choices) > 1:
                        all_choices.remove(current_value)

                    mutated_value = np.random.choice(all_choices)
                offspring_crossover[idx][random_key] = mutated_value
        return offspring_crossover

    # Creating the initial population.
    current_generation = populate_first_gen(param_space, pop_size, integer_params)

    # stopping criteria
    last_best = None
    still_count = 0
    generation_count = 0

    # best individual_table
    best_table = pd.DataFrame(columns=['fitness', 'params'])

    while still_count < stoping_rounds and generation_count < max_num_generations:
        # Measing the fitness of each chromosome in the population.
        fitness_all = [input_model(params) for params in current_generation]

        # Selecting the best parents in the population for mating.
        fitness_table = pd.DataFrame({'params': current_generation, 'fitness': fitness_all}).sort_values('fitness',
                                                                                                         ascending=False)
        # print(fitness_table)
        parents = fitness_table['params'].iloc[:num_parents].tolist()
        # print(parents)

        # Generating next generation using crossover.
        offspring_crossover = crossover(parents, offspring_size=pop_size - num_parents)

        # Adding some variations to the offsrping using mutation.
        offspring_mutation = mutation(offspring_crossover)

        # Creating the new population based on the parents and offspring.
        current_generation = parents + offspring_mutation

        # record the best individuals
        best_table = best_table.append(fitness_table.iloc[0, :])
        current_best_fitness = fitness_table['fitness'][0]
        current_best_params = fitness_table['params'][0]

        # The best result in the current iteration.
        print("Best fitness : {} with params: {}".format(current_best_fitness, current_best_params))

        if current_best_fitness == last_best:
            still_count += 1
        else:
            still_count = 0
        generation_count += 1
        last_best = current_best_fitness

    best_table = best_table.sort_values('fitness', ascending=False)

    return {"best fitness": best_table['fitness'].iloc[0],
            "best params": best_table['params'].iloc[0],
            "history": best_table}