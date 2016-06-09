Droplet
=======

Droplet is a blog application that allows a user to post any combination of any structural data (image, video, text, etc.).
The application is named such with the mental model that every post would represent "a droplet of your day"

### Setup

> - Include / mention adding SSH key or simply using HTTPS in the cloning process
> - Include some instructions on setup / depoyment on Windows

1. First, you need to clone the repo

    ```bash
    $ git clone git@github.com:abekim/droplet.git
    $ cd droplet
    ```

2. Download `pip` and `virtualenv`

    ```bash
    $ sudo easy_install pip 
    $ sudo sudo pip install virtualenv
    ```

3. Download and install `mongodb`

    ```bash
    $ brew install mongodb
    ```

4. Optionally, install `foreman` Ruby gem

    ```bash
    $ sudo gem install foreman
    ```

5. Optionally, you can setup an isolated environment using `virtualenv`

    ```bash
    $ virtualenv --no-site-packages env 
    $ source env/bin/activate
    ```

6. Install system dependencies. You may need to include `sudo` at the front of the command if on Linux

    ```bash
    $ pip install -r requirements.txt
    ```

7. Run the application locally

    If you've installed `foreman` earlier,

    ```bash
    $ foreman start
    ```

    Otherwise,

    ```bash
    $ python manage.py run
    ```

### Future Implementation

- Blog post interaction
	- Get post
	- Make a new post
	- Update an existing post
- User authentication

### Slugging

If you haven't heard of this term, [this wikipedia article](https://en.wikipedia.org/wiki/Slug_(publishing)) does a good job at describing its origin. Slug, in our use case, is a way to ensure that the unique URLs generated for each post is both human readable and insightful with respect to its contents.

While there are multiple ways to slug it, I've decided to slug with dates and post subjects.
