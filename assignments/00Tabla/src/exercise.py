def main():
    #escribe tu código abajo de esta línea
    inc = 0.5
    final = 10
    x = 0.5
    while (x<=final):
        y= 3*(x**2) + 7*x - 15
        z= y - 2*(x**2)
        print(f" valores x={x} y={y} z={z}")
        x = x + inc
    pass

if __name__=='__main__':
    main()
