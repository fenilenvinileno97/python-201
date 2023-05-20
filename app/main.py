import pandas as pd
import charts

def run():
    
    region = input('Enter a region =>')
    df = pd.read_csv('../data/countries.csv')
    df = df[df['Continent'] == region]
        
    countries = df['Country'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(region, countries, percentages)

if __name__ == '__main__':
    run()