
currentSum = 0
powerSum = 0
resistance = [16, 27, 39, 56, 81]
current = []
power = []

for i in range(0,5):
    current.append((eval(input('Enter current value: '))))
    power.append(resistance[i] * current[i]**2)
    
print("Resistance \t Current \t Power")

print()
                  
for x in range(0, 5):
     print(resistance[x],"\t\t", current[x],"\t\t", power[x],"\n")
     currentSum += current[x];
     powerSum += power[x];
print("Total: \t\t", currentSum, "\t\t", powerSum)
