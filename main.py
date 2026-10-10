from src.reporter import DataFrameReporter
import pandas as pd

def main():
    data = pd.read_csv('data/payments.csv')

    reporter_1 = DataFrameReporter(float_format='0.02f', percent_format='0.03%')
    reporter_2 = DataFrameReporter(float_format='0.03f', percent_format='0.01%', include_all=True)

    reporter_1.show_report(data, 'Отчёт в формате 1:')
    print()
    reporter_2.show_report(data, 'Отчёт в формате 2:')

if __name__ == '__main__': 
    main()