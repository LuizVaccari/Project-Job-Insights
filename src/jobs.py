from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path) as file:
        content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = content
        lista = []
        for row in data:  # para cada linha em data
            new_object = {}  # crio um novo objeto
            index = 0  # zero o index para iniciar no index 0
            for column in header:  # para cada coluna no header
                new_object[column] = row[index]
                # chama uma coluna como chave e coloca valor da linha por index
                index += 1
                # soma 1 index para ir para o próximo ítem da linha em dados
            lista.append(new_object)  # apensa o novo objeto à lista
        return lista  # retorna a lista final

    """Reads a file from a given path and returns its contents

    Parameters
    -----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """


#  read('/home/luiz/Trybe/sd-010-a-project-job-insights/src/jobs.csv')
