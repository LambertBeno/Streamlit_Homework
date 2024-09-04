from data_processing.imports import st, yf, datetime, markdown


st.write("""
# Простое приложение для визуализации котировок акций
         
Возможна демонстарция **цены закрытия** и **объёма торгов**
по выбранному **Тикеру** и периоду доступному по данному **Тикеру**
         """)

tickerSymbol = st.text_input('Впишите **Тикер**')
tickerData = yf.Ticker(tickerSymbol)
history = tickerData.history(period="max")
    
if history.empty:
    st.write(f"Нет данных для тикера **{tickerSymbol}**.")
else:
    st.write(f"Исторические данные для {tickerSymbol}:")

    first_date = history.index.min().date()
    last_date = history.index.max().date()

    start_date = st.date_input(
        "Выберите начальную дату",
        value=first_date,
        min_value=first_date,
        max_value=last_date
        )

    end_date = st.date_input(
        "Выберите конечную дату",
        value=last_date,
        min_value=start_date,
        max_value=last_date
        )
    
    interval = st.selectbox(
    "Выберите интервал данных",
    options=["1d", "1wk", "1mo", "3mo"],
    index=3
    )


    if start_date > end_date:
        st.error("Конечная дата должна быть больше или равна начальной дате.")
    else:
        st.write(f"Вы выбрали период с {start_date} по {end_date}")

    tickerDf = tickerData.history(start=start_date, end=end_date, interval=interval)

    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
