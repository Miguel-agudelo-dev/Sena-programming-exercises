import random
import time

print("🌴 BIENVENIDO A CAZADOR DE RESTREPO 🌴")
print("Hecho por: Miguel")
print("Atrapa 5 frutas antes de que caigan 3 al piso")
print("------------------------------------")

puntos = 0
vidas = 3
frutas = ["🥭 Mango", "🍌 Banano", "🍊 Naranja", "🍍 Piña"]

while vidas > 0 and puntos < 5:
    fruta = random.choice(frutas)
    print(f"\n¡Cae un {fruta}!")
    
    respuesta = input("Escribe ATRAPAR rápido: ").lower()
    
    if respuesta == "atrapar":
        puntos = puntos + 1
        print(f"¡Bien! +1 punto. Llevas {puntos}/5 🥳")
    else:
        vidas = vidas - 1
        print(f"Se cayó! Te quedan {vidas} vidas 😢")
    
    time.sleep(1)

if puntos == 5:
    print("\n🏆 ¡GANASTE! Eres el mejor cazador de Restrepo")
else:
    print("\n💀 GAME OVER. Intenta de nuevo")

print(f"Puntaje final: {puntos}")
