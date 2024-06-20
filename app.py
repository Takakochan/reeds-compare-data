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
ftp.login(ftpname, key)
ftp.prot_p()
ftp.set_pasv('true')
ftp.cwd(path)
flo = BytesIO()
flo.seek(0)
data = pd.read_csv(flo, encoding='UTF8',sep=";")
data = data.set_index(['Length'])
df = pd.DataFrame(data)

columns = st.sidebar.multiselect("Columns:", df.columns)
filter = st.sidebar.radio("Choose by:", ("inclusion", "exclusion"))

if filter == "exclusion":
    columns = [col for col in df.columns if col not in columns]
df[columns]
data1 = df[columns]
#data = data.drop['Unnamed']
df = pd.DataFrame(data)
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.sidebar.button('Plot graph'):
    data1.plot()
    plt.show()
    st.pyplot()
