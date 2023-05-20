import csv

def read_csv(filepath):
  with open(filepath, "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = list(zip(header, row))
      iter_dict = {key: value for (key, value) in iterable}
      data.append(iter_dict)
    return data


if __name__ == '__main__':
  print(read_csv('./data/countries.csv'))
