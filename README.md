# GeneticAlgorithmLib

A library focused on providing simple and generic functions and classes to
help build a genetic algorithm.

# How to use (quick start)

To use this library, you have to code a class that inherit from Agent in a
new python file
(let us call them respectively AgentClassChild and myCode.py),
with the specific functions you need (such as get_offspring, get_score)
that depend from the problem you want to solve.
Then, in a main.py, write :


```python
from myCode import AgentClassChild

# AgentClassChild being a class inhereting from Agent,
# with your specific requirements

P = Population(AgentClassChild)
S = P.evolve()
print(S)
```


and execute it.
While it is running, you can execute in your shell :


```shell
tail -f code.log
```


to check how the program is going.
