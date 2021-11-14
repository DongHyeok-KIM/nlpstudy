

from multiprocessing import Pool
import multiprocessing as mp





import matplotlib.pyplot as plt
import random



def process_B():
    def random_walk_():

        random.seed(100)

        fig = plt.figure(figsize=(12, 6))

        for i in range(100):
            walk_ = [0]
            for j in range(100):
                walk_.append(random.uniform(-1, 1) + walk_[-1])
            plt.plot(walk_, alpha=0.5)

        # plt.savefig(f'{seed_}.png')
        plt.close(fig)

        return None
    num_cores = 4
    pool = Pool(num_cores)
    pool.map(random_walk_,range(48))