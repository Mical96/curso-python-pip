import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C'] #etiquetas
    values = [200, 34, 120] #sus valores

    fig, ax = plt.subplots() #fig = figura, ax = coordenadas 
    ax.pie(values, labels=labels)
    plt.savefig('pie.png') #aqui se guarda la imagen
    plt.close()
    
    #plt.show: muestra la grafica pero se detiene el codigo