def calcular_salario():
    # Entrada de datos
    nombre = input("Introduce el nombre del trabajador: ")
    horas = float(input("Introduce las horas trabajadas: "))
    tarifa = float(input("Introduce la tarifa por hora: "))

    # Calcular salario bruto
    if horas <= 35:
        salario_bruto = horas * tarifa
    else:
        horas_normales = 35 * tarifa
        horas_extra = (horas - 35) * (tarifa * 1.5)
        salario_bruto = horas_normales + horas_extra

    # Calcular impuestos
    impuesto = 0
    if salario_bruto > 500:
        if salario_bruto <= 900:  # 500 + 400
            impuesto = (salario_bruto - 500) * 0.25
        else:
            impuesto = (400 * 0.25) + ((salario_bruto - 900) * 0.45)

    # Calcular salario neto
    salario_neto = salario_bruto - impuesto

    # Imprimir resultados
    print("\n--- Detalles del Salario ---")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Salario bruto: {salario_bruto:.2f}€")
    print(f"Impuestos: {impuesto:.2f}€")
    print(f"Salario neto: {salario_neto:.2f}€")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_salario()