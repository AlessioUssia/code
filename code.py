import queue


class Coda_propritaria:
    def __init__(self):
        self._lista = []

    def put(self, valore):
        self._lista.append(valore)

    def pop(self):
        """
        Restituisce il valore minimo presente nella lista e lo cancella dalla lista stessa
        :return:
        """
        "[2,4,1,9]"
        "enumerate restituisce [(0,2),(1,4),(2,1),(3,9)]"
        "[2,4,1,9] è la lista su cui calcolo il minimo"

        (pos_min, val_min) = min(enumerate(self._lista), key=lambda t: t[1]) #---> il minimo viene fatto sul secondo elemento di
                                                                        # ogni tupla ---> esce la tupla (2,1)
        self._lista.pop(pos_min)
        return val_min


d = Coda_propritaria() #---> stesso comportamento

d.put(3)
d.put(6)
d.put(9)
print(d.pop())
d.put(1)
print(d.pop())
print(d.pop())
print(d.pop())

c = queue.PriorityQueue()

c.put((2, "Paolo"))
c.put((1, "Giulia"))
c.put((2, "Antonio"))
print(c.get())
c.put((1, "Anna"))
print(c.get())
print(c.get())
print(c.get())
