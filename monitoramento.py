def coleta_dados(num_pontos):
    phs = [7.1, 8.3, 7.8, 6.9, 8.0]
    temperaturas = [21.5, 23.0, 19.8, 22.1, 20.7]
    turbidezes = [45.0, 30.2, 55.3, 40.0, 48.5]

    return phs[:num_pontos], temperaturas[:num_pontos], turbidezes[:num_pontos]

def analisa_dados(phs, temperaturas, turbidezes):
    ph_medio = sum(phs) / len(phs)
    ph_maximo = max(phs)
    ph_minimo = min(phs)

    temperatura_media = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)

    turbidez_media = sum(turbidezes) / len(turbidezes)
    turbidez_maxima = max(turbidezes)
    turbidez_minima = min(turbidezes)

    return (ph_medio, ph_maximo, ph_minimo, 
            temperatura_media, temperatura_maxima, temperatura_minima, 
            turbidez_media, turbidez_maxima, turbidez_minima)

def gera_alertas(ph_medio, temperatura_media, turbidez_media):
    alertas = []

    if ph_medio < 7.0 or ph_medio > 8.5:
        alertas.append("Alerta: pH médio fora do intervalo ideal (7.0 - 8.5).")
    
    if temperatura_media < 18.0 or temperatura_media > 28.0:
        alertas.append("Alerta: Temperatura média fora do intervalo ideal (18°C - 28°C).")
    
    if turbidez_media > 50.0:
        alertas.append("Alerta: Turbidez média acima do nível seguro (50 NTU).")

    return alertas

def main():
    num_pontos = 5
    phs, temperaturas, turbidezes = coleta_dados(num_pontos)
    (ph_medio, ph_maximo, ph_minimo, 
     temperatura_media, temperatura_maxima, temperatura_minima, 
     turbidez_media, turbidez_maxima, turbidez_minima) = analisa_dados(phs, temperaturas, turbidezes)
    alertas = gera_alertas(ph_medio, temperatura_media, turbidez_media)

    print("Dados coletados:")
    for i in range(num_pontos):
        print(f"Ponto {i+1}: pH={phs[i]}, Temperatura={temperaturas[i]}°C, Turbidez={turbidezes[i]} NTU")

    print("\nAnálise dos dados:")
    print(f"pH Médio: {ph_medio}, pH Máximo: {ph_maximo}, pH Mínimo: {ph_minimo}")
    print(f"Temperatura Média: {temperatura_media}°C, Temperatura Máxima: {temperatura_maxima}°C, Temperatura Mínima: {temperatura_minima}°C")
    print(f"Turbidez Média: {turbidez_media} NTU, Turbidez Máxima: {turbidez_maxima} NTU, Turbidez Mínima: {turbidez_minima} NTU")

    print("\nAlertas:")
    for alerta in alertas:
        print(alerta)

if __name__ == "__main__":
    main()
