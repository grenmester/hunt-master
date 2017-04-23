
state_graph = {}

module_graph = {}

class Page(Object):

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name + " page"

class ContentPage(Page):

	def __init__(self,name, html_body, link_to):
		super().__init__(name)
		self.html_body = html_body
		self.link_to = link_to


