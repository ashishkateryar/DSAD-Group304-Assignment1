# author : Ashish Kateryar

class PatientRecord:
    def __init__(self, age, name, Pid):
        self.PatId = str(Pid) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None


patientUnorderedList = []
with open('inputPS24a.txt', 'r') as fileObject1:
    tempId = 1001
    for line in fileObject1:
        line = line.replace('\n', '')
        line = line.replace(' ','')
        line = line.split(',')
        print(line)        
        patientUnorderedList.append(PatientRecord(line[1], line[0], tempId))
        tempId += 1

for record in patientUnorderedList:
    print(record.PatId, record.age, record.name)
    print('*************************')
