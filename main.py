from mainWindow import MainWindow


if __name__== "__main__":
    app = MainWindow() 

# Notes: We now using md-block, a custom html element that renders
# markdown. Just download the js file
# from https://md-block.verou.me/md-block.js
# The idea will be. Python will download that js script. place it
# into the directory with the html files so that the html can find it
# then simply write the md file content into an html template with
# the md-block element in it. 