from data_processing.imports import st, pd, plt, sns, yf, np, datetime, warnings, markdown, io
from scripts.data_gen import data_generator
from scripts.charts_and_plots import *

warnings.filterwarnings('ignore')

st.write("""
#### Описание:
Здесь Вы можете провести некоторые иследования 
для своего ресторана, получить возможные взаимосвязи
и общую информацию. В качестве примера вам предоставлено
исследование по чаевым в вымышленном ресторане
с искусственно сгенерированными данными.
#### Важно:
Учитывайте стркутуру загружаемого файла,
он должен состоять  из **восьми** столбцов, как показано в примере,
столбец с нумерацией не должен присутствовать. 
Наименования столбцов могут быть какие угодно,
они будут изменены на верные. Столбец с датами также может
отсутствовать, в таком случае он будет сгенерирован, по принципу
начало **2023-01-01** и конец **2023-01-31**. 

    """)

# Функция загрузки и обработки файла с кэшированием
@st.cache_data
def load_and_clean_data(uploaded_file):
    # Проверяем расширение файла
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file, index_col=None)
    elif uploaded_file.name.endswith('.txt'):
        df = pd.read_csv(uploaded_file, delimiter='\t')

    # Убираем полностью пустые столбцы
    df = df.dropna(axis=1, how='all')

    # Убираем полностью пустые строки
    df = df.dropna(axis=0, how='all')

    # Применяем генератор данных к загруженному файлу
    df = data_generator(df)

    return df

uploaded_file = st.sidebar.file_uploader('Загрузи свой файл в следующем формате: csv, xlsx, txt', type=['csv', 'xlsx', 'txt'])

# Проверяем, что файл загружен
if uploaded_file is not None:
    # Список для проверки расширений файла
    bool_list = [
        uploaded_file.name.endswith('.csv'),
        uploaded_file.name.endswith('.xlsx'),
        uploaded_file.name.endswith('.txt')
    ]

    if any(bool_list):
        df = load_and_clean_data(uploaded_file)

        # Выводим датафрейм
        st.write(df)

        selected_plot = st.selectbox('Выберите график для отображения', list(plot_functions.keys()))
        fig = plot_functions[selected_plot](df)

        if fig is not None:
            st.pyplot(fig)

            # Сохраняем график в буфер (в памяти) в формате PNG
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)  # Возвращаемся к началу буфера

            # Кнопка для скачивания графика
            st.sidebar.download_button(
                label="Скачать график в формате PNG",
                data=buf,
                file_name="plot.png",
                mime="image/png")


    else:
        st.write("**Вы загрузили файл с неверным форматом**")
else:
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    tipsDf = pd.read_csv(url)
    tipsDf = data_generator(tipsDf)  # Применяем генератор данных
    st.write("**Экземпляр данных**")
    st.write(tipsDf)

    selected_plot = st.selectbox('Выберите график для отображения', list(plot_functions.keys()))
    fig = plot_functions[selected_plot](tipsDf)

    if fig is not None:
        st.pyplot(fig)

        # Сохраняем график в буфер (в памяти) в формате PNG
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)  # Возвращаемся к началу буфера

        # Кнопка для скачивания графика
        st.sidebar.download_button(
            label="Скачать график в формате PNG",
            data=buf,
            file_name="plot.png",
            mime="image/png")