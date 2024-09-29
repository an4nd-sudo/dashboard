import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')



st.title('India')

df = pd.read_csv('xl1.csv')
#with st.expander('show data'):
 #   st.dataframe(df)


st.header('Population Of India')
fig6= px.line(df,x="State/UTs", y="Population")
st.plotly_chart(fig6)


st.header('Covid-19 cases in India')


fig7= px.pie(df,values=['Zone'])
st.plotly_chart(fig7)





#data = ['Total Cases','Active','Discharged','Deaths']

#op = st.sidebar.selectbox('select a Data to Display',df[''])

#data = st.sidebar.selectbox('Select a State',df['State/UTs'].unique())


col1,col2,col3,col4 = st.columns(4)

cont1=col1.container(border=True,)
cont1.metric('Total Cases',round(df['Total Cases'].sum()))

cont2=col2.container(border=True)
cont2.metric('Recovered',round(df['Discharged'].sum()))

cont4=col4.container(border=True)
cont4.metric('Death',round(df['Deaths'].sum()))

cont3=col3.container(border=True)
cont3.metric('Active',round(df['Active'].sum()))





col9,col10,col11,col12= st.columns(4)

fig1= px.bar(df,x="Total Cases", y="State/UTs",text='Total Cases')
cont1=col9.container(border=True)
cont1.plotly_chart(fig1)


fig3= px.bar(df,x="Discharged", y="State/UTs")
cont2=col10.container(border=True)
cont2.plotly_chart(fig3)


fig4= px.bar(df,x="Active", y="State/UTs")
cont3=col11.container(border=True)
cont3.plotly_chart(fig4)

fig5= px.bar(df,x="Deaths", y="State/UTs")
cont4=col12.container(border=True)
cont4.plotly_chart(fig5)


st.header('Active Covid Cases in India')
fig8= px.line(df,x="State/UTs", y="Active Ratio")
st.plotly_chart(fig8)

st.header('Revovery ration of India')
fig9= px.line(df,x="State/UTs", y="Discharge Ratio")
st.plotly_chart(fig9)

st.header('Average recovery ratio Of India')
fig10= px.line(df,x="State/UTs", y="Discharge Avg")
st.plotly_chart(fig10)

st.header('Average Death ratio of India')
fig11= px.line(df,x="State/UTs", y="Death Avg")
st.plotly_chart(fig11)








#st.subheader('Cases Reported in Each State')

#df2 = df[df['State/UTs']==data]

#col5,col6,col7,col8= st.columns(4)
#cont5=col5.container(border=True)
#cont5.metric('Total Cases',df2['Total Cases'])

#cont6=col6.container(border=True)
#cont6.metric('Recovered',df2['Discharged'])



#cont7=col7.container(border=True)
#cont7.metric('Deaths',df2['Deaths'])

#cont8=col8.container(border=True)
#cont8.metric('Active',df2['Active'])


#fig6= px.line(df,x="State/UTs", y="Population")
#st.plotly_chart(fig6)



#col13,col14,col15 = st.metric(3)




