from datetime import datetime, timedelta

pasos =    {'Paso 1: 40 g mm + 100 manitoba + 50 agua': 4, \
            'Paso 2: 40 g mm + 100 manitoba + 50 agua': 4, \
            'Paso 3: 1º amasado de primera masa': 0.25, \
            'Paso 4: 1ª fermentación': 12, \
            'Paso 5: 2º amasado': 0.30, \
            'Paso 6: reposo': 1, \
            'Paso 7: dividir, bolear y meter en moldes': .25, \
            'Paso 8: fermentación final': 8, \
            'Paso 9: horneado': 1, \
            'Paso 10: reposo boca abajo': 10
            }
        

hora = input("hora a la que quieres empezar (HH:MM):")
hora_obj = datetime.strptime(hora,'%H:%M')
dia_dt_obj = datetime.now().date()

fecha_de_inicio_str = '{}-{}-{} {}:{}'.\
                                        format(dia_dt_obj.year, \
                                                dia_dt_obj.month, \
                                                dia_dt_obj.day, \
                                                hora_obj.hour, \
                                                hora_obj.minute)


fecha_de_inicio_obj = datetime.strptime(fecha_de_inicio_str, '%Y-%m-%d %H:%M')
hora_paso = fecha_de_inicio_obj 
for paso in pasos.keys():
    print(paso)
    print('empieza: {}'.format(hora_paso))
    print('termina: {}'.format(hora_paso+timedelta(hours=pasos[paso])))
    print('-----')
    hora_paso += timedelta(hours=pasos[paso])

