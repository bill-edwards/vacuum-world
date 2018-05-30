from collections import deque

# Supporting machinery for building search trees.

class Node(object):

	def __init__(self, state, parent, action, path_cost):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost

def generate_child_node(problem, node, action):

	return Node(
		problem.result(node.state, action),
		node,
		action,
		node.path_cost + problem.path_cost(node.state, action)
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

	def __init__(self):
		self.queue = []
		self.set = set()

	def add(self, node):
		self.queue.append(node)
		self.queue.sort(key = lambda node: node.path_cost, reverse=True)
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
		print 'GPC'
		nodes = [node for node in self.queue if node.state.stringify() == state.stringify()]
		if len(nodes) == 0: return None
		else:
			return nodes[0].path_cost

	# Given a state S and a node N with matching state, replaces any node N' whose state is S with N.
	def replace_node(self, state, node):
		print 'RN'
		indices = [index for (index, node) in enumerate(self.queue) if node.state.stringify() == state.stringify()]
		if len(indices) != 0:
			index = indices[0]
			self.queue[index] = node
			self.queue.sort(key = lambda node: node.path_cost, reverse=True)


# The search algorithms themselves

# TO DO: (i) Record actual time taken to find solution; (ii) Record number of nodes expanded; (iii) Make printing to screen optional.

def breadth_first_graph_search(problem, initial_state):

	if problem.goal_test(initial_state): return []

	node = Node(initial_state, None, None, 0)
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

def uniform_cost_graph_search(problem, initial_state):

	if problem.goal_test(initial_state): return []

	node = Node(initial_state, None, None, 0)
	frontier = PriorityQueueFrontier()
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
