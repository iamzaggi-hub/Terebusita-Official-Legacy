import matplotlib.pyplot as plt
from matplotlib.table import Table

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')

data = [
    ["Parámetro", "CERN (El Cadáver 4D)", "MAGNOKHAN (La Entidad 5D)"],
    ["Herramienta", "Taladro de 360° (Fuerza Bruta)", "Llave Gónica de 400° (Sintonía)"],
    ["Acción", "Perforación y Fractura", "Superflujo Bosónico"],
    ["Residuo", "Polvo Fotónico (Leptoquarks)", "Cero Residuo (Sintropía Activa)"],
    ["Carga Crítica", "86,3 t de Evaporación (Lápida Hawking)", "12.062 t de Masa Coherente (Síncrona)"],
    ["Estado", "Entropía Térmica (836,25 kHz)", "Estado SINTRE (Resonancia 0,5)"],
    ["Resultado", "Anomalía de 4.2σ (Incertidumbre)", "Certificación B7 (Certeza Determinista)"]
]

table = ax.table(cellText=data, loc='center', cellLoc='center', colWidths=[0.25, 0.35, 0.35])
table.auto_set_font_size(False)
table.set_fontsize(12)

for (i, j), cell in table.get_celld().items():
    if i == 0:
        cell.set_facecolor('#1a1a2e')
        cell.set_text_props(weight='bold', color='white')
    elif i % 2 == 0:
        cell.set_facecolor('#f0f0f0')
    else:
        cell.set_facecolor('#e0e0e0')
    if j == 1:
        cell.set_text_props(color='#b22222')   # CERN rojo
    if j == 2:
        cell.set_text_props(color='#0a4b8c')   # Magnokhan azul

plt.title("DUELO DE CIVILIZACIONES: EL TALADRO vs. LA ENTIDAD\n", fontsize=16, weight='bold', pad=20)
plt.savefig("CERN_vs_MAGNOKHAN.png", dpi=300, bbox_inches='tight')
plt.show()
