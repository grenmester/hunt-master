import json

state_graph = {}
module_names = set()
module_data = {}

class Module:

	def __init__(self, name, link_to):
		if name not in module_names:
			self.name = name
		else:
			raise Exception("A module with this name already exists."\
				"Please use a unique name for the module")
		self.link_to = link_to
		state_graph[self.name] = self.link_to

	def __repr__(self):
		return self.name + " page"

class ContentModule(Module):

	def __init__(self,name, html_body, link_to):
		super().__init__("/content/" + name, link_to)
		self.html_body = html_body
		self.link_to = link_to
		module_data[self.name] = (html_body,)

def save_state_graph(filename = "state.json"):
	with open(filename, 'w') as fp:
		json.dump(state_graph, fp)

def save_module_data(filename = "modules.json"):
	with open(filename, 'w') as fp:
		json.dump(module_data, fp)