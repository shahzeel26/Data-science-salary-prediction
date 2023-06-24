import streamlit as st
import pandas as pd
import numpy as np
from encoder import Encoder
from remove_outlier import remove_outlires
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

def prediction():
    st.title('Salary prediction of data science field')
    ab=pd.read_csv('D:\zeel\projects\data_science salary prediction\ds_salaries.csv')
    ab['experience_level'] = ab['experience_level'].replace(['EN', 'MI', 'SE', 'EX'],['Entry-Level', 'Mid-Level', 'Senior-Level', 'Executive-Level'])
    ab['employment_type'] = ab['employment_type'].replace(['PT', 'FT', 'FL', 'CT'], 
                                                        ['Part-Time', 'Full-Time', 'Freelance', 'Contract'])
    ab['remote_ratio'] = ab['remote_ratio'].replace([100, 0, 50], ['remote', 'on-site', 'hybrid'])
    ab['company_size'] = ab['company_size'].replace({'L':'large', 'S':'small', 'M':'medium'})
    b=ab.drop(columns='employee_residence',axis=1)
    b=b.drop(columns='salary_in_usd',axis=1)
    b=b.drop(columns='salary',axis=1)
    b=b.drop(columns='company_location',axis=1)
    # a=b.copy()
    ab= Encoder(ab)
    ab = remove_outlires(ab, 'salary_in_usd', 2)
    X=ab.drop(columns='employee_residence',axis=1)
    X=X.drop(columns='salary_in_usd',axis=1)
    X=X.drop(columns='salary',axis=1)
    X=X.drop(columns='company_location',axis=1)
    
    scaler=StandardScaler()
    scaler.fit(X)
    standardized_data=scaler.transform(X)
    X=standardized_data
    Y=ab['salary_in_usd']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=2)
    # training_data_prediction=model.predict(X_train)
    model=LinearRegression()
    model.fit(X_train,Y_train)
    d=b['job_title'].unique()
    d.sort()
    e=b['experience_level'].unique()
    e.sort()
    l=b['employment_type'].unique()
    l.sort()
    p=b['salary_currency'].unique()
    p.sort()
    o=b['remote_ratio'].unique()
    o.sort()
    q=b['company_size'].unique()
    q.sort()
    work_year=st.number_input('work_year',min_value=2020,max_value=2050,value=2020)
    experience_level=st.selectbox(
    'Type or select experience level from the dropdown',
    e[0:])
    for i in range(0,len(e)):
        if e[i]==experience_level:
            f=i
            break
    
    employment_type=st.selectbox(
    'Type or select employment type from the dropdown',
    l[0:])
    for i in range(0,len(l)):
        if l[i]==employment_type:
            k=i
            break

    job_title=st.selectbox(
        'Type or select job title from the dropdown',
        d[0:])
    for i in range(0,len(d)):
        if d[i]==job_title:
            j=i
            break

    salary_currency=st.selectbox(
        'Type or select salary currency from the dropdown',
        p[0:])
    for i in range(0,len(p)):
        if p[i]==salary_currency:
            m=i
            break
    remote_ratio=st.selectbox(
        'Type or select type of working from the dropdown',
        o[0:])
    for i in range(0,len(o)):
        if o[i]==remote_ratio:
            r=i
            break
    company_size=st.selectbox(
        'Type or select company size from the dropdown',
        q[0:])
    for i in range(0,len(q)):
        if q[i]==company_size:
            s=i
            break
    if st.button('Predict the price'):
            input_data =(work_year,f,k,j,m,r,s) 
            input_data_as_numpy_array=np.asarray(input_data)
            input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
            std_data=scaler.transform(input_data_reshaped)
            prediction=model.predict(std_data)                         
            st.success(prediction)
            st.write("in USD")






    