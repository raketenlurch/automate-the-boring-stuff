#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats','moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)

    count = 0
    while count  < len(table):
        for item in table[count]:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1

    for words in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][words].rjust(colWidths[item]), end=" ")
        print()

printTable(tableData)
