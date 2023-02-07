import pandas as pd
from uuid import uuid4
from classes.Patient import Patient
from classes.Bio import Bio
from classes.BioData import BioData
from classes.ReportBioStandard import ReportBioStandard
import io
from classes.EvolutionReport import EvolutionReport as ER

def merge_in_pdf(patient, count):
    images = []
    for index in range(count):
        report = ReportBioStandard(patient, index)
        images.append(report.show((1000, 2000)))
    images.append(ER(patient).get_weights())
    image = images.pop(0)
    obj = io.BytesIO() 
    image.save(
        obj, 
        format = "pdf" ,
        resolution = 100.0, 
        save_all = True, 
        append_images = images
    )
    obj.seek(0)

    


    return obj


def report(filename, name, indexes):
    uniqueIndexes = list(set(indexes.split(",")))
    #print(f'unique_indexes{uniqueIndexes}')
    bd = BioData(path = filename)
    bios = bd.create_array_of_bios(uniqueIndexes)
    patient = Patient(name = name, bios = bios)
    return merge_in_pdf(patient, len(bios))
    
def save_in_xls(filename):
    df = pd.read_csv(filename)
    xlsFile = filename.replace('.csv', '.xls')
    df.to_excel(xlsFile)

def get_dictionaries(filename):
    df = pd.read_csv(filename)
    return df.to_dict(orient = 'records')

    