from data_processing.imports import st, pd, plt, sns, yf, np, datetime, warnings, markdown
from modules.functions import is_numeric, is_gender, is_smoking_area, is_meal_time, is_weekday

def data_generator(data: pd.DataFrame) -> pd.DataFrame:

    if 7 <= len(data.columns) < 9:
        if len(data.columns) == 7:
            start_date = pd.to_datetime('2023-01-01')
            end_date = pd.to_datetime('2023-01-31')
            
            data['time_order'] = pd.to_datetime(np.random.randint(
                start_date.value,
                end_date.value,
                len(data)), unit='ns')
        else:
            pass
        # Переименовываем колонки
        new_names_df = pd.DataFrame({
        'new_names': [
            'Чек',
            'Чаевые',
            'Пол_официанта',
            'Зона_курения',
            'День',
            'Время',
            'Людей',
            'Время_Заказа']})

        new_column_names = new_names_df['new_names'].tolist()
        data.columns = new_column_names
        data['Время_Заказа'] = data['Время_Заказа'].dt.date

        # Обработка числовых столбцов
        is_numeric([data['Чек'], data['Чаевые'], data['Людей']])
        
        # Обработка остальных столбцов
        data['Пол_официанта'] = is_gender(data['Пол_официанта'])
        data['Зона_курения'] = is_smoking_area(data['Зона_курения'])
        data['День'] = is_weekday(data['День'])
        data['Время'] = is_meal_time(data['Время'])
        

    else:
        data = st.write("Ваш файл не соответствует требованиям.")

    return data