class PathCode:
    """
    A class representing a code that encodes the path in the XML structure.
    
    Attributes:
    left (float): The left bound of the encoding interval.
    right (float): The right bound of the encoding interval.
    value (str): The value associated with the encoded path, often the text content of an XML element.
    """
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self) -> str:
        return f'({self.left},{self.right},{self.value})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def contains(self, other):
        return self.left <= other.left and other.right <= self.right
    
    def contains(self, l, r):
        return self.left <= l and r <= self.right
    
    def contained_in(self, other):
        return other.left <= self.left and self.right <= other.right
    
    def contained_in(self, l, r):
        return l <= self.left and self.right <= r
    
    def __lt__(self, other):
        if self.left == other.left:
            return self.right < other.right
        return self.left < other.left

    def __gt__(self, other):
        if self.left == other.left:
            return self.right > other.right
        return self.left > other.left

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __ne__(self, other):
        return not self == other
