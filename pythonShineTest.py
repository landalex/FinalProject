localList = ["0-0-0", "10-0-1", "10-1-3"]
biomeDiamonds = []
biomeSwords = []
biomeEnemies = []
biomeData = []
for i in range(len(localList)):
    biomeData.append(localList[i].split("-"))
for j in range(len(biomeData)):
    for k in range(1):
        biomeDiamonds.append(biomeData[j][k])
        biomeSwords.append(biomeData[j][k+1])
        biomeEnemies.append(biomeData[j][k+2])


print biomeData
print biomeDiamonds
print biomeSwords
print biomeEnemies
