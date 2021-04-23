class ParsingNode:
    '''
    Parsing Node.

    Args:
        key: The key stored in the node.
    '''
    #
    #
    def __init__(self, key=None):
        self.key = key

    #
    #
    def __str__(self):
        return str(self.key)