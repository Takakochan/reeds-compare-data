import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from ftplib import FTP_TLS
import ftplib
from io import BytesIO
import io


ftp = FTP_TLS('minty-web.com')
print('going to the sever....')
print('loged in....')
ftp.login(st.secrets["ftpname"], st.secrets["key"])
ftp.prot_p()
ftp.set_pasv('true')
ftp.cwd(st.secrets["path"])
flo = BytesIO()
ftp.retrbinary('RETR ' + 'ReedsData3.csv', flo.write)
flo.seek(0)
data = pd.read_csv(flo, encoding='UTF8',sep=";")
data = data.set_index(['Length'])
df = pd.DataFrame(data)

columns = st.sidebar.multiselect("Select reeds to compare:", df.columns)
filter = st.sidebar.radio("Choose by:", ("inclusion", "exclusion"))

if filter == "exclusion":
    columns = [col for col in df.columns if col not in columns]
df[columns]
data1 = df[columns]
#data = data.drop['Unnamed']
df = pd.DataFrame(data)
#st.set_option('deprecation.showPyplotGlobalUse', False)
if st.sidebar.button('Click for Visualisation!'):
    data1.plot()
    plt.show()
    st.pyplot()
