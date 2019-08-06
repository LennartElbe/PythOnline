<!DOCTYPE html>
<HTML>

<HEAD>
    <TITLE>MEME</TITLE>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="js/ace/ace.js"></script>
    <script src="js/skulpt.js" type="text/javascript"></script>
    <script src="js/skulpt-stdlib.js" type="text/javascript"></script>
    <script type="text/javascript" src="./template.js"></script>
</HEAD>

<BODY>
    <div class="container-fluid">
        <div class="row">
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Interpreter Mode</button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <a class="dropdown-item" id="clientside">Clientside</a>
                    <a class="dropdown-item" id="serverside">Serverside</a>
                </div>
            </div>
                <h1>Python simulator for programming class</h1>
                <p>Enter your program code on the right and press the "Press Me" button to execute your program.</p>
            </div>
        </div>
        <div class="row">
            <div class="col-sm" style="position: relative;">
                <div id="program-code">
                </div>
            </div>
            <div class="col-sm" style="position: relative; height: 500px;">
                <div id="program-output">
                </div>
            </div>
        </div>
        <div class="row">
            <button class="btn btn-primary" type="button" id="butt">Press Me</button>
            <button class="btn btn-info" type="button" id="clear">Clear Output</button>
        </div>
    </div>
</BODY>

</HTML>