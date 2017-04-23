import seek
DOMAIN = "seek.com"

start = seek.StartModule("""<p> HI!</p><img src="static/img/beach_hacks_logo.jpg" alt="Giant Glass Pyramid">""", "test1")
test1 = seek.TextModule('test1', "textinput", "BYE!")
test2 = seek.TextInputModule("textinput", "showersuite", "Test!")
test2 = seek.GPSModule("showersuite", "findtest", "1.775", "2.7775")
test3 = seek.FindObjectModule("findtest", "matchtest", "dog")
test4 = seek.ImageMatchModule("matchtest", "qrtest", "test.png")
test5 = seek.QRModule("qrtest", "<p>This page should have no continue button</p>", "end", DOMAIN)

print start
print test1
print test2
print test3
print test4
print test5

seek.save_module_data()
