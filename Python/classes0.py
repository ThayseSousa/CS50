class Flight:

#generic idea to what flight means in our application

	def __init__(self,origin, destination,duration):
		#init - it will say what is going to happen when someone is creating a flight
		#we don't have a flight and we wanna to creat our first flight
		# in () are our parameters, what we want to populate
		# parameters in Python will aways start with "self"
		self.origin = origin
		self.destination = destination
		self.duration = duration

def main():

	#Create a flight
	f = Flight(origin="New York", destination="Paris", duration = 540)

	#change the value of a variable
	f.duration += 10

	#print details about flight 
	print(f.origin)
	print(f.destination)
	print(f.duration)

	if __name__ == "__main__":
		main()