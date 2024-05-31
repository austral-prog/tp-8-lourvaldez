

def get_coordinate(treasure):
    return treasure[1]
    
    #algo de hacer una lista 
    #lugares= [1F, 5B, 3D, 4B, 8C, 6A, 6D, 8A, 7F, 1C, 2A, 4E, 7E]

    #me debe devolver una tupla



def convert_coordinate(coordinate):
    bibop=coordinate[0]
    bibup=coordinate[1]
   
    muestro=tuple(f"{bibop}{bibup}")
    return muestro


def create_record(azara_record, rui_record):
    virulinda = str(rui_record[1][0])
    virulana = rui_record[1][1]
    fiufiu = virulinda + virulana
    comecoco= tuple(azara_record[:] + rui_record[:])
    if azara_record[1]==fiufiu:
            return comecoco
    #reate_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
#('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
    else:
        return "not a match"
