Droplet
=======

Droplet is a blog application that allows a user to post any combination of any structural data (image, video, text, etc.).
The application is named such with the mental model that every post would represent "a droplet of your day"

### Setup

1. Make sure you have Node.js and `npm` installed. Running the following two commands will verify that they are installed.

    ```bash
    $ node -v && npm -v
    ```

    If either is not installed, install the instructions for [installing Node.js](https://nodejs.org/en/download/package-manager/) (`npm` is included as a part of Node.js) and/or [installing npm](http://blog.npmjs.org/post/85484771375/how-to-install-npm)

2. Next, you need to clone the repo.

    ```bash
    $ git clone git@github.com:abekim/droplet.git
    ```

    If you have yet to add an SSH key for your GitHub account, you can either follow the [instructions by GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) or clone the repository using HTTPS:

    ```bash
    $ git clone https://github.com/abekim/droplet.git
    ```

3. Enter the cloned directory and install local dependencies:

    ```bash
    $ npm install
    ```

4. Start the server

    ```bash
    $ npm start
    ```

### Future Implementation

- Blog post interaction
	- Get post
	- Make a new post
	- Update an existing post
- User authentication
    - Admin

### Slugging

If you haven't heard of this term, [this wikipedia article](https://en.wikipedia.org/wiki/Slug_(publishing)) does a good job at describing its origin. Slug, in our use case, is a way to ensure that the unique URLs generated for each post is both human readable and insightful with respect to its contents.

While there are multiple ways to slug it, I've decided to slug with dates and post subjects.
