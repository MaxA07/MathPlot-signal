import numpy as np
import matplotlib.pyplot as plt


class Signal:
    __FREQUENCY, __START, __STOP, __STEP = 5, 0, 10, 0.001

    def __init__(self):
        self.__frequency = Signal.__FREQUENCY
        self.__start = Signal.__START
        self.__stop = Signal.__STOP
        self.__step = Signal.__STEP
        self.t = np.arange(0, 1, 0.001)
        self.y = np.sin(2 * np.pi * 1 * self.t)

    def plot_graph(self):
        self.t = np.arange(self.__start, self.__stop, self.__step)
        self.y = np.sin(2 * np.pi * self.__frequency * self.t)
        plt.plot(self.t, self.y)
        plt.show()

    def get_frequency(self):
        return self.__frequency

    def set_frequency(self, new_frequency):
        self.__frequency = new_frequency


s = Signal()
s.plot_graph()
