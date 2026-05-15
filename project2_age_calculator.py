import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import date

st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered"
)

st.title("🎂 Age Calculator")

st.write("Calculate your exact age in years, months, and days.")

dob = st.date_input(
    "Enter Your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    value=date(2000, 1, 1)
)

if st.button("Check Age"):
    today = date.today()
    age = relativedelta(today, dob)

    st.success(
        f"Your age is {age.years} Years, {age.months} Months and {age.days} Days."
    )

    total_days = (today - dob).days

    st.info(f"You have lived approximately {total_days:,} days.")

    next_birthday = date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    days_left = (next_birthday - today).days

    st.warning(f"{days_left} days left until your next birthday 🎉")


# Command to run -  py -m streamlit run project2_age_calculator.py