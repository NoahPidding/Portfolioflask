# Welcome to our Halloween Themed Portfolio!
By Sarah X, Charlie Z, Rohan N, Rivan N, and Noah P

This is our portfolio flask! Within this readme, we will walk through our thought processes and what we learned throughout our Flask journey.

# Run Instructions
In order to run the code you must first copy the project into Intellij. After copying the project from Intellij and choosing a configuration, you should be able to run the code and click the link at the bottom of the Intellij page. Once on the site, items in the navigation bar will direct you to our projects, about us section and music section.

# Sections
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
