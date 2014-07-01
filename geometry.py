class Point(object):
	"""docstring for Point"""
	def __init__(self, arg):
		super(Point, self).__init__()
		self.arg = arg

		x = 0
		y = 0
	def setPosition(self, x, y):
		self.x = x
		self.y = y
	def getPosition():
		return x, y

class Line(object):
	"""docstring for Line"""
	def __init__(self, arg):
		super(Line, self).__init__()
		self.arg = arg
		point1 = new Point()
		point2 = new Point()
	def setPoints(self, point1, point2):
		self.point1 = point1
		self.point2 = point2
		
		