def runtime():
    greeting = "Hey, Hey, Hey!"
    name = "Repl"
    doa = "October 30"
    job = "Runtime Link"
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def planning():
    greeting = "Hey, Hey!"
    name = "Padlet"
    doa = "October 23"
    job = "Project Planning"
    embed = "https://padlet.com/jmortensen7/csptime1_2"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def journal():
    greeting = "Hey!"
    name = "Google Doc"
    doa = "October 16"
    job = "Journals"
    embed = "https://docs.google.com/document/d/1fioQivtuh1K1jUl7TWyhOu3eaMYt7DtLRx1GFxRu-Xw/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def playground():
    greeting = "Play, Play, Play!"
    name = "Replit"
    doa = "October 9"
    job = "Playground"
    embed = "https://repl.it/@jmort1021/Python-Hello-Series?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def code():
    greeting = "Code"
    name = "Gist"
    doa = "October 2"
    job = "Code Sample"
    gist = "https://gist.github.com/jm1021/cfb277c7357e02fcb4123a6c7429a5c1.js"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "gist": gist}
    return info

def alldata():
    return [runtime(), planning(), journal(), playground(), code()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Charlie-A Portfolio"
    
    source = {"name": name}
    #Project Data
    project1 =  "Hello Series"
    projlinks1 = [
        Link("Project Plan", "https://docs.google.com/document/d/1fl0xDhyVlljBU_9vBKrwyA1KdtyL13fyFEHq5LzqP-A/edit?usp=sharing"),
        Link("Repl", "https://repl.it/@charliezhu1/Hangman#README.md"),
        Link("Journals", "https://docs.google.com/document/d/1fioQivtuh1K1jUl7TWyhOu3eaMYt7DtLRx1GFxRu-Xw/edit?usp=sharing")
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", "https://docs.google.com/document/d/1IbB0bGAwiSk8j68Wcs0m1TMWh8LOb2xa7dvgEmebQjc/edit"),
        Link("Repl", "https://repl.it/@charliezhu1/Projectexploring#main.py"),
        Link("Resources", "https://docs.google.com/document/d/1fioQivtuh1K1jUl7TWyhOu3eaMYt7DtLRx1GFxRu-Xw/edit?usp=sharing")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
    #link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href

#Project data class contain project name and links (Link class objects)
class Project():
    #project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
    #HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    #source data getter
    def get_source(self):
        return self.source
    #project data getter
    def get_projects(self):
        return self.projects
