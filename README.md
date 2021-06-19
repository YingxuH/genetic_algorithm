### Genetic Algorithm 

A black-box optimization package published in [pypi](https://pypi.org/project/genetic-algorithm/).

#### Installation
    pip install genetic_algorithm

#### Example

The original example code can be found in [test.py](./test.py).

    import numpy as np
    import matplotlib.pyplot as plt
    from genetic_algorithm import GeneticAlgorithm

Define the function to be optimized  

    x = np.linspace(0, 5, 1000)
    
    ground_truth = x**3 - 2*(x**2) + 1
    
    
    def func(a,b,c):
    return x**a - b*(x**2) + c

Declare the fitness function as the negative RMSE of the predicted 
values.

    def fitness(params):
    return -np.sqrt(np.mean((ground_truth-func(**params))**2))
        
The parameter space to be searched should come as a dictionary as follows:

    param_space = {"a": {'type': 'float', 'range':[0, 5]},
    "b": {'type': 'float', 'range':[-1, 5]},
    "c": {'type': 'int', 'range':[0, 3]}
    }

Run genetic algorithm.

    ga = GeneticAlgorithm(model=fitness,
                        param_space=param_space,
                        pop_size=100,
                        parent_pool_size=10,
                        keep_parent=False,
                        max_iter=100,
                        mutation_prob=0.3,
                        crossover_prob=0.7,
                        max_stop_rounds=5,
                        verbose=False)
    
Get the best parameters as well as the history. 

    result = ga.evolve()
    print(result)

Visualize the difference between predicted and ground truth data: 

    predicted = func(**result["best params"])
    plt.scatter(x, ground_truth, s=3, label="ground truth")
    plt.scatter(x, predicted, s=3, c='r', label="predicted")
    plt.legend(loc='upper left')
    plt.show()

population size = 100             |  population size = 500
:-------------------------:|:-------------------------:
![](./img/example1.png)  |  ![](./img/example2.png)

There is still quite some difference between the predicted ones and the ground truth. 
If the population size goes 100 to 500, the optimizer is then working better than before. There are other parameters such as 
cross-over rate and mutation rate which can also affect the optimization performance. 
