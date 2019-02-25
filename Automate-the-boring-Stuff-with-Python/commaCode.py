# Funktion zur Ausgabe der Indexe
def comma_code(list):
    for i in list:
        if i == list[len(list) -1]:
            print('and', end="")
        print(i, end="")

# Eingabe des Users und Ausgabe der Liste
print('Bite geben Sie eine Liste ein:')
user_list = input()
comma_code(user_list)