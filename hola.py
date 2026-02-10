import seaborn as sns
import matplotlib.pyplot as plt

# 1. Datos de ejemplo: Horas de estudio de dos grupos diferentes
datos = {
    'Grupo A': [2, 3, 3, 4, 4, 4, 5, 5, 6, 10], # El 10 es un valor atípico
    'Grupo B': [1, 2, 2, 3, 3, 3, 4, 4, 5, 6]
}

# 2. Configurar el estilo
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))

# 3. Crear el gráfico de caja
sns.boxplot(data=[datos['Grupo A'], datos['Grupo B']], palette="Set2")

# 4. Personalización
plt.xticks([0, 1], ['Grupo Presencial', 'Grupo Virtual'])
plt.title("Comparativa de Horas de Estudio (Boxplot)", fontsize=14)
plt.ylabel("Horas por semana")

# 5. Guardar
plt.savefig("grafico_caja.png")
print("¡Boxplot generado como grafico_caja.png!")