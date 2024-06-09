class Knapsack:
    value = 0
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.empty()

    def print(self):
        for row in self.knapsack:
            print(row)


    def greedy(self, items_):
        items = items_[:]
        for item in items:
            self.addItem(item)
    def aproksymacyjnyI(self, items_):
        items = items_[:]
        #sortowanie nierosnąco względem wartości
        items.sort(key=lambda x: int(x[2]), reverse=True)
        for item in items:
            self.addItem(item)

    def aproksymacyjnyII(self, items_):
        items = items_[:]
        #sortowanie nierosnąco względem stosunku wartości do objętości
        items.sort(key=lambda x: int(x[2])/(int(x[0]) * int(x[1])), reverse=True)
        for item in items:
            self.addItem(item)



    def addItem(self, item):
        for a in range(self.width):
            for i in range(self.height):
                if self.knapsack[a][i] == '0':
                    if int(item[0]) <= self.width - a and int(item[1]) <= self.height - i:
                        self.value += int(item[2])
                        for x in range(int(item[0])):
                            for y in range(int(item[1])):
                                self.knapsack[a + x][i + y] = item[2]
                        return

    def empty(self):
        self.knapsack = []
        self.value = 0
        for a in range(self.height):
            self.knapsack.append(['0'] * int(self.width))











