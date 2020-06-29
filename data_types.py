# Testkommentar
# lists
Number_List = [1, 0, 6, 9, 10]
String_List = ['test100', 'test1']
Number_List.reverse()
String_List.sort(key=len)
print(String_List)
print(Number_List)

# indexing lists
list_indexing = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list_indexing[1][0])

# tupel - sind unveränderbar, nachdem sie erstellt wurden
Tupel1 = (1, 2, 3, 4)
Tupel_List = [(1, 2), (3, 4), (5, 6)]
print(Tupel1[0])
print(Tupel_List[0])

# dictonarys
Dictonary = {
    'Key1': 'Value1',
    1: 'Value2'
}
print(Dictonary.get('Key1'))

