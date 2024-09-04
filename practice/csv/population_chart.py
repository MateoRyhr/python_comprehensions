import os
import read_csv
import population
import charts

country_name_header = 'Country/Territory'

world_population_csv = f'{os.path.dirname(__file__)}/world_population.csv'

data = read_csv.read_csv(world_population_csv)

argentine_population = population.get_dict_slice(population.get_country_by_key_value(data,country_name_header,'Argentina'),range(5,13))
labels = list(argentine_population.keys())
labels.reverse()
print(f'Labels: {labels}')
values = list(argentine_population.values())
values.reverse()
print(f'Values: {values}')
charts.generate_bar_chart(
        labels,
        values
    )