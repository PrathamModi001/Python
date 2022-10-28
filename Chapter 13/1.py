# A virtual environment is useful in situations when we made a project in flask 0.5.2 and latest is 1.1.x version but we dont want to remake the project in 1.1.x but we now want to work on latest version of flask.
# So we want two different version of flask so we can execute this situation if create a virtual environment for the project and at system interpretor we can continue with the 1.1.x version

# =====================================================================================
# To install virtual environment, write:
# 1. pip install virtualenv (in the windows powershell (terminal wala powershell))
# To create an environment, write:
# 2. virtualenv myprojectenv {or any other name at this place}
# Now the virtual environment is craeted but we must activate it
# 3. .\myproject\Scripts\activate.ps1
# if any issues search virual environment wont activate windows stackoverflow to get the solution
# ======================================================================================

# Now since the virtualenv is installed its like running two pythons at the same time with the option to chose btw them.
# we can choose btw them,by selecting the 3.9.10 or whatever at the bottom right/left corner according to your settings, then run the terminal again by closing all other terminals now the virtualenv will open.
# ===========================================================================================

# we can get a lsit of all the modules presnet in the system interpreter and the virtenv by writing a command 
# pip freeze
#  if we want to make a text file that contains the current installed versions of modules we can do:
# pip freeze > requirements.txt or {whatever}.txt
# =========================================================================================

# we can also help someone else create the same environment by creating the requirements.txt using pip freeze > requiremnts.txt and then give this text file to the other person and the write the code:
# pip install -r requiremnts.txt
# =========================================================================================