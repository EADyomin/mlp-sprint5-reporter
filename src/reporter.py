import pandas as pd

class DataFrameReporter:

    def __init__(
        self,
        float_format: str = '0.05f',
        percent_format: str = '0.02%',
        include_all: bool = False
    ):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df: pd.DataFrame, title=None):
        if title:
            print(title)
        
        print('Количество столбцов:', df.shape[1])
        print('Количество строк:', df.shape[0])

        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)

        print('Доля дубликатов:', format(duplicates / df.shape[0], self.percent_format))

        print(df.describe(include='all' if self.include_all else None))
        
        # выведите количество пропусков во всем датафрейме одним числом
        missing_total = df.isna().sum().sum()
        print('Количество пропусков:', missing_total)
        
        # выведите долю пропусков во всем датафрейме одним числом с плавающей точкой
        # в формате float_format
        total_cells = df.shape[0] * df.shape[1]
        missing_fraction = missing_total / total_cells if total_cells else 0
        print('Доля пропусков:', format(missing_fraction, self.float_format))