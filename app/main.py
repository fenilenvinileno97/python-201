<<<<<<< HEAD
import charts

def run():
    labels = ['Colombia', 'Argentina', 'Brazil']
    values = [200, 34, 120]
    charts.generate_bar_chart(labels, values)
=======
import pandas as pd
import charts

def run():
    
    region = input('Enter a region =>')
    df = pd.read_csv('../data/countries.csv')
    df = df[df['Continent'] == region]
    
    countries = df['Country'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(region, countries, percentages)
>>>>>>> 2a28d8b (Pandas use in former app project in use in former app project from Python 102)

if __name__ == '__main__':
    run()