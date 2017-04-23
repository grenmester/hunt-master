import seek
DOMAIN = "seek-165508.appspot.com"
start = seek.StartModule('<p> You\'ll be tasked with finding an item and taking a picture of it four times. Are you ready? </p>', 'image0')
items = [seek.FindObjectModule('image' + str(i), 'image' + str((i+1)%4), ['drink','computer keyboard','computer','outerwear'][i]) for i in range(4)]
# Make sure it ends
items[-1].link_to = 'end'

print start
print items
seek.save_module_data()
