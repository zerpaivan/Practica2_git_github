# script para organizar una lista de ciudades por estados
# y de forma alfabetica
from sorted_dict import sortedDict
file = open("cities_and_states.txt", "r")
list_cities_states = file.readlines()
file.close()
print(list_cities_states)
# bucle que elimina los espacios en blanco al final y al inicio
# de cada elemento de la lista
for i in range(len(list_cities_states)):
    list_cities_states[i] = list_cities_states[i].strip()


#blucle que crea lista de los estados
states_plus_cities = {}
for n, c_s in enumerate(list_cities_states, 1):
    temp = c_s.split(" - ")


    if temp[1] not in states_plus_cities:
        states_plus_cities[temp[1]] = []
        states_plus_cities[temp[1]].append(temp[0])
    else:
        states_plus_cities[temp[1]].append(temp[0])

print(states_plus_cities)
print(sortedDict(states_plus_cities))
print("prueba de actulizacion de github")
