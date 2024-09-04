from data_processing.imports import pd
from data_processing.dictionaries import abbreviated_days, full_meals

def is_numeric(series_list: list[pd.Series]) -> None:
        for series in series_list:
            # Обновляем значения прямо в оригинальной серии
            series.update(pd.to_numeric(series, errors='coerce'))


def validate_values(possible_values, abbreviations=None):
    def decorator(func):
        def wrapper(column: pd.Series, *args, **kwargs) -> pd.Series:
            # Применяем проверку и преобразование
            def process_value(x):
                lower_x = x.lower()  # Приводим к нижнему регистру для проверки
                
                if lower_x in possible_values:
                    if abbreviations:
                        # Если передан словарь сокращений, возвращаем сокращение
                        return abbreviations[lower_x]
                    return x.capitalize()  # Иначе просто капитализируем
                return 'Unknown'
            
            # Применяем функцию ко всем значениям в колонке
            column = column.apply(process_value)
            return func(column, *args, **kwargs)
        return wrapper
    return decorator

@validate_values(['male', 'female'])
def is_gender(column: pd.Series) -> pd.Series:
    return column

@validate_values(['yes', 'no'])
def is_smoking_area(column: pd.Series) -> pd.Series:
    return column

@validate_values(['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun'])
def is_weekday(column: pd.Series) -> pd.Series:
    return column

@validate_values(['breakfast', 'lunch', 'dinner'])
def is_meal_time(column: pd.Series) -> pd.Series:
    return column


                  
            

