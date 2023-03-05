

import pandas as pd
file_name="C:\Dev\Python\CursoPhyton\TT040323.642.XLS"

book  = pd.read_excel(file_name, 
                   usecols=[0, 1])


for n in book.values:
    if str(n[1]).__contains__('CARREFOUR'):
        print(n[0])

    