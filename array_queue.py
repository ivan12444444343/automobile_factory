import arrays

class Queue:
    __slots__ = ['__elements','__front','__back','__size']

    def __init__(self,size=3):
        self.__elements = arrays.Array(size)
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def __str__(self):
        string = ''
        i = self.__front
        while i != self.__back:
            string += str (self.__elements [i]) + ', '
            i = (i + 1) % len (self.__elements)
        return '[' + string[:-2] + ']'
    
    def is_empty(self):
        return self.__size == 0
    def size(self):
        return self.__size
    def enqueue(self, value):
        # Suppose this is our current queue. b, and c are in line
        # suppose array looks like this as we have added and removed items a bit:
        # [none,b,c,none]
        # front_index = 1 (value = b)
        # back_index = 3 (value = none)

        # we now want to add a "d" to the end of the queue line
        # we will assume _back is stored correctly so we just go ahead and put it there:
        # from our example we want to do: elements[3] = "d"
        self.__elements[self.__back] = value

        #Front will stay the same right!? the person in line stays the same when another joins the line

        #therefore we only need to caluclate a new back.
            #we could make all sorts of if to realize our back index is at length - 1 right??
            #but as a shortcut we can simply use this formula to have it caluclate!
            # self.__back = (self.__back + 1) % len(self.__elements)
            # (3 + 1) % 4 = 0
            # SET IT to to newly calculated value
            # self.__back = 0

        self.__back = (self.__back + 1) % len(self.__elements)

        #increment the size
        self.__size += 1

        #We will still need to eventually check if the cat caught its tail.
        #example: our array = [1,2,3] and we try to enqueue
        #there is no room left we need to expand the array and adjust values
        #we will do this day 3!
        if self.__back == self.__front:
            self.__resize ()

            
    def front(self):
        if self.__size != 0:
            return self.__elements[self.__front]
        else:
            raise IndexError("front not defined")
        
    def back(self):
        if self.__size != 0:
            return self.__elements[self.__back-1]
        else:
            raise IndexError("back not defined")
        
    def dequeue(self):
        if self.__size != 0:
            front = self.__elements[self.__front]
            #now set the current front to none
            self.__elements[self.__front] = None

            #no increment front, wrap around if needed
            self.__front = (self.__front + 1) % len(self.__elements)

            #decrement size
            self.__size -= 1

            return front
        
    def __resize(self):

        new_array_size = self.__size * 2
        new_array = arrays.Array(new_array_size)

        i = 0
        j = self.__front

        for _ in range(self.__size):
            #check to wrap around
            if j == self.__size:
                j = 0
            
            new_array[i] = self.__elements[j]

            j+=1
            i+=1

        self.__elements = new_array
        self.__front = 0
        self.__back = self.__size

        
        

        
def main():
    queue = Queue(3)
    print(queue)

    queue.enqueue("Mary Smith")
    queue.enqueue("Barack Obama")

    print("add some people")
    print(queue)

    # print("Front Peek:",queue.front())
    # print("Back Peek:",queue.back())

    item_removed = queue.dequeue()
    print("Remove From Line:",item_removed)
    print("line after removed:",queue)

    print("add somemore people...")
    queue.enqueue("Stefon Diggs")
    queue.enqueue("pinta Diggs")
    queue.enqueue("Rhyleigh")
    print(queue)

if __name__ == "__main__":
    main()