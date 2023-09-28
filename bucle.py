import readchar
print("Presiona la tecla ↑ para salir del bucle")
while True:
    key = readchar.readkey()
    print(f"Tecla presionada: {key}")
    
    if key == "up":
        break


