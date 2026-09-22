class emp:
    def work(self):
        print("working his job")
class developer:
    def develop(self):
        print("developing")
class tester(emp,developer):
    def test(self):
        print("testing")

t=tester()
t.work()
t.develop()
t.test()

# output:
# working his job
# developing
# testing