class company:
    def rules(self):
        print("rule is rule")
class hr_team(company):
    def hiring(self):
        print("hiring")
class front_end(company):
    def design(self):
        print("designing")
class back_end(company):
    def back(self):
        print("coding")

c1=hr_team()
c2=front_end()
c3=back_end()
c1.hiring()
c2.design()
c3.back()
c1.rules()
c2.rules()
c3.rules()