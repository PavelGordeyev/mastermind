#####################################################################
## Description:  Class to describe a single peg. Used for all pegs,
##				 both color and white and black.  Integers used to
##				 represent colors
#####################################################################
class Peg:

	def __init__(self, val):
		self.val = val

	def getPegVal(self):
		return self.val