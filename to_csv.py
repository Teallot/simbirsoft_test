import pandas as pd


# Формирование csv файла
class ToCsv:
    @staticmethod
    def to_csv(any_dict, file_name):
        df = pd.DataFrame(any_dict)
        df.to_csv(f'{file_name}.csv', index=False, encoding='utf-8')
