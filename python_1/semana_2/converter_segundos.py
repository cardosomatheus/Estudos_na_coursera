def converter_segundos_em_dias():
    segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
    vminutos, vsegundos = divmod(segundos,60)
    vhora,vminutos = divmod(vminutos,60)
    vdias,vhora = divmod(vhora, 24)
    print(f'{vdias} dias, {vhora} horas, {vminutos} minutos e {vsegundos} segundos.')



if __name__ == '__main__':
    converter_segundos_em_dias()