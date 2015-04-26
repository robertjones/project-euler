import heapq
from collections import namedtuple


class Graph:

    def __init__(self, data):
        self.arr = [[int(el) for el in line.split(',')]
                    for line in data.split('\n')[:-1]]
        self.width = len(self.arr[0])
        self.height = len(self.arr)
        self.avg_cost = (sum(sum(el for el in row) for row in self.arr)
                         / (self.width * self.height))

    def neighbours(self, coord):
        x, y = coord
        return [(x + a, y + b) for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]
                if (0 <= x + a < self.width) and (0 <= y + b < self.height)]

    def cost(self, coord):
        x, y = coord
        return self.arr[y][x]


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b, avg_cost):
    return 0


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, graph.cost(start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = graph.cost(start)

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for nxt in graph.neighbours(current):
            new_cost = cost_so_far[current] + graph.cost(nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(goal, nxt, graph.avg_cost)
                frontier.put(nxt, priority)
                came_from[nxt] = current

    Results = namedtuple('Results', ['came_from', 'cost_so_far'])

    return Results(came_from, cost_so_far)

sample_data = """131, 673, 234, 103, 018
          201, 096, 342, 965, 150
          630, 803, 746, 422, 111
          537, 699, 497, 121, 956
          805, 732, 524, 037, 331
          """

file_name = 'p083_matrix.txt'

with open(file_name, 'r') as f:
    data = f.read()

graph = Graph(data)

start = (0, 0)
goal = (graph.width-1, graph.height-1)

result = a_star_search(graph, start, goal)
min_path_sum = result.cost_so_far[goal]

print(min_path_sum)
