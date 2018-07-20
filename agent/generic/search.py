from collections import deque

# Supporting machinery for building search trees.

class Node(object):

	def __init__(self, state, parent, action, path_cost, depth):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
		self.depth = depth

def generate_child_node(problem, node, action):

	return Node(
		problem.result(node.state, action),
		node,
		action,
		node.path_cost + problem.path_cost(node.state, action),
		node.depth + 1
	)

def generate_solution(node):

	action_list = []
	while node.action != None:
		action_list.append(node.action)
		node = node.parent
	return action_list

class FIFOFrontier(object):

	def __init__(self):
		self.queue = deque()
		self.set = set()

	def add(self, node):
		self.queue.append(node)
		self.set.add(node.state.stringify())

	def pop(self):
		node = self.queue.popleft()
		self.set.discard(node.state.stringify())
		return node

	def test_membership(self, state):
		return state.stringify() in self.set

	def size(self):
		return len(self.set)

class PriorityQueueFrontier(object):

	def __init__(self, orderer):
		self.queue = []
		self.set = set()
		self.orderer = orderer

	def add(self, node):
		self.queue.append(node)
		self.queue.sort(key = self.orderer, reverse=True)
		self.set.add(node.state.stringify())

	def pop(self):
		node = self.queue.pop()
		self.set.discard(node.state.stringify())
		return node

	def test_membership(self, state):
		return state.stringify() in self.set

	def size(self):
		return len(self.set)

	def get_path_cost_to_state(self, state):
		nodes = [node for node in self.queue if node.state.stringify() == state.stringify()]
		if len(nodes) == 0: return None
		else:
			return self.orderer(nodes[0])

	# Given a state S and a node N with matching state, replaces any node N' whose state is S with N.
	def replace_node(self, state, node):
		indices = [index for (index, n) in enumerate(self.queue) if n.state.stringify() == state.stringify()]
		if len(indices) != 0:
			index = indices[0]
			self.queue[index] = node
			self.queue.sort(key = self.orderer, reverse=True)


# The search algorithms themselves

def breadth_first_graph_search(problem, initial_state):

	if problem.goal_test(initial_state): return []

	node = Node(initial_state, None, None, 0, 0)
	frontier = FIFOFrontier()
	frontier.add(node)
	explored = set()
	i = 0

	while True:
		print i, frontier.size()
		i += 1
		if frontier.size() == 0: return 'FAILURE'
		node = frontier.pop()
		explored.add(node.state.stringify())
		for action in problem.actions(node.state):
			child_node = generate_child_node(problem, node, action)
			if (child_node.state.stringify() not in explored and not frontier.test_membership(child_node.state)):
				if problem.goal_test(child_node.state): return generate_solution(child_node)
				frontier.add(child_node)

def depth_first_tree_search(problem, initial_state, limit=None):
	
	node = Node(initial_state, None, None, 0, 0)
	frontier = [node]
	path = []
	i = 0

	while True:
		print i, len(frontier), len(path)
		i += 1
		if len(frontier) == 0: return 'FAILURE'
		node = frontier.pop()
		if problem.goal_test(node.state): return generate_solution(node)
		path = path[:node.depth]
		path.append(node.state.stringify())
		if (limit == None or node.depth < limit):
			for action in problem.actions(node.state):
				child_node = generate_child_node(problem, node, action)
				if (child_node.state.stringify() not in path):
					frontier.append(child_node)

def iterative_deepening_tree_search(problem, initial_state):

	limit = 1;
	while True:
		print 'Depth-first tree search with limit ', limit
		result = depth_first_tree_search(problem, initial_state, limit)
		if result != 'FAILURE': return result
		limit += 1

def best_first_graph_search(evaluation_function):

	def search_function(problem, initial_state):

		if problem.goal_test(initial_state): return []

		node = Node(initial_state, None, None, 0, 0)
		frontier = PriorityQueueFrontier(evaluation_function)
		frontier.add(node)
		explored = set()
		i = 0

		while True:
			print i, frontier.size()
			i += 1
			if frontier.size() == 0: return 'FAILURE'
			node = frontier.pop()
			if problem.goal_test(node.state): return generate_solution(node)
			explored.add(node.state.stringify())
			for action in problem.actions(node.state):
				child_node = generate_child_node(problem, node, action)
				if (child_node.state.stringify() not in explored and not frontier.test_membership(child_node.state)):
					frontier.add(child_node)
				elif (frontier.test_membership(child_node.state) and frontier.get_path_cost_to_state(child_node.state) > child_node.path_cost):
					frontier.replace_node(child_node.state, child_node)

	return search_function

def uniform_cost_graph_search():
	return best_first_graph_search(lambda node: node.path_cost)

def greedy_best_first_search(heuristic):
	return best_first_graph_search(heuristic)

def a_star_search(heuristic):
	return best_first_graph_search(lambda node: node.path_cost + heuristic(node))


# AND-OR search to generate contingency plans for non-deterministic search graphs.
def and_or_search(problem, initial_state):

# Chooses from the possible actions that can be taken in a given state.
def or_search(state, problem, path):

# Maps plans to all possible outcome states resulting from a given action.
def and_search(states, problem, path):
