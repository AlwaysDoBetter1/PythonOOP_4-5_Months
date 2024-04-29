'''
A queue is an abstract data type with a first-in, first-out access discipline to elements. Adding an element is
possible only at the end of the queue, selecting only from the beginning of the queue, and the selected element
is removed from the queue.

Implement a Queue class that describes a queue. When instantiated, the class must accept an arbitrary number of
positional arguments, each of which is an element of the queue. The order of the arguments determines the order
of the elements in the queue, that is, the first argument is the first element of the queue, the second argument
is the second element of the queue, and so on.

The Queue class must have two instance methods:

add() - a method that takes an arbitrary number of positional arguments and adds them to the end of the queue in the
order in which they were passed
pop() is a method that removes the first element from the queue and returns it. If the queue is empty, the method
should return None
An instance of the Queue class must have the following informal string representation:

<first queue element> -> <second queue element> -> <third queue element> -> ...
In addition, instances of the Queue class must support comparison operations between themselves using the == and !=
operators. Two queues are considered equal if they are of equal length and contain equal elements in equal positions.

Also, instances of the Queue class must support the addition operation between themselves using the + and += operators:

the result of addition using the + operator must be a new instance of the Queue class, representing a queue with all
the elements of the original queues: first all the elements of the left queue, then all the elements of the right queue
The result of addition using the += operator must be a left instance of the Queue class, representing a queue to which
all the elements of the right queue have been added
Finally, an instance of the Queue class must support a bitwise right shift operation by an integer n using the >>
operator, which must result in a new instance of the Queue class representing the original queue minus the first n
elements. If n is greater than or equal to the length of the original queue, the result must be an instance of the
Queue class representing an empty queue.
'''


class Queue:
    def __init__(self, *args):
        self.que = list(args)

    def add(self, *args):
        self.que += args

    def pop(self):
        if self.que:
            return self.que.pop(0)
        else:
            return None

    def __str__(self):
        return " -> ".join(map(str, self.que))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.que == other.que
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.__class__(*(self.que + other.que))
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.que += other.que
            return self
        else:
            return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if len(self.que) > n:
                return self.__class__(*self.que[n:])
            else:
                return ""
        else:
            return NotImplemented

# Example:
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

# Output:
# 1 -> 2 -> 3 -> 4 -> 5
