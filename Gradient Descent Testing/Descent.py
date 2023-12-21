from abc import ABC, abstractmethod
from matplotlib import pyplot as plt


class Descent(ABC):

    @abstractmethod
    def plot_progress(self):
        pass

    @abstractmethod
    def get_next_step(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


# TODO: maybe @abstractproperty with getters and setters...?


class NaiveGD(Descent):
    def __init__(self, learning_rate, dimension):
        self.learning_rate = learning_rate
        self.dimension = dimension
        self.data = [] # TODO: the actual dimensions and this should be an ndarray fs lol

    def plot_progress(self, *args, **kwargs):
        assert 1 <= self.dimension <= 3
        plt.plot(self.data, *args, **kwargs) # TODO: the actual plotting! also this will prob all need to be 2D or 3D now