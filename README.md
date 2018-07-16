Before anything else…
Download the ChromeDriver and CHMOD it to your system
- For ChromeDriver Download the ChromeDriver from here https://sites.google.com/a/chromium.org/chromedriver/downloads And extract it to your "Downloads" folder
- In your terminal, cd to Downloads folder as follows : cd Downloads chmod +x chromedriver and move the downloaded binary to /usr/local/bin as follows: sudo mv -f [name of the extracted ChromeDriver file] /usr/local/bin


## **Running the examination solution**

**A. Preconditions**

1. Python 3.4 and above
2. virtualenv
3. pip
4. ChromeDriver binary


**B. Installation**

Python 3
- Ignore this if you have Python 3 installed in your machine
- Follow the instruction from here http://docs.python-guide.org/en/latest/starting/install3/osx/

virtualenv
- pip3 install virtualenv

pip
- This comes with Python installation by default, so all you need is to upgrade it.
- pip3 install --upgrade pip


**C. Creating Virtual Environment**

1. Open terminal.

2. Go to the directory which you want to put your virtual environment. In this example, let us use the `/Documents` folder.

3. Run `python3 -m virtualenv <your_virtual_env_name>`
You should see something similar to :

Using base prefix '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6'
New python executable in /path/to/Documents/py3poc/<your_virtual_env_name>/bin/python3.6
Also creating executable in /Users/<machine_name>/Documents/<your_virtual_env_name>/bin/python
Installing setuptools, pip, wheel...done

4. Once it's `done`, you now have the virtual environment!

**D. Activating the Virtual Environment**

1. `cd` to the virtual environment folder you created.
In this example, let's use `test-env`. Assuming you created virtual environment with name `test-env` in the step C.3 above, go to that folder by running, `cd test-env`.

2. Once inside the folder, run `source bin/activate`. Your terminal will look similar with this :

(test-env) Jamess-MacBook-Pro:test-env jmarturillas$

Take note of the virtual environment name enclosed with parentheses `(test-env)`. This is an indicator that your virtual environment is now activated.

**E. Cloning the `rf-test-automation` repository.**

1. Clone the examination repository as follows :
`git@github.com:jmarturillas/rf-test-automation.git`

F. Installing all the libraries of the repository

1. Open the PyCharm

2. Open the `rf-test-automation` from the directory where you downloaded it. In this example, it should be residing on `/Users/<machine>/Documents/test-env`

3. Open the PyCharm terminal.

4. Run `pip install -r requirements.txt`

5. Once the installation is complete, it's time to install the modified `robotframework-pageobjectlibrary` dependency.
The reason why this is `modified` is because it only supports Python 2 so I had to modify its `setup.py`.
To install this, `cd` to it's directory by running `cd robotframework-pageobjectlibrary` then `pip install .`

**PS : Do not overlook the dot (.) after the `install` in the command above.**

**G. Running the rf-test-automation**

1. Create a directory in your desktop for auto-generated logs of RobotFramework.

2. Open the PyCharm terminal and run the following command :

`/Users/<machine_name>/Documents/<your_virtual_env_name>/rf-test-automation/venv/bin/robot -d /Users/<machine_name>/Desktop/test/logs/ /Users/<machine_name>/Documents/<your_virtual_env_name>/rf-test-automation/mv_skill_test/tests/login/Login.robot`


**NOTE : The command above will run the whole Login.robot and it’s test cases.**
