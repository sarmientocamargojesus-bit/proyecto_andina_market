"""Calcula la relación de contraste WCAG 2.x de los pares de color del sitio."""
import sys

PARES = {
    "texto / fondo": ("#1f2933", "#ffffff"),
    "texto suave / fondo": ("#52606d", "#ffffff"),
    "marca / fondo": ("#8a3b12", "#ffffff"),
    "texto suave / tarjeta": ("#52606d", "#f7f5f2"),
    "texto / tarjeta": ("#1f2933", "#f7f5f2"),
    "mensaje de error / fondo": ("#9b1c1c", "#ffffff"),
}


def luminancia(hex_color):
    canales = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lineal = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in canales]
    return 0.2126 * lineal[0] + 0.7152 * lineal[1] + 0.0722 * lineal[2]


def contraste(a, b):
    claro, oscuro = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (claro + 0.05) / (oscuro + 0.05)


if __name__ == "__main__":
    minimo = min(contraste(*par) for par in PARES.values())
    for nombre, par in PARES.items():
        print(f"{nombre:<28} {contraste(*par):5.2f}:1")
    print(f"Mínimo: {minimo:.2f}:1 (requerido ≥ 4.5:1)")
    sys.exit(0 if minimo >= 4.5 else 1)
