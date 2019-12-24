import random
from copy import copy, deepcopy
from genetic_algorithm.Individual import Individual


class Generation(object):
    def __init__(self, model=None, inds=None, parent_pool_size=None, pop_size=None, arg_lst=None):
        self.model = model
        # expecting list
        self.inds = inds
        self.parent_pool_size = parent_pool_size
        self.pop_size = pop_size
        self.arg_lst = arg_lst

        self.parents = None
        self.best_ind = None

    def set_model(self, model):
        self.model = model

    def set_inds(self, inds):
        self.inds = inds

    def get_model(self):
        return self.model

    def get_inds(self):
        return self.inds

    def get_best_ind(self):
        return self.best_ind

    def get_best_fitness(self):
        return self.best_ind.get_fitness()

    def get_best_gene_set(self):
        return self.best_ind.get_gene_set()

    def best_gene_set_to_print(self):
        return self.best_ind.get_gene_set_to_print()

    def calculate_fitness(self):
        for ind in self.inds:
            fitness = self.model(ind.get_gene_set_to_print())
            ind.set_fitness(fitness)

    def select(self):
        self.calculate_fitness()
        self.inds.sort(reverse=True)
        self.parents = self.inds[:self.parent_pool_size]
        self.best_ind = self.inds[0]

    # TODO: shift implementation to individual
    def crossover(self):
        if self.parents is None:
            print("generation haven't been selected")
            self.select()

        offspring = []

        for k in range(self.pop_size-self.parent_pool_size):
            # First parent to mate.

            parent1 = self.parents[k % self.parent_pool_size]
            # randomly select half of the parameters and set to zeros.
            args_parent1_gene = random.sample(self.arg_lst, len(self.arg_lst) // 2)

            # TODO: shift to individual implementation
            parent1_gene = {key: copy(value) for key, value in parent1.get_gene_set().items() if key in args_parent1_gene}

            # Index of the second parent to mate.
            parent2 = self.parents[(k + 1) % self.parent_pool_size]
            # randomly select half of the parameters and set to zeros.
            args_parent2_gene = [x for x in self.arg_lst if x not in args_parent1_gene]
            parent2_gene = {key: copy(value) for key, value in parent2.get_gene_set().items() if key in args_parent2_gene}

            # create current offsprint as the summation of the two parents.
            new_gene_set = {**parent1_gene, **parent2_gene}
            new_individual = Individual(gene_set=new_gene_set)

            offspring.append(new_individual)

        # add parent to the next gen
        offspring.extend(self.parents)
        return Generation(model=self.model, inds=offspring, parent_pool_size=self.parent_pool_size,
                          pop_size=self.pop_size, arg_lst=self.arg_lst)

    def mutate(self, mutation_prob):
        for ind in self.inds:
            ind.mutate(mutation_prob)



