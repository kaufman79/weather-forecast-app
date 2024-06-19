import streamlit as st
import plotly.express as px
from backend import get_data

# add ST widgets
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select the data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the Temperature data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            temps_fahrenheit = [(temp * 9 / 5 + 32) for temp in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # create a temperature plot
            figure = px.line(x=dates, y=temps_fahrenheit, labels={"x": "Date", "y": "Temperature(F)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write(f"'{place}' is not a valid city name. Check your spelling and try again.")
