class menu:
	item=[]
	cost=[]
	def add (self,item,cost):
		self.item.append(item)
		self.cost.append(cost)	
	def show (self):
		for i in range(len(self.item)):
			print("item=%s,cost=%d"%(self.item[i],self.cost[i]))
c=menu()
c.add("idli",5)
c.show()
