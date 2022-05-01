class Board:
    def showBoard(self, data):
        print("| %i | %i | %i |" % (data[0], data[3], data[6]))
        print("-------------")
        print("| %i | %i | %i |" % (data[1], data[4], data[7]))
        print("-------------")
        print("| %i | %i | %i |" % (data[2], data[5], data[8]))
        print("----------------")

