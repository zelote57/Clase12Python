laberinto = [
        "########",
        "#      #",
        "#b#### #",
        "#a  #  #",
        "##### ##",
        "#      #",
        "########"
    ]

print(laberinto[0])
print(laberinto[1])
print(laberinto[0][1])
print(laberinto[1][0])

# def laberinto():
#     laberinto = [
#         "########",
#         "#      #",
#         "# #### #",
#         "#   #  #",
#         "##### ##",
#         "#      #",
#         "########"
#     ]

#     x, y = 1, 1

#     while True:
#         for fila in laberinto:
#             print(fila)

#         movimiento = input("Mover (WASD): ").upper()

#         if movimiento == "W":
#             y -= 1
#         elif movimiento == "S":
#             y += 1
#         elif movimiento == "A":
#             x -= 1
#         elif movimiento == "D":
#             x += 1

#         print(y,x)
#         print(laberinto[y][x])
        
#         if laberinto[y][x] == "#":
#             print("¡Te chocaste con una pared!")
#             break

# laberinto()