segundos = int(input('Quantos segundos deseja converter? '))
dias = segundos // 86400
segundos_restante_dia = segundos % 86400
horas = segundos_restante_dia // 3600
segundos_restante_horas = segundos % 3600
minutos = segundos_restante_horas // 60
segundos_restante = segundos % 60
print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, horas, minutos, segundos_restante))
