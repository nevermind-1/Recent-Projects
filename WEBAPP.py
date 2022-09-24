anthony = {
    'Name': 'ajuba anthony',
    'Quizes': [74.0,86.0,95.0,84.0],
    'Homework': [91.0,74.0,93.0],
    'Recitation': [81.0,82.0,84.0],
    'Tests': [98.0,100.0]
}

james = {
    'Name': 'chinaza james',
    'Quizes': [77.0,87.0,94.0,84.0],
    'Homework': [94.0,74.0,99.0],
    'Recitation': [70.0,83.0,86.0],
    'Tests': [97.0,100.0]
}

Selen = {
    'Name': 'Selen Ander',
    'Quizes': [98.0,100.0,94.0,100.0],
    'Homework': [94.0,74.0,96.0],
    'Recitation': [78.0,88.0,84],
    'Tests': [97.0,90.0]
}

def average(number):
    total = sum(number)
    result = total/len(number)
    return result


def get_average(student):
    Quizes = average(student['Quizes'])
    Homework = average(student['Homework'])
    Recitation = average(student['Recitation'])
    Tests = average(student['Tests'])
    print(student['Name'])
    return .2*Quizes + 1*Homework + .3*Recitation + .4*Tests

print(get_average(anthony))
print(get_average(james))
print(get_average(Selen))