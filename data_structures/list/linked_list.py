class Link:
    def __init__(self, data=None):
        self.data = data
        self.link = None
        self.back = None

    def display(self):
        print(f"{self.data}", end = '')

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None

    def preappend(self, data):
        new_link = Link(data=data)

        if not self.is_empty():
            new_link.link = self.first
            self.first.back = new_link
        else:
            self.last = new_link
            
        self.first = new_link

        return f"Preappend {data}"

    def append(self, data):
        if self.is_empty():
            self.preappend(data)
        else:
            new_link = Link(data=data)
            self.last.link = new_link
            new_link.back = self.last
            self.last = new_link

        return f"Append {data}"

    def peek(self, location):
        return location.link

    def push(self, data):
        self.append(data=data)

    def pop(self):
        if self.is_empty():
            print("Pop of empty list")
            return None

        temp = self.last        
        self.last = self.last.back
        if self.last:
            self.last.link = None
        else:
            self.first = None
        print(f"Pop {temp.data}")
        return temp.data

    def insert(self, data, index=None):
        if not index or index == self.length() or self.is_empty():
            self.push(data=data)
        elif index == 0:
            self.preappend(data=data)
        elif index > self.length() - 1:
            print("Index out of range")
            return None
        else:
            position = self.first
            counter = 0
            while counter < index:
                position = position.link
                counter += 1

            new_link = Link(data=data)
            back = position.back
            back.link = new_link
            new_link.back = back
            new_link.link = position
            position.back = new_link
            print(f"Insert {new_link.data} at index {counter}")

    def update(self, data, index):
        if not index or index > self.length() - 1:
            print("Index out of range")
            return None

        position = self.first
        counter = 0
        while counter < index:
            position = position.link
            counter += 1

        position.data = data
        print (f"Update element({counter}) = {data}")
        return "Success"        


    def delete(self, index=None):
        if self.is_empty() or index > self.length() - 1:
            print("Index out of range")
            return None

        elif not index or index == self.length() - 1:
            self.pop()

        elif index == 0:
            location = self.first
            link = location.link
            self.first = link
            link.back = None
            return location.data
        
        else:
            count = 0
            location = self.first
            while count < index:
                count += 1
                location = location.link

            link = location.link
            back = location.back
            link.back = back
            back.link = link
            return location.data

    def __call__(self, index):
        if index > self.length() - 1:
            print("Index out of range")
            return None
        else:
            count = 0
            position = self.first
            while count < index:
                position = position.link
                count += 1

            return position.data
            
    def length(self):
        if self.is_empty():
            return 0

        count = 1
        location = self.first
        while location.link:
            count += 1
            location = location.link
        return count

    def display(self):
        if self.is_empty():
            print("[]")

        else:
            location = self.first
            print("[", end="")
            while location is not None:
                location.display()
                if location.link:
                    print(", ", end="")
                location = location.link

            print("]")
