descuento(precio:REAL): REAL
# Importe del descuennto acordado sobre 'precio'

Precondicion 
    precio >= 0

Realizacion 
    si 
        precio < 100
    entonces
        #precio < 100 --> no hay descuento
        Resultado <-- 0
    si no si
        precio < 500
    entonces 
    # 100 <= precio < 500 --> descuento del 5%
        Resultado <-- precio * 0.05
si no
    # precio >= 500 --> descuento del 8%
    Resultado <-- precio * 0.08

Postcondicion
    precio < 100 --> Resultado = 0
    100 <= precio < 500 --> Resultado = precio * 0.05
    500 <= precio --> Resultado = precio * 0.08

fin descuento

