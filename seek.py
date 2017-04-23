
import json

module_names = set() # Ensures that module names are unique.  "start" and "end" are reserved.
module_data = {}

class Module(object):

	def __init__(self, name, link_to):
		if name not in module_names:
			self.name = name
		else:
			raise Exception("A module with this name already exists."\
				"Please use a unique name for the module")
		self.link_to = link_to

	def __repr__(self):
		return self.name + " page targeting: " + self.link_to

class ContentModule(Module):

	def __init__(self, name, html_body, link_to):
		super(ContentModule, self).__init__(name, link_to)
		self.html_body = html_body
		self.url = "/content/" + self.name
		module_data[self.name] = {"url": self.url, "target": self.link_to, "data": {"html": html_body}}

class TextModule(ContentModule):
	def __init__(self, name, link_to, text):
		html_body = "<p>" + text + "</p>"
		super(TextModule, self).__init__(name, html_body, link_to)

class StartModule(ContentModule):
	def __init__(self, html_body, link_to):
		super(StartModule, self).__init__("start", html_body, link_to) #TODO switch to subclassing Module and change server code

class QRModule(Module):
	def __init__(self, name, html_body, link_to, root):
		super(QRModule, self).__init__(name, link_to)
                self.html_body = html_body
		self.url = r"/qr/" + self.name
		module_data[self.name] = {"url": self.url, "target": link_to, "data": {"html": html_body}}
		import qr
                qr.make_qr("qr/" + self.name + "_qr.png", root + '/' + self.link_to + '/')

class InteractiveModule(Module):
	def __init__(self, name, link_to, module_type, extra_data_dict):
		super(InteractiveModule, self).__init__(name, link_to)
		# self.module_type = module_type #Do we need this?
		self.url = "/" + module_type + "/" + self.name
		module_data[self.name] = {"url": self.url, "target": self.link_to, "data" : extra_data_dict}

class GPSModule(InteractiveModule):
	def __init__(self, name, link_to, x_coordinate, y_coordinate):
		super(GPSModule, self).__init__(name, link_to, "gps", {"x_coordinate": x_coordinate, "y_coordinate": y_coordinate})

class FindObjectModule(InteractiveModule):
	def __init__(self, name, link_to, object_name):
		assert(type(object_name) == type([1]))
                super(FindObjectModule, self).__init__(name, link_to, "find", {"object_name": object_name})

class ImageMatchModule(InteractiveModule):

	def __init__(self, name, link_to, image_filename):
		super(ImageMatchModule, self).__init__(name, link_to, "match", {"image_filename": image_filename})

class TextInputModule(InteractiveModule):

	def __init__(self, name, link_to, correct_string):
		super(TextInputModule, self).__init__(name, link_to, "text", {"correct_string": correct_string})

def save_module_data(filename = "modules.json"):
	url_module_data = {}
	for module_name in module_data:

		module_info = module_data[module_name]
		target_name = module_info["target"]
		if target_name == "end":
			target_url = "/end/"
		else:
			target_url = module_data[target_name]["url"]
		url_module_data[module_name] = {"url": module_info["url"], "target": target_url, "data": module_info["data"]}

	with open(filename, 'w') as fp:
		json.dump(url_module_data, fp)

