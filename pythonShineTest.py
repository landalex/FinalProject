newList = []
for i in range(len(listOrig)):
	newList.append(listOrig[i])

counter = 0

for i in range(len(listOrig) - 1):
	counter += 1
	if listOrig[i] > listOrig[i+1]:
		newList[i+1] = newList[i]
		newList[i] = listOrig[i+1]
	elif listOrig[i] <= listOrig[i+1]:
		newList[i+1] = listOrig[i+1]
	if counter == ((len(listOrig)) - 1):
		if newList[-2] > newList[-1]:
			newList[-1] = newList[-2]
			newList[-2] = listOrig[-1]
