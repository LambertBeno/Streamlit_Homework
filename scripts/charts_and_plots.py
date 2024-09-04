from data_processing.imports import plt, sns, st, pd

# Шаг 1: Динамика чаевых во времени
def plot_tips_over_time1(df: pd.DataFrame):
    df['Время_Заказа'] = pd.to_datetime(df['Время_Заказа'])
    grouped_df = df.groupby(df['Время_Заказа'].dt.date)['Чаевые'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(grouped_df.index, grouped_df.values, marker='o')
    ax.set_title('Динамика чаевых во времени')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Чаевые')
    return fig

# Шаг 1: Динамика чаевых во времени (Вариант 2)
def plot_tips_over_time2(df: pd.DataFrame):
    # Линейный график для чаевых во времени
    st.line_chart(df.set_index('Время_Заказа')['Чаевые'])

# Шаг 2: Гистограмма для total_bill
def plot_total_bill_histogram(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Чек'], bins=20, edgecolor='black')
    ax.set_title('Распределение счетов')
    ax.set_xlabel('Сумма счета')
    ax.set_ylabel('Частота')
    return fig

# Шаг 3: Scatterplot для связи между total_bill и tip
def plot_total_bill_vs_tip1(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Чек', y='Чаевые', ax=ax)
    ax.set_title('Связь между Чеком и Чаевыми')
    ax.set_xlabel('Сумма счета')
    ax.set_ylabel('Чаевые')
    return fig

# Шаг 3: Scatterplot для связи между total_bill и tip (Вариант 2)
def plot_total_bill_vs_tip2(df: pd.DataFrame):
    # Создаем scatterplot
    scatter_data = df[['Чек', 'Чаевые']]  # Выбираем нужные колонки для scatter chart
    st.scatter_chart(scatter_data)

# Шаг 4: Связь между total_bill, tip и size
def plot_total_bill_tip_size(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Чек', y='Чаевые', size='Людей', hue='Людей', palette='coolwarm', ax=ax)
    ax.set_title('Связь между Чеком, Чаевыми и Количеством людей за столом')
    ax.set_xlabel('Сумма счета')
    ax.set_ylabel('Чаевые')
    return fig

# Шаг 5: Связь между днём недели и суммой счета
def plot_day_vs_total_bill(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='День', y='Чек', estimator=sum, ax=ax)
    ax.set_title('Сумма счетов по дням недели')
    ax.set_xlabel('День недели')
    ax.set_ylabel('Сумма счета')
    return fig

# Шаг 6: Связь между днями недели, чаевыми и полом
def plot_day_vs_tip_vs_gender(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Чаевые', y='День', hue='Пол_официанта', palette='coolwarm', ax=ax)
    ax.set_title('Чаевые по дням недели с цветом по половому признаку')
    ax.set_xlabel('Чаевые')
    ax.set_ylabel('День недели')
    return fig

# Шаг 7: Boxplot для суммы счетов по дням недели, разделённых по времени дня
def plot_boxplot_day_vs_total_bill(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='День', y='Чек', hue='Время', ax=ax)
    ax.set_title('Сумма счетов по дням недели и времени дня')
    ax.set_xlabel('День недели')
    ax.set_ylabel('Сумма счета')
    return fig

# Шаг 8: Тепловая карта корреляций числовых переменных
def plot_heatmap(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Тепловая карта корреляций числовых переменных')
    return fig



plot_functions = {
    "Динамика чаевых во времени (Вариант 1)": plot_tips_over_time1,  # Вариант 1 с plt
    "Динамика чаевых во времени (Вариант 2)": plot_tips_over_time2,  # Вариант 2 с st.line_chart
    "Гистограмма для Чеков": plot_total_bill_histogram,
    "Связь между Чеком и Чаевыми (Вариант 1)": plot_total_bill_vs_tip1,  # Вариант 1 с plt
    "Связь между Чеком и Чаевыми (Вариант 2)": plot_total_bill_vs_tip2,  # Вариант 2 с st.scatter_chart
    "Связь между Чеком, Чаевыми и Количеством людей": plot_total_bill_tip_size,
    "Сумма чеков по дням недели": plot_day_vs_total_bill,
    "Чаевые по дням недели и полу": plot_day_vs_tip_vs_gender,
    "Сумма чеков по дням недели и времени дня": plot_boxplot_day_vs_total_bill,
    "Тепловая карта корреляций числовых переменных": plot_heatmap
}
