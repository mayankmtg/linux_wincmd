from optparse import OptionParser

class HeaderChecks:
    
    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-n", "--name", dest="name", help="name of command")
        self.parser.add_option("-d", "--desc", dest="desc", help="Description of the command")
        self.parser.add_option("-e", "--example", dest="example", help="An example usage of the command")
        self.parser.add_option("-t", "--head", dest ="head", help="Header of the file")
    
    def parse(self):
        (options, args) = self.parser.parse_args()
        return (options, args)