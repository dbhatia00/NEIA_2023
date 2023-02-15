pop = 300000
print('Year\t\tPopulation')
for year in range(2010, 2050):
    print(str(year) + '\t\t' + str(pop))
    pop += int(0.03 * pop)