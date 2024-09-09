
class XPathQueryValidator:
    """
    A class for validating XPath queries against a set of tag intervals.
    
    Attributes:
    tags (list): A list containing XML tags present in the given xml file.
    """

    def __init__(self, tags=None)->None:
        self.tags = tags
        pass

    def validate(self,query):

        """
        Validates an XPath query against the stored tags. 
        The query is valid if all tags in the query are present in the tags dictionary.

        Parameters:
        query (str): The XPath query as a string.

        Returns:
        bool: True if the query is valid, False otherwise.
        """

        if self.tags is None:
            return False
        query = query.split('/')
        query = [q for q in query if q != '']
        for q in query:
            if q not in self.tags:
                return False
        return True
    