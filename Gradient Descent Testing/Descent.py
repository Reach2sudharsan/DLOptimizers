from abc import ABC, abstractmethod

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
