from flask import Flask,render_template,request
from dotenv import load_dotenv
import requests,os

#Flask module object initialization
appObj=Flask(__name__)

#Configuration to load from .env file.
load_dotenv()
backEndURI=os.getenv('SERV_BACKEND_URL')

"""
Front-ends Home/Default page rendering into browser
"""
@appObj.route("/")
def getHomePage():
    return render_template('index.html')

"""
Registration - form submission with '/api/submit' call routing with validations.
"""
@appObj.route("/api/submit",methods=['POST'])
def sumitUiFormData():
    form_data=dict(request.form)
    strResult=''
    strUserNameVal=request.form['uNameField']
    strEmailVal=request.form['userEmailFld']
    strIniPwdVal=request.form['iniPwdFld']
    strReConfPwdVal=request.form['reConfPwdFld']
    flag1=(len(strUserNameVal)!=0 and len(strEmailVal)!=0 and len(strIniPwdVal)!=0 and len(strReConfPwdVal)!=0)
    flag2=(strReConfPwdVal in strIniPwdVal)
    print("\nValue of Flags : "+str(flag1)+" "+str(flag2)+" ")
    if flag1:
        if flag2:
            requests.post(backEndURI+"/api/submit",json=form_data)
            return "Data submitted successfully"
        else:
            strResult="Reconfirm Password!!.. did't matched.."
    else:
            strResult="Fields! can't be empty."
    
    return render_template('index.html',frmSubmit_res=strResult)


"""
View-Details - button click from UI with '/api' call to render JSON lists.
"""
@appObj.route("/api")
def getViewJesonDataLists():
    strResponse=requests.get(backEndURI+"/api")
    return strResponse.json()

"""
call for 'main' module - for front-end app to load into browser.
"""
if __name__ == '__main__':
   appObj.run(debug=True,port=1010)
