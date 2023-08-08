data = """
	ppm	posicion	pulsaciones	errores	fecha	modo
1	674	1	468	29	2023-08-08 17:24:40	juego
2	717	1	751	43	2023-08-08 16:59:30	juego
3	723	1	724	11	2023-08-08 16:30:14	juego
4	735	1	501	34	2023-08-07 23:26:15	juego
(Ingresar valores deseados)
"""

lines = data.strip().split('\n')
cpm_total = 0
pulsaciones_total = 0
errores_total = 0
num_entries = 0

for line in lines[1:]:  # Empezamos desde la segunda línea para ignorar los encabezados
    fields = line.split('\t')
    cpm = int(fields[1]) / 100
    pulsaciones = int(fields[3]) / 100  
    errores = int(fields[4]) / 100
    cpm_total += cpm
    pulsaciones_total += pulsaciones
    errores_total += errores
    num_entries += 1

if num_entries > 0:
    media_cpm = cpm_total / num_entries
    media_pulsaciones = pulsaciones_total / num_entries
    media_errores = errores_total / num_entries
    print("Media de CPM:", media_cpm * 100)
    print("Media de pulsaciones:", media_pulsaciones * 100)
    print("Media de errores:", media_errores * 100)
else:
    print("No hay datos disponibles para calcular la media.")
