# Welcome to our Halloween Themed Portfolio!
By Sarah X, Charlie Z, Rohan N, Rivan N, and Noah P

This is our portfolio flask! Within this readme, we will walk through our thought processes and what we learned throughout our Flask journey.

# Run Instructions
In order to run the code you must first copy the project into Intellij. After copying the project from Intellij and choosing a configuration, you should be able to run the code and click the link at the bottom of the Intellij page. Once on the site, items in the navigation bar will direct you to our projects, about us section and music section.

# Features
Our Flask Web Portfolio/Flask Project has the following features:
* A landing page with our team name. This includes a hero header and a "headless horseman" CSS/JS animation.
* Responsive bootstrap navbar. Includes Home, About Us, Hello Series, Flask Project, and Music. We've edited our code so this navbar becomes a working dropdown on mobile.
* An About Us page. This page gives a brief overview of all the team members, including their Name, Birthday, Job, and a short description.
* A Hello Series and Flask Project page. These two pages include the respective project plans, repls, and journals for the two projects.
* A music encycopedia page. This page includes a half-page hero header, and a dropdown menu.
* The music page includes sub-pages for Pop, Rock, and Jazz. For each page, there are four example songs and their corresponding music videos, which are embedded from Vimeo.

# TODO's
Uncompleted TODOs are italicized. Ordered in chronological order of completion. 

* Create a working Halloween-themed Flask site on Repl
* Create a header with group name and members
* Link to project plans and journals through the repl-flask site
* Convert the Repl code to Github, download to intellij and ensure it works for all team members
* Add a working navbar
* Add a Hello Series and Flask Project page that includes the links to the documents. Ensure that the pages are accessable via the navbar
* Create plans and goals for the Flask Project. Delegate roles to team members and set goals. 
* Create a Music project that includes information and music for different types of music. Should have a homepage and three pages for pop, rock, and jazz.
* *Add animation into the Music Page - decided to not do this for formatting reasons, instead did large animation on Homepage*
* Combine the music page with the Flask project. Ensure that the templates are correct and work correctly.
* Add the About Us page. Create a .py to store dictionaries for the information.
* Embedd the links on the Flask Project and Hello Series as embeded documents. 
* Create a dropdown menu on the music page to store the pages from the previous music-only site
* Create a table template to store information on the music pages. Embedd videos that correspond with their respective songs.
* Add animation to the Halloween homepage
* Polish the descriptions for the music page
* Fix the formatting on the About us page (add paddings and margins, make the headers look better).


# Code Sections
Within our main.py section, we are basically setting up our website. The beginning lines basically quickstart Flask. We found out that the web adress actually is changing when the navbar is clicked, which was a really cool thing to see. For example, our web adress would change from http://portfolioflask.charliezhu1.repl.co/ to http://portfolioflask.charliezhu1.repl.co/hello/. This /hello/ can also be seen in our main.py section with the @app.route section below. We also dicovered that the certain templates are essentially formatting our website.

In the templates folder, there are several html files, which are used to format the website. Our website is set to have a navigation bar at the top of the page, where links can be clicked to get to another page to then see some of the work we've done. The base.html file acts as a template for the rest of the html files, as they are all fairly similar. Using {% block %} and {% endblock %}, we were able to use the base.html template for the other pages, while also being able to add things to each specific page to make them different (names, links, etc.). For the home.html file, we included a background image by using some <style> </style> details/insturctions from the base.html file as well as some code in our home.html file to import the image into only that file. 

In the projects.py section, variables are assigned to names and links so they can be used in the rest of the code. For example, the names, titles, and links to the different works we have done throughout the year are defined in this file. The variables are then assigned into lists that hold these variables for easier access in the other parts of the portfolio's code. These are then compiled using the functions towards the bottom of the code which replicate utilization of object based programming.

With the music section of our project, we first had the project on repl, in which we ended up transferring it into Github and Intellij. We created a new template html file so that the genres of music pages looked different than the pages with our projects on them. Instead of creating a whole new navigation bar, we decided to use a drop down menu instead which the user could select the three different genres of music we included: pop, rock and jazz. We embedded multiple videos on each page and added a brief description as well. 

# Self Grades
Rohan: 5/5(implemented the nav bar with bootstrap and accompanying variables, also edited the main.py file in order to better fit the needs of our portfolio)

Rivan: 5/5(changed the definition of each variable to suit our portfolio, which also meant changing links, and implementing a new href for our video.)

Noah: 5/5(utilized the jinja code in order to create space for headers and other aspects of the portfolio, was also able to figure out how to implement these headers and figured out how to do lists in html for the future.)

Sarah: 5/5(was able to implement the usage of images into the website for our theme, and was able to format the images and text to the correct areas.)

Charlie: 5/5(found out how to change the color of the div boxes in order to better show our theme, and also found out how to change text colors and background colors to fit the Halloween theme.) 
