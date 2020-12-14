file = open("cities_and_states.txt", "r")
list_cities_states = file.readlines()
file.close()

# bucle que elimina los espacios en blanco al final y al inicio
# de cada elemento de la lista
for i in len(list_cities_states):
    list_cities_states[i] = list_cities_states[i].strip()
