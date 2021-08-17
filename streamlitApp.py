import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image

icon = Image.open('images/heart.png')
# webpage title:
st.set_page_config(page_title = 'Health Insurance App', page_icon = icon)


rf = open('models/RandomForestModel.pkl', 'rb')
model = pickle.load(rf)

# funtion of predict cost of insurance 
def insurance_data(age, gender, bmi, kids, smoker, region):
	input_data = (age, gender, bmi, kids, smoker, region)

    # changing input_data to a numpy array
	input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array
	input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
	result = model.predict(input_data_reshaped)
	return int(result[0])


def main():
    # st.title("Medical Insurnce Premium")
	img = Image.open("images/form.jpg")
	st.image(img, width = 700)


	html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Medical Insurance Premium </h2>
    </div>
    """
	st.markdown(html_temp,unsafe_allow_html=True)
	st.header("Enter Your Details: ")
	Age = st.text_input("Age:")
	Gender = st.radio("Select Gender (Male : 0, Female : 1): ", (0, 1))
	BMI = st.text_input("BMI: (Formula : Weight / Height in Metered Square)")
	Childrens = st.selectbox("How Many Childrens Do You Have:", [0, 1, 2, 3, 4, 5])
	Smoker = st.radio("Smoker: (Yes : 0, No : 1): ", (0, 1))
	Region = st.selectbox("Region: (SouthEast : 0, SouthWest : 1, NorthEast : 2, NorthWest : 3): ", [0, 1, 2, 3])

	result=""
	if st.button("USD"):
		result = insurance_data(Age, Gender, BMI, Childrens, Smoker, Region)
		st.success('The Predicted Amount is : {} USD'.format(result))
		st.write("Click the Rupees Button to View as Amount in Rupees: ")
	if st.button("Rupees"):
		result = insurance_data(Age, Gender, BMI, Childrens, Smoker, Region)
		st.success('The Predicted Amount is : {} Rupees'.format(result * 74))


	Developer = "Developed By Dhanasekar M"
	st.text(Developer)
 

if __name__=='__main__':
	main()