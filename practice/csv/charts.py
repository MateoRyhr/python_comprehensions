import matplotlib
import matplotlib.pyplot as plt

# Disable scientific notation on axes
    # by setting the threshold exponent very high
matplotlib.rcParams["axes.formatter.limits"] = (-99, 99)

def generate_bar_chart(labels, values):
    # ax --> coordenadas donde empezamos a graficar
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show();

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show();


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,200,300]
    # generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)