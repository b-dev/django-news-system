******************
Django news system
******************

Simple news system based on Django.

Requirements
============

All requirements are listed in ``requirements.txt`` file.

Development environment
=======================

Python, virtualenv and dependencies
-----------------------------------

#. Install Python 2.6.x or 2.7.x. Installation steps depends on yours operating system.

#. Install Pip, the python package installer::

    sudo easy_install pip

   For more information about ``pip`` refer to http://www.pip-installer.org/.

#. I will recommend using ``virtualenv`` for development. This is great to have separate environment for
   each project, keeping the dependencies for multiple projects separated::

    sudo pip install virtualenv

   For more information about ``virtualenv`` refer to http://www.virtualenv.org/

#. Create virtualenv for the project. This can be inside the project directory, but cannot be under
   version control::

    virtualenv --distribute venv

#. Activate your virtualenv::

    source venv/bin/activate

   Later to deactivate use::

    deactivate

#. Clone the repository::

    git clone git://github.com/kgrodzicki/django-news-system.git

#. Navigate to project directory::

    cd django-news-system

#. Next step will be to install/upgrade dependencies from ``requirements.txt`` file::

    pip install -r requirements.txt

#. Create the database tables for all apps in INSTALLED_APPS whose tables haven't already been created::

    python manage.py syncdb

#. Run jetty server::

    python manage.py runserver --noreload

#. Sample application is now up and running - http://localhost:8000/news
