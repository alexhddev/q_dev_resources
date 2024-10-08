import matplotlib.pyplot as plt
import numpy as np

def initial_plot():
    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.show()

def plot_cosine_with_labels():
    x = np.linspace(0, 10, 100)
    y = np.cos(x)

    plt.plot(x, y, 'b-', label='cosine')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('Cosine Plot')
    plt.legend()
    plt.show()

def plot_cosine_and_sine():
    x = np.linspace(0, 10, 100)
    y1 = np.cos(x)
    y2 = np.sin(x)

    plt.plot(x, y1, 'b-', label='cosine')
    # sine line should be dashed:
    plt.plot(x, y2, 'r--', label='sine')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cosine and Sine Plots')
    plt.legend()
    plt.show()

def plot_world_population():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    populations = [2.5, 3.0, 3.7, 4.3, 5.0, 5.7, 6.4]

    plt.plot(years, populations, 'ro--')
    plt.xlabel('Year')
    plt.ylabel('Population (billions)')
    plt.title('World Population Over Time')
    plt.show()

# function that plots a pie chart with the usage of the most popular programming languages
def plot_programming_languages():
    languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
    usage = [70, 15, 10, 5, 5]

    plt.pie(usage, labels=languages, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Most Popular Programming Languages')
    plt.show()

    
    

plot_programming_languages()