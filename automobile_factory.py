import car
import array_queue

def unload_shipment(filename,belt):
    #open the file
    with open(filename) as file:
        for line in file:
            part = line.strip()
            belt.enqueue(part)

def install_part(car,my_belt,their_belt):
    if not my_belt.is_empty():
        #remove the next part from my_belt
        part = my_belt.dequeue()

        if car.needs_part(part):
            car.install(part)
        else:
            their_belt.enqueue(part)

    return car.is_complete()

#12.31
def assemble_cars_1(worker_belt, coworker_belt):
    protocol = car.Car("BMW", car.PROTOCOL)

    while True:
        if install_part(protocol, worker_belt, coworker_belt):
            print(repr(protocol))
            break

#12.32
def assemble_cars_2(worker_belt, coworker_belt):
    protocol = car.Car("BMW", car.PROTOCOL)
    automobile = car.Car("AUDI", car.AUTOMOBILE)

    while not worker_belt.is_empty() or not coworker_belt.is_empty():
        if install_part(protocol, worker_belt, coworker_belt):
            print("Completed:", repr(protocol))
            protocol = car.Car("BMW", car.PROTOCOL)
        
        if install_part(automobile, coworker_belt, worker_belt):
            print("Completed:", repr(automobile))
            automobile = car.Car("AUDI", car.AUTOMOBILE)

import node_stack

#12.33
def assemble_cars_3(worker_belt, coworker_belt):
    protocol = car.Car("BMW", car.PROTOCOL)
    astromech = car.Car("AUDI", car.AUTOMOBILE)

    cargo_ship = []
    shipping_container = node_stack.Stack()

    while not worker_belt.is_empty() or not coworker_belt.is_empty():
        if install_part(protocol, worker_belt, coworker_belt):
            print("Completed:", repr(protocol))

            #load onto shipping container
            #first make sure shipping container not full (can only fit 5)
            if len(shipping_container) >= 5:
                #put the full container on ship
                cargo_ship.append(shipping_container)

                #create a new empty container
                shipping_container = node_stack.Stack()

            shipping_container.push(protocol)

            protocol = car.Car("BMW", car.PROTOCOL)
        
        if install_part(astromech, coworker_belt, worker_belt):
            print("Completed:", repr(astromech))

            #load onto shipping container
            #first make sure shipping container not full (can only fit 5)
            
            if len(shipping_container) >= 5:
                #put the full container on ship
                cargo_ship.append(shipping_container)

                #create a new empty container
                shipping_container = node_stack.Stack()

            shipping_container.push(automobile)

            automobile = car.Car("AUDI", car.AUTOMOBILE)

    if not shipping_container.is_empty():
        cargo_ship.append(shipping_container)

    return cargo_ship

def ship(shipment):
    container_number = 0
    for container in shipment:
        container_number += 1
        print("Unpacking shipping container #", container_number, "...", sep="")
        while not container.is_empty():
            droid = container.pop()
            print("  ", droid)

def main():
    belt_1 = array_queue.Queue()
    belt_2 = array_queue.Queue()
    unload_shipment("parts_0010_0005.txt",belt_1)
    # unload_shipment("parts_0005_0005.txt",belt_2)
    # print(belt_1)

    # proto_car = car.Car("BMW",cars.PROTOCOL)

    # install_part(proto_car,belt_1,belt_2)

    # assemble_cars_1(belt_1,belt_2)

    # assemble_cars_2(belt_1,belt_2)

    my_cargo_ship = assemble_cars_3(belt_1,belt_2)

    container_number = 0
    for container in my_cargo_ship:
        container_number += 1
        print("Unpacking shipping container #", container_number, "...", sep="")

        while not container.is_empty():
            car = container.pop()
            print(car)

    #ship(my_cargo_ship)
    #print(my_cargo_ship[0])

 

if __name__ == "__main__":
    main()

    # C3PO = BMW
    # R2D2 = AUDI