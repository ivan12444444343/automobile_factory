PROTOCOL = "Protocol"
AUTOMOBILE = "Automobile"

PROTOCOL_PARTS = ["battery", "radiator", "brakes", "axle", 
    "alternator", "air filter"]

AUTOMOBILE_PARTS = ["bumper", "transmisson", "ignition", "muffler", 
    "hood"]

class Car:
    __slots__ = ["__serial_number", "__type", "__parts"]

    def __init__(self,serial_number,type=PROTOCOL):
        self.__serial_number = serial_number
        self.__type = type
        self.__parts = {}
        if type == PROTOCOL:
            parts_list = PROTOCOL_PARTS
        elif type == AUTOMOBILE:
            parts_list = AUTOMOBILE_PARTS
        else:
            raise TypeError("Unknown car type: " + str(type))
        
        for part in parts_list:
            self.__parts[part] = False

    def __repr__(self):
        string = self.__type + " Car:\n" + \
        "serial number: " + str(self.__serial_number) + "\n"
        
        #now go through the parts list
        for part in self.__parts:
            if self.__parts[part]:
                status = "installed"
            else:
                status = "missing"
            
            string += part + ": " + status + "\n"

        return string
    
    def __str__(self):
        #return serial number and is_complete
        string = str(self.__serial_number)
        if self.is_complete():
            string += ": is complete"
        else:
            string += ": is not complete"

        return string

    def needs_part(self,part):
        if part not in self.__parts:
            return False
        else:
            #now we can check if it is not installed or not
            return not self.__parts[part]
        
    def install(self,part):
        #first make sure this part is even needed for this type of droid
        if part not in self.__parts:
            raise ValueError("Part not compatible with this car type")

        #make sure it isn't already installed:
        if self.__parts[part]:
            raise ValueError("Part already installed")
        
        self.__parts[part] = True

    def is_complete(self):
        for part in self.__parts:
            if not self.__parts[part]:
                return False
        return True

def main():
    astro_car = Car("AUDI",AUTOMOBILE)
    print(repr(astro_car))
    print(astro_car)

if __name__ == "__main__":
    main()
               