import math

def funcion(x: float) -> float:
    # La función a evaluar: x/5 + e^x - 2
    return (x / 5) + math.exp(x) - 2

# MODIFICACIÓN 1: Se cambió el nombre de la función a interpolacion_lineal
def interpolacion_lineal(a: float, b: float, tol: float, num_iter: int) -> float:
    if (funcion(a) * funcion(b) >= 0):
        print("No se puede continuar con el método de interpolación lineal: no hay cambio de signo.")
        return None

    c_prev = 0.0
    print(" i \t | a \t\t | b \t\t | f(a) \t | f(b) \t | c \t\t | f(c) \t | er")
    
    for i in range(num_iter):
        fa = funcion(a)
        fb = funcion(b)
        
        # MODIFICACIÓN 2: Implementación de la fórmula de la Regla Falsa en lugar de (a+b)/2
        # Se aproxima la raíz usando la recta que une los puntos (a, f(a)) y (b, f(b))
        c = b - (fb * (a - b)) / (fa - fb)
        fc = funcion(c)
        
        # Cálculo del error relativo (se omite en la primera iteración al no haber valor previo)
        if i == 0:
            er = 100.0 
        else:
            er = (abs(c - c_prev) / abs(c)) * 100
            
        print(f" {i+1} \t | {a:.4f} \t | {b:.4f} \t | {fa:.4f} \t | {fb:.4f} \t | {c:.4f} \t | {fc:.4f} \t | {er:.2f}")
        
        # Criterio de paro por tolerancia
        if (er <= tol) and (i > 0):
            print(f"\nMétodo finalizado con {i+1} iteraciones y un error de {er:.2f}%")
            return c
            
        # MODIFICACIÓN 3: La actualización de los límites (a o b) sigue la misma lógica de signos,
        # pero ahora converge más rápido apoyado en la recta secante.
        if funcion(a) * funcion(c) < 0:
            b = c
        elif funcion(c) * funcion(b) < 0:
            a = c
        else:
            print(f"\nMétodo finalizado con {i+1} iteraciones")
            return c
            
        c_prev = c
        
    print("Se alcanzó el número máximo de iteraciones sin lograr la tolerancia deseada.")
    return c

def main():
    print("--- Método de Interpolación Lineal (Regla Falsa) ---")
    
    # MODIFICACIÓN 4: Ciclo while para asegurar que el límite inferior (a) sea estrictamente menor al límite superior (b)
    while True:
        a = float(input("Ingrese el valor de a del intervalo (límite inferior): "))
        b = float(input("Ingrese el valor de b del intervalo (límite superior): "))
        if a >= b:
            print("Error: No es posible tener un límite inferior mayor o igual al límite superior. Intente de nuevo.\n")
        else:
            break
            
    tol = float(input("Ingrese la tolerancia (en porcentaje, ej. 0.01): "))
    num_iter = int(input("Ingrese el número máximo de iteraciones: "))
    
    # MODIFICACIÓN 5: Llamada a la nueva función interpolacion_lineal
    c = interpolacion_lineal(a, b, tol, num_iter)
    
    if (c is not None):
        print(f"La raíz de la ecuación x/5 + e^x - 2 es: {c:.6f}")

if __name__ == "__main__":
    main()
