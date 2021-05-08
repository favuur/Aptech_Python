class school:
    def __init__(self,name,year):
        self.nam=name
        self.yea=year
    def printout(sen):
        print("my school name is", sen.nam, "founded in", sen.yea)


sen=school("NIJ",1997)
sen.printout()


class football(school):
    def __init__(self,name,year,coach):
        school.__init__(self,name,year)
        self.coa=coach
        #to add coach
    def coachdetails(self):
        print("my school name is", sen.nam, "founded in", sen.yea,"by",self.coa)




play=football("redeemer cityfc",1997,"mayores")
play.printout()
play.coachdetails()





class formula1:
    def __init__(self,length,breath):
        self.len=length
        self.bre=breath
    def area_rec(self):
        print(self.len*self.bre)
len=int(input("length figure"))
bre=int(input("breath figure"))

a=formula1(len,bre)
a.area_rec()





