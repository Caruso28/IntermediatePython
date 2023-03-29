# File Handling
#import os

# .txt file
#txt_file = open("Intermediate/my_file.txt", "r+") #r lectura, r+ lectura y escritura, w+ escritura
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#for line in txt_file.readLines():
    #print(line)

#txt_file.write("\nAunque tambien me gusta Java")
#print(txt_file.readline())

#os.remove(""Intermediate/my_file.txt"")


# .json file
#import json
#json_file = open("Intermediate/my_file.json", "w+") #r lectura, r+ lectura y escritura, w+ escritura

#json_text = { #Como un Dict
    #"Name":"Guido", 
    #"Surname":"Rimati", 
    #"Age":37,
    #"Hobbies": {"Estudiar", "Deporte"},
    #"Language": "Python"
#    } 
#json.dump(json_text, json_file, indent = 2)
#jsom_file.close()

# with open("intermediate/my_fli.json") as my_other_file:
    #for line in my_other_file readlines();
        #print(line)

# .csv file
#import csv
#csv_file = open("Intermediate/my_file.csv", "w+") #r lectura, r+ lectura y escritura, w+ escritura
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(["name", "surname", "age"])
#csv_writer.writerow(["Guido", "Rimati", "37"])

#csv_file.close()

# with open("intermediate/my_file.csv") as my_other_file:
    #for line in my_other_file readlines();
        #print(line)

# .xlsx file
# import xlrd # Debe importarse el modulo

# .xml file
#import xml
