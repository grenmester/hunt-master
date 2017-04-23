import seek

start = seek.ContentModule("start", "<p> HI!</p>", "test1")
test1 = seek.ContentModule("test1", "<p> BYE!</p>", "test1")

seek.save_state_graph()
seek.save_module_data()