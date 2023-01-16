#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 29/12/2022
The aim of this program is to provide a general genetic algorithm
"""

import logging
logging.basicConfig(filename='code.log', level=logging.INFO)


class Agent(object):
    """
    The agent evolves by mutating and being selected.
    """
    def __init__(self):
        self.genes = []

    def get_score(self):
        """
        Returns how much the agent is performing.
        This is what will be maximized.
        """
        return(0)

    def get_offspring(self):
        """
        Returns a mutated version of the agent.
        """
        pass


class Population(object):
    """
    A group of agents of set size.
    Can evolve through mutations and selection.
    """
    def __init__(self, Agent_type, size=100):
        self.size = size
        self.population = [Agent_type() for _ in range(size)]
        self.history = []

    def get_best_agent(self):
        """
        Returns the best agent of the population given their scores.
        """
        scores = [a.get_score() for a in self.population]
        best_index = scores.index(max(scores))
        best_agent = self.population[best_index]
        return(best_agent)

    def evolve(self, nb_gen=100):
        """
        Evolves the population through a set number of generations.
        Returns the best agent at the end.
        Logs all the best agents of each generation.
        """
        logging.info(f"Initiating evolution : {nb_gen} generations to go")
        for i in range(nb_gen):
            best_agent = self.get_best_agent()
            self.history.append(best_agent)
            logging.info(f"Best agent of generation {i} :\n{best_agent}")
            self.population = [best_agent.get_offspring()
                               for _ in range(self.size-1)]
            self.population += [best_agent]
        logging.info(f"\nBest agent at the end of evolution :\n{best_agent}")
        return(best_agent)

