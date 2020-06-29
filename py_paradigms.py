# function
def multiplikation2numbers(zahlen_liste):
    zahlen_liste = list(zahlen_liste)
    result = zahlen_liste[0] * zahlen_liste[1]
    return result


print(multiplikation2numbers([2, 5]))


# if/else
# elif unterdrückt weitere Ausgabe, sobald ein Argument vorher war ist.
# Einheit in der Form: Sekunde, Monat, Jahr
def alter_umrechnen(alter_jahre, einheit):
    if einheit == 'Jahr' and alter_jahre >= 0:
        print('Du bist ' + str(alter_jahre) + ' Jahre alt.')
    elif einheit == 'Monat' and alter_jahre >= 0:
        print('Du bist ' + str(alter_jahre * 12) + ' Monate alt.')
    elif einheit == 'Sekunde' and alter_jahre >= 0:
        import math as m
        print('Du bist ' + str(int(alter_jahre * 365 * 24 * m.pow(60, 2))) + ' Sekunden alt.')
    else:
        print('Alter oder Einheit nicht korrekt')


alter_umrechnen(23, 'Sekunde')

# while-loop
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 0
while number_list[n] <= 5:
    print(number_list[n])
    n = n + 1

# for-loop
for count_var in 'Durchlauf':
    print(count_var)

# error handler
try:
    print(int('Text'))
except (ValueError, TypeError) as error_warning:  # Hier ist es wichtig die Art des Fehlers anzugeben -> PEP8
    print(error_warning)  # die Fehlermeldung ist direkt als Varible speicherbar.

# Classes and Objects
