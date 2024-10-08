import lxml.etree as etree
from .pathCode import PathCode
from .utils import Utils
from .xpathQueryValidator import XPathQueryValidator
from .statistics_collection import Statistics_collection
from .recursive_arithmetic_encoding import Recursive_arithmetic_encoder

class XMLCompressor:
    """
    A class for compressing XML documents using interval-based encoding.
    
    Attributes:
    root (Element): The root element of the XML document.
    tagIntervals (dict): A dictionary mapping XML tags to intervals.
    pathCodes (list): A list of PathCode objects representing the encoded paths of leaf nodes in the XML document.
    queryValidator (XPathQueryValidator): An instance of XPathQueryValidator for validating XPath queries.
    statistics (Statistics_collection): An instance of Statistics_collection for collecting statistics and generating intervals.
    utils (Utils): A utility class instance providing additional functionality.
    """
    def __init__(self, root) -> None:
        self.root = root
        self.tagIntervals = {}
        self.pathCodes = []
        self.queryValidator = XPathQueryValidator()
        self.statistics = Statistics_collection()
        self.utils = Utils()
        self.recursive_arithmetic_encoder = Recursive_arithmetic_encoder(self.tagIntervals)
        self.build()

    def build(self):
        """
        Constructs the interval-based path encodings for the XML document.
        """
        self.pathStack = []
        self.tagIntervals = self.statistics.generate_tag_intervals(self.root)
        self.queryValidator = XPathQueryValidator(self.tagIntervals.keys())
        self.recursive_arithmetic_encoder = Recursive_arithmetic_encoder(self.tagIntervals)
        self.pathCodes = self.recursive_arithmetic_encoder.getPathCodes(self.root)
        self.pathCodes.sort()

    def XPathQueryEncoding(self, query):
        """
        Encodes an XPath query into an interval representation using recursive 
        arithmetic encoding.

        Parameters:
        query (str): The XPath query as a string.

        Returns:
        tuple: A tuple representing the left and right bounds of the query encoding.
        """
        query = query.split('/')
        query = [q for q in query if q != '']
        l = 0.0
        r = 1.0
        for q in query:
            length = self.tagIntervals[q][1] - self.tagIntervals[q][0]
            l = self.tagIntervals[q][0] + l*length
            r = self.tagIntervals[q][0] + r*length
        return (l,r)
    
    def get(self,query):
        """
        Retrieves the values corresponding to a valid XPath query based on path encodings.

        Parameters:
        query (str): The XPath query as a string.

        Returns:
        list: A list of values corresponding to the query.
        
        Raises:
        ValueError: If the query is invalid.
        """
        if not self.queryValidator.validate(query):
            raise ValueError('Invalid query')
        query_encoding = self.XPathQueryEncoding(query)
        values = []
        for path in self.utils.bisect_range(self.pathCodes, query_encoding[0], 
                                            query_encoding[1], key=lambda x: x.left):
            if path.contained_in(query_encoding[0], query_encoding[1]):
                values.append(path.value)
        return values
    
    def to_string(self):
        """
        Converts the compressed XML document to a string representation.

        Returns:
        str: A string representation of the compressed XML document.
        """

        out = "Value intervals:\n"
        out += "left,right,value\n"
        for path in self.pathCodes:
            out += f'{path.left},{path.right},{path.value}\n'

        out += "\nTag intervals:\n"
        out += "tag,left,right\n"
        for tag, interval in self.tagIntervals.items():
            out += f'{tag},{interval[0]},{interval[1]}\n'
        return out
