import seek

start = seek.StartModule("<p> HI!</p>", "test1")
test1 = seek.TextModule('test1', "showersuite", "BYE!")
test2 = seek.GPSModule("showersuite", "end", "1.775", "2.7775")

print start
print test1
print test2

seek.save_module_data()