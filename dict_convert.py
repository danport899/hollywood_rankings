import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')

    my_reader = csv.DictReader(datafile)
    dict_list = []
    for row in my_reader:
        dict_list.append( dict(row) )
    datafile.close()
    return dict_list
