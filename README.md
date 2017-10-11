### HerokuPyRestApi Repository


This is a skeleton repo for Python projects. It is based off of Kenneth Reitz's sample module found [here](https://github.com/kennethreitz/samplemod). [Learn more](http://www.kennethreitz.org/essays/repository-structure-and-python).

We will use **_Heroku_** to deploy this app and test it there.

**Install Heroku command line**

then:
```bash
$ heroku login

```
Create a new app in Heroku from within your local Git new repository
```bash
$ heroku create

https://thawing-waters-31685.herokuapp.com/ | https://git.heroku.com/thawing-waters-31685.git
```

this would have created the remote URL to push code into Heroku
```bash
$ git remote -v

heroku	https://git.heroku.com/thawing-waters-31685.git (fetch)
heroku	https://git.heroku.com/thawing-waters-31685.git (push)
```
And then push the committed code (remember to do git commit -m "comment..")

```
$ git push heroku master
```
this will trigger the deployment of your app and the installation of the required modules and setup configuration to prepare Heroku Env to run your application

you can review your app once again into Heroku Dashboard to notice the difference after the push operation has completed

Since when we start Heroku deployment the platform tries to guess what type of application we are trying to deliver and given that we have a requirements.txt file
Heroku will imply this is a Python Project. 
Although, you might want to specify the Python version that you want, this can be done if you have a "runtime.txt" file in your project whereby you have to specify the
right version of your Python. Failing to do so Heroku installation will have the latest Python version which will be version 3 and that might not work as in your local project
where you might be using Python2.7

vi runtime.txt
```
python2.7.10
```

Final push:
```bash
$ git push heroku master

Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 305 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote:  !     Warning: Your application is missing a Procfile. This file tells Heroku how to run your application.
remote:  !     Learn more: https://devcenter.heroku.com/articles/procfile
remote:  !     The latest version of Python 2 is python-2.7.14 (you are using python-2.7.10, which is unsupported).
remote:  !     We recommend upgrading by specifying the latest version (python-2.7.14).
remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
remote: -----> Found python-3.6.2, removing
remote: -----> Installing python-2.7.10
```
**Here you can see how Heroku has proceeded to uninstalled previously assumed python3.6.2 with version requested 2.7.10**
***

Now you could set application's variable, like this one as an example which is useful to size Web concurrency and after setting it you can verify it like shown:
```
$ heroku config
=== thawing-waters-31685 Config Vars

$ heroku config:set WEB_CONCURRENCY=3
Setting WEB_CONCURRENCY and restarting ⬢ thawing-waters-31685... done, v5
WEB_CONCURRENCY: 3

$ heroku config
=== thawing-waters-31685 Config Vars
WEB_CONCURRENCY: 3
```

**Create a _Procfile_**

`Procfile` and like so, without any extension and with the capital letter has to be there in order to have _Heroku_ successfully start the _dynos_ . _(For any other details refer to [Heroku documentation](https://devcenter.heroku.com/articles/procfile))_

```bash
web: gunicorn pyrestapi.testapp:app
```
with this Heroku knows the type of application(*Process Type*) to run under name <web> and the command : _gunicorn_ (which is installed via _requirements.txt_)
then gunicorn cmdline has: (http://docs.gunicorn.org/en/latest/run.html)
```
$ gunicorn [OPTIONS] APP_MODULE

# Where APP_MODULE is of the pattern $(MODULE_NAME):$(VARIABLE_NAME). The module name can be a full dotted path. The variable name refers to a WSGI callable that should be found in the specified module.
```

So here, since we have a module (a dir with *\_\_init\_\_.py* in it) named **pyrestapi**, where inside we created **testapp.py** and that has app as our WSGI callable (provided by ```Flask()``` )
hence Heroku will know to trigger this command upon start of dynos and have gunicorn start our Flask application.

**Testing locally**

You can test this app locally using either ```Flask``` and just run _python_ referencing the _testapp.py_ or use **_Heroku_** local tool:
```
$ heroku local
```
