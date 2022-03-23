# automation-test-github
Github testing procedure to test login feature from github with invalid input

**Testcase**
1.  Login with valid email and wrong password. Expected value login failed (Negative)
2.  Login with wrong email and valid password. Expected value login failed (Negative)
3.  Login with empty email and valid password. Expected value login failed (Negative)
4.  Login with valid email and valid password hash md5. Expected value login failed (Negative)

**Test Report**
  xray.json
  html
 
**Automation Test Video**


https://user-images.githubusercontent.com/85162323/159639713-36e7d894-abd5-4499-84d9-d4f8822b4a6e.mp4

pytest -v --html=report.html --jira-xray --xraypath=xray.json .\automation-github.py   
