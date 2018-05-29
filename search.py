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


# The search algorithms themselves	

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
