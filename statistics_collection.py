
class Statistics_collection:
    """
    A class for collecting statistics and generating interval encodings for XML elements.
    
    Attributes:
    adjusted_freq (dict): A dictionary storing the adjusted frequency of XML tags.
    tagIntervals (dict): A dictionary storing the interval encodings of XML tags.
    """

    def __init__(self) -> None:
        self.adjusted_freq = {}
        self.tagIntervals = {}
        pass

    def get_adjusted_frequency(self, root):
        """
        Recursively calculates the adjusted frequency of XML tags starting from the root element.

        Parameters:
        root (Element): The root element of the XML document.
        """
        if root is None:
            return
        
        if root.tag not in self.adjusted_freq:
            self.adjusted_freq[root.tag] = 1
            for ancestor in self.pathStack:
                self.adjusted_freq[ancestor] += 1

        self.pathStack.append(root.tag)
        for child in root:
            self.get_adjusted_frequency(child)
        self.pathStack.pop()

    def get_interval_encodings(self):
        """
        Computes interval encodings for XML tags based on their adjusted frequencies.
        """
        n = sum(self.adjusted_freq.values())
        left = 0.0
        right = 0.0
        for tag in self.adjusted_freq:
            right = left + self.adjusted_freq[tag]/n
            self.tagIntervals[tag] = (left, right)
            left = right

    def generate_tag_intervals(self, root):
        """
        Generates the interval encodings for XML tags starting from the root element.

        Parameters:
        root (Element): The root element of the XML document.

        Returns:
        dict: A dictionary with tags as keys and their interval encodings as values.
        """
        self.pathStack = []
        self.get_adjusted_frequency(root)
        self.get_interval_encodings()   
        return self.tagIntervals
