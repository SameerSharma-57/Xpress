from .pathCode import PathCode

class Recursive_arithmetic_encoder:
    def __init__(self, tagIntervals):
        """
        Initializes the Recursive_arithmetic_encoder object.

        Parameters:
        tagIntervals (dict): A dictionary of tag intervals.
        """
        self.tagIntervals = tagIntervals
        self.pathCodes = []
    
    def generate_path_encodings(self,root,parentInterval):
        """
        Recursively generates path encodings for each element in the XML document.

        Parameters:
        root (Element): The current XML element.
        parentInterval (tuple): The interval encoding of the parent element.
        """
        if root is None:
            return
        
        interval = self.tagIntervals[root.tag]
        length = interval[1] - interval[0]
        left = interval[0] + parentInterval[0]*length
        right = interval[0] + parentInterval[1]*length
        parentInterval = (left, right)

        childs = root.getchildren()
        if len(childs) == 0:
            self.pathCodes.append(PathCode(left, right, root.text))
            return
        for child in childs:
            self.generate_path_encodings(child, parentInterval)

    def getPathCodes(self, root):
        """
        Returns the path codes generated by the encoder.

        Returns:
        list: A list of PathCode objects.
        """
        self.generate_path_encodings(root, (0.0,1.0))
        return self.pathCodes