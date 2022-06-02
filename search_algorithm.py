# class for sequential search
class SequentialStringList:

    # constructor, which creates a list
    def __init__(self):

        self.list=[]

    # method to add the element to a list
    def add(self,element):

        self.list.append(element)

    # method to find the element in a list
    def find(self,element):

        for i in self.list:
            if i == element:
                return i

        return None

# class for binary search
class BinaryStringList:

    # constructor, which creates a list
    def __init__(self):

        self.list2=[]
    
    # method to add the element to a list
    def add(self,element):
        self.list2.append(element)

    # method to find the element in a list
    def find(self,element):

        # sorting the list
        self.list2.sort()

        # variables to store the first positon and last position
        first_pos=0
        last_pos=len(self.list2)-1
        flag=False

        while first_pos <= last_pos and not flag:

            # getting the midpoint of the list
            mid_point=(first_pos+last_pos )//2

            # checking whether the element is at the mid position of the list
            if self.list2[mid_point] == element:            
                return self.list2[mid_point]
            else:

                # checking whether the element is less than mid position element
                if element < self.list2[mid_point]:
                    last_pos=mid_point - 1
                else:
                    first_pos=mid_point + 1

        return None
