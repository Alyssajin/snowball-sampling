import random
import networkx as nx
from matplotlib import pyplot as plt


class Queue():

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):

        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            exit()

    # Getting the size of the queue
    def size(self):
        return len(self.queue)

    # printing the elements of the queue
    def printQueue(self):
        return self.queue


class Snowball():

    def __init__(self):
        self.G1 = nx.Graph()

    def draw_graph(self):
        plt.figure()
        nx.draw(self.G1, with_labels=True)
        plt.show()

    def snowball(self, G, size, k, j):
        q = Queue()
        list_nodes = list(G.nodes())

        m = k - 1
        dictt = set()
        while (m):
            id = random.sample(list(G.nodes()), 1)[0]
            q.enqueue(id)
            m = m - 1

        while len(self.G1.nodes()) <= size:
            if q.size() > 0:
                id = q.dequeue()
                self.G1.add_node(id)

                if id not in dictt:
                    dictt.add(id)
                    list_neighbors = list(G.neighbors(id))
                    if len(list_neighbors) >= k:
                        for x in list_neighbors[:k - 1]:
                            q.enqueue(x)
                            j += 1
                    elif len(list_neighbors) < k and len(list_neighbors) > 0:
                        for x in list_neighbors:
                            q.enqueue(x)
                            j += 1
                else:
                    continue
            else:
                initial_nodes = random.sample(list(G.nodes()) and list(dictt), k)
                no_of_nodes = len(initial_nodes)
                for id in initial_nodes:
                    q.enqueue(id)

        return self.G1


def main():
    G = nx.karate_club_graph()
    size = 10
    k = 4
    s = Snowball()
    s.snowball(G, size, k, 1)


if __name__ == "__main__":
    main()
