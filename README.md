# CalTTC Django
![](static/graphics/logos/logo_banner.png)
This is the django version of the CalTTC website.

## Setup Directions: How to get Started
1. Clone this repository to your machine (we will clone it to our desktop for this quickstart guide). In case you don't know how to clone a repo: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository.
1. Open up the terminal and run `pip install django` on your machine.
1. Download Visual Studio Code (VS Code) or your preferred text editor.
1. Start VS code and select File > Open Folder at `desktop/calttc_django`.
1. To start the website in the browser, open the terminal and navigate to desktop/calttc_django and run `python3 manage.py runserver' (you many need to install python if not already installed).
1. It should indicate that there is a localhost running the server. For me this is at 'http://127.0.0.1:8000/'.  Navigate to this in your browser and you should see the website.  
1. You are now ready to start messing around with the source code. I have included many in-line comments to assist you if you are not familiar with django or bootstrap.  Bootstrap is the system we are using to develop the frontend (the part that the user sees)on both mobile and desktop for responsive web design(design changes based on window size and device type).  Django allows us to simplify the backend with an included admin interface for managing or database (user records and models) and allows the webpage to be dynamic. I would recommend reading up on this in the links below.

If you are having trouble getting started with HTML.  I would watch the first few videos from this playlist:    
* [Basic HTML Tutorial](https://www.youtube.com/watch?v=gQojMIhELvM&list=PLoYCgNOIyGAB_8_iq1cL8MVeun7cB6eNc)    

If you are having trouble understanding bootstrap I would recommend looking at these links:  
* [Reference Guide](https://www.w3schools.com/bootstrap4/bootstrap_ref_all_classes.asp)      
* [Grid System](https://www.w3schools.com/bootstrap5/bootstrap_grid_basic.php)    
* [Navigation Bar](https://www.w3schools.com/bootstrap5/bootstrap_navbar.php)    
* [5 min Intro](https://www.youtube.com/watch?v=yalxT0PEx8c)    
* [1hour 30min Tutorial](https://www.youtube.com/watch?v=9cKsq14Kfsw)  

Django may have a steep learning curve depending on your prior experience.  Basically, it is a Model-View-Template framework.  When a user goes to a page on our site, it asks django to run a function called a 'view' which contains instructions on which html file we would like to load for the user.  We call this html file a 'template' because it can contain dynamic information which we indicate with "{{ fixed content }}" or "{% function %} (explained in more detail in the example below).
* [Model-View-Template Explanation](https://www.youtube.com/watch?v=GGkFg52Ot5o)
* [Django Example Application Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

## An Example of MVT in the website
Now that you should be familiar with the conceptual basics, I would like to show you an example of how we use the MVT to make our pages dynamic.  The example we will look at first is a dynamic html title which changes to indicate what page we are on in the browser. Although this may seem simple, the code can be a little bit confusing. We will also discuss how the bootstrap navbar changes depending on the page we are on.

1. Navigate to calttc_django/calttc_project directory. Here we will find two important files:
* urls.py
* views.py

2. Open the urls.py file in VS code. The urls.py files navigates users from the url to a particular 'view' or function call.  Take a look at the line with `path('home/', views.home, name='home'),` this indicates that if the url is 'https://calttc.berkeley.edu/home/' or 'http://127.0.0.1:8000/home/, it will call a 'view' or python function entitled `home` in the `views.py` file.
3. Open the views.py file in VS code. Looking in the `views.py` file we do find a function entitled home (`def home(request):`) which returns a render function:
```
# should just have "Cal Table Tennis" as Title for not 
# "Home | Cal Table Tennis" for search result optimization and
page_title = None
...
return render(request, "home.html",
	{
	'page_title': page_title,
	...
	'all_announcements': all_announcements,
	}
```
In this case, the render function has three arguments in this order: 
* request
* template
* context

The 'request' is the an abstraction of the users session which we need not worry about right now. 

The 'template' is a string that points toward a file in the templates folder in this case `templates/home.html`.

The 'context' is a dictionary that contains all the data we wish to pass into the template.

4. Open up the `templates/home.html' file in VS code.
At the top of the is file, it says `{% extends 'base.html' %}`.  This is known as a 'template tag' in django and it indicates that this file is an extension of 'base.html'. 'base.html' contains the header and footer for each page on the website.
1. Open up the `templates/base.html' file in VS code. This contains all of the page meta data as well as a bootstrap navbar. Take a look at the title tag: 
```
<title>
	{% if page_title %}
		{{ page_title }} | 
	{% endif %}
	Cal Table Tennis 
</title>
```
as you can see we can include logic in the tags as well.  For the home page, we set `page_title` to `None` so our title is simply Cal Table Tennis. If you go to the view for schedule, the `page_title` will be set to `Schedule` rather than `None`.

Notes:
* The pipe '|' is the standard notation for page and can be parsed by most browsers.
* We do not use 'Home | Cal Table Tennis' as the title because search engines will will display this as Home: Cal Table Tennis when a user searches for our website instead of just Cal Table Tennis.

Scrolling down further we see the navbar.  Do not be intimidated by this code. We will just look at one line right now:
```
{% url "schedule" as url %}
<a class="nav-link {% if request.path == url %}active{% endif %}" href={{ url }} style="padding-right:0; display:inline-block;">Schedule</a>
```
Bootstrap styling uses css classes to alter the navbar styling. `class="nav-link active"` indicates a highlighted navbar link where as `class="nav-link"` simply displays a grayed out link.  Here we assigned the url of schedule to a variable called `url`. We do this because if this url needs to be changed in the future we can just do so in the urls.py rather than change all of the templates. We now use the `request` context object's url to determine what page the user is on.  Comparing these with `==`, we can add the `active` class making the link appear highlighted.  

## Collaborator Push Protocol:

It is important to push to the repository properly to avoid merge conflicts.

1. If you already have a copy of the repo on your local machine, skip to step 2. If you haven't already, [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository to your computer.
2. Using your terminal, [cd and ls](https://tutorials.codebar.io/command-line/introduction/tutorial.html) into the new website repository: `cd calttc_django`
3. Before you start changing code, always make sure that you have the latest github remote repository by using `git pull`.
* If you forgot this step, no big deal, as long as you are not simultaneously editing the same code as another collaborator there will be no issue if you plan to merge this code back into the main branch.
4. Now we will create a new branch for your new feature using either:
* the `git checkout -b [yourbranchname]`.
* or the more complex `git branch [yourbranchname]` command and `git checkout -b [yourbranchname]`
You are now in a new branch.  You can go back to the main branch by running `git checkout main` or `git checkout master`.
5. Now you can go into VS Code and start working on your new branch. 
6. _(Optional)_ After you have made your changes, you can run the `git status` terminal command in your local repository to see the files you have changed.
7. Now you need to stage the files you modified for commit or in other words _add_ the files to be commited. You can stage or _add files two ways:
* stage individual files by doing `git add [yourfilename]`.    
* stage all of the files you changed by doing `git add .` or `git add -A`.    
8. Now that all of your changed files are staged, we can commit (basically saves the changes that you have made).  This allows us to restore this _commit_ later if we wish to.  Come up with a commit message that is relatively short and describes the changes that you have made.  Commit by running `git commit -m "[yourcommitmessage]"`. 
9. After the changes are committed, we can upload our local repository to the remote github repository.  This can be done using `git push`.
* You must be a __Collaborator__ on the CalTTC github page to do this step.  
* There is a possibility that you may have to do `git push --set-upstream origin [yourbranchname]` if it is your first time pushing.
10. Now your terminal will give you some instructions to do a pull request on `https://github.com/CalTableTennis/calttc_django/pull/new/[yourbranchname]`.    
Once on the [CalTTC Django Github Page](https://github.com/CalTableTennis/calttc_django), you will see a green button that says __compare & pull request__.  Click this.
11. Write a brief description of the changes you made in the __write__ tab so that other collaborators know what you did.
12. Wait until someone else leaves a comment approving the change and the __approve__ your pull request.  If required make the changes others require. 
13. Once there is approval you can merge the branch using the __merge__ function or the __squash and merge__ function if you want to delete the branch afterward. 

## Copying to the berkeley.edu domain:
1. To upload the github to the actual hosting domain, calttc.berkeley.edu, you need to go to your terminal and `ssh username@ssh.ocf.berkeley.edu` using the calttc credentials. You can upload the files with terminal commands although this can be tricky.
1. If you don't want to type in your password every time and just drag and drop to update the website, you should use a graphical interface (like cyberduck) with:
* Protocol: SFTP (or SSH)
* Host name: ssh.ocf.berkeley.edu 
* Port: 22
1. If you know how to manage it, you can also setup git on the OCF machine and do a `git pull` from that machine. (WARNING!) This has not been done as this can easily be screwed up. If a user pulls improperly overwriting the website database, It can cause irrecoverable data loss.

Visit the [Remote Shell and File Transfers](https://www.ocf.berkeley.edu/docs/services/shell/) page at the OCF website for more information regarding file uploads.