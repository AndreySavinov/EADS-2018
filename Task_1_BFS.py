def bfs_shortest_path(graph, start, goal):
	# keep track of explored nodes
	explored = []
	# keep track of all the paths to be checked
	queue = [[start]]
	while queue:
		# pop the first path from the queue
		path = queue.pop(0)
		# get the last node from the path
		node = path[-1]
		if node not in explored:
			neighbours = graph[node]
		
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				# return path if neighbour is goal
				if neighbour == goal:
					return new_path
 
			# mark node as explored
			explored.append(node)	
	


def graph_generator():
		with open("input.txt", "r") as f:
			content = f.readlines()
		content = [x.strip() for x in content] 
		v = int(content[0])
		e = int(content[1])
		s = content[2]
		t = content[3]
		graph_points = content[4:]
		graph = {}
		for i in range(v):
			graph[str(i)] = []
				
		for element in graph_points:
			element = element.split(" ")
			if element[0] in graph.keys():
				graph[element[0]].append(element[1])								
		return graph,v,e,s,t
			
	
					
					
					
def main():
	import math
	main_graph = graph_generator()
	dijkstra_graph = main_graph[0]
	dist = bfs_shortest_path(dijkstra_graph, main_graph[3], main_graph[4])
	if (len(dist)%2 == 0):#odd number of nodes = len(dist) - 1
		reber_one = math.ceil((len(dist) - 1)/2.)
		reber_two = len(dist) - 1 - reber_one
		distance = reber_two*2 + reber_one*1
	else:
		distance = math.ceil((len(dist) - 1)/2.)*2 + math.ceil((len(dist)-1)/2.)*1
		
	with open("output.txt", "w") as out:
		out.write(str(distance))
	
	
if __name__ == "__main__":
	main()					
					