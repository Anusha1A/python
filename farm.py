if __name__ == '__main__':
	heads=int(35)
	legs=int(94)
	rabbits=int((legs+((-2)*heads))/2)
	chickens=int(heads-rabbits)
	print('{},{}'.format(chickens,rabbits))