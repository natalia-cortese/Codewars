"""
Challenge:
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
"""

def tower_builder(n_floors):
	tower=[]
	for floor in range(1,n_floors+1):
		stars=' '*(n_floors-floor)
		stars+='*'*(floor*2-1)
		stars+=' '*(n_floors-floor)
		print(stars)
		tower.append(stars)
	return tower

tower_builder(5)