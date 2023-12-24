# Define your HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{}</title>
    <link rel="icon" href="https://obsidian.md/images/obsidian-logo-gradient.svg">
    <link rel="stylesheet" href="../styles.css">
  </head>
  <body>
    <div>
        <md-block>{}</md-block>    
    </div>
	<script type="module" src="https://md-block.verou.me/md-block.js"></script>
  </body>
</html>
"""


# Define your CSS template
css_template = """
body {
    font-family: 'Arial', sans-serif;
    background-color: #333;
    color: #e4e4e4; 
    padding: 5%; 
}

p {
    line-height: 1.5; 
}

a {
    color: #8a2be2; 
    text-decoration: none; 
}

a:hover {
    text-decoration: underline; 
}"""