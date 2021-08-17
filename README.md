
# Medical Insurance Premium

The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.

## Table of Content

  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Environment Setup](#Environment)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Technoloies Used](#TechnologiesUsed)
  * [Bug / Feature Request](#Bug/FeatureRequest)
  
  
## Demo

[![](https://user-images.githubusercontent.com/77889053/129683728-6197e11b-82e7-46f7-9a46-227ad1cdbd19.png)](https://medical-insurance-premium.herokuapp.com/)

## Overview
This is a Health Insurance Web Application which predicts cost of insurance by getting user inputs.

## Motivation
The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.

## Environment

Run this project on your local environment by following command:

- Create new Conda Environment
```bash
  create conda --name env_name python=3.x
```
- Activate the new Environment
```bash
  conda activate env_name
```

- Clone this Respository on Local Directory
```bash
  git clone https://github.com/ai-professor/medical-insurance-premium.git
```

  
## Installation


- import required libraries on current directory
```bash
  pip install -r requirements.txt
```

- Run the streamlit app by following command:
```bash
  streamlit run streamlitApp.py
```
## Dataset

You can find the dataset from Kaggle:
```bash
https://www.kaggle.com/noordeen/insurance-premium-prediction
```
The insurance.csv dataset contains 1338 observations (rows) and 7 features (columns). The dataset contains 4 numerical features (age, bmi, children and expenses) and 3 nominal features (sex, smoker and region) that were converted into factors with numerical value designated for each level.
## Screenshots

![form](https://user-images.githubusercontent.com/77889053/129684455-5db0ae6e-8704-48f2-affa-8f365e024acf.png)

![result](https://user-images.githubusercontent.com/77889053/129684568-2537c7df-a942-47b0-a22b-17d3fe4deb17.png)

  ## Directory Tree 
```
├── images 
├── models
    ├── DecisionTreeModel.pkl
    ├── LinearRegressorModel.pkl
    ├── RandomForestModel.pkl
    ├── XGBoostModel.pkl
├── Procfile
├── README.md
├── streamlitApp.py
├── app.ipynb
├── insurance_premium.ipynb
├── insurance.csv
├── requirements.txt
├── setup.sh
```

  
## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

**Random Forest Regression get the best fit accuracy, than other modesl like Linear Regression, Decision Tree, XGBoost Regression.** 
![rf](https://user-images.githubusercontent.com/77889053/129688924-cc7c625b-2312-4e70-b053-ffe61f42bce9.png)

**Develop and Deploy the Web app Using Streamlit,**
Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world.
![streamlit](https://user-images.githubusercontent.com/77889053/129688631-b0b583ea-c7b3-40f7-910a-49feb1572077.png)
## Bug / Feature Request

If you face any bug/issues (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/ai-professor/health-insurance-premium) here by including your search query and the expected result


## Support

For support, email creatorslab.ma@gmail.com or text me at telegram https://t.me/ai_professor

  
## 🚀 About Me
My Name is Dhanasekar, a passionate and Aspiring Data Scientist. I am enhancing my knowledge with the latest development in the field of Data Science with focus on Feature Engineering, Data pre-processing, Data collection (Web scraping) and model training. After some time you can call me self-taught Data Science Engineer from India.

  
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/techydhana-ai/)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/aiprofessor_)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
