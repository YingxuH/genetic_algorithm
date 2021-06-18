### Genetic Algorithm 

#### Installation
    pip install genetic_algorithm

#### Use Cases
    from genetic_algorithm import GeneticAlgorithm

    def func(a,b,c,d):
    return -(a-1)**2 - (b-3)**2 - (c-5) ** 2 - len(d)
    
    
    def fitness(params):
    return func(**params)
    
    
    param_space = {"a": {'type': 'float', 'range':[0, 2]},
    "b": {'type': 'float', 'range':[1, 5]},
    "c": {'type': 'int', 'range':[3, 7]},
    "d": {'type': 'object', 'range':['ab', 'abc', 'abcd', 'a']}}
    
    ga = GeneticAlgorithm(model=fitness,
    param_space=param_space,
    pop_size=100,
    parent_pool_size=5,
    max_iter=100,
    mutation_prob=0.2,
    max_stop_rounds=5)
    
    result = ga.evolve()
    print(result)