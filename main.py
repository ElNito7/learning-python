from random import choices

randomList = ["1","2","3","4","5","6","7","8","9","10","A","E","I","O","U",]
ticket = choices(randomList, k=4)
print("The ticket "+"".join(ticket)+" will win a prize")