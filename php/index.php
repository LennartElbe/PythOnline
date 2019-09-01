<!DOCTYPE html>
<HTML>

<HEAD>
    <TITLE>MEME</TITLE>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="css/style.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="js/ace/ace.js"></script>
    <script src="js/skulpt.js" type="text/javascript"></script>
    <script src="js/skulpt-stdlib.js" type="text/javascript"></script>
    <script type="text/javascript" src="./template.js"></script>
</HEAD>

<BODY>
    <div class="container-fluid" style="margin-left: 20px; padding-left: 5px;">
        <h1 style="margin-left: -15px;">PythOnline testing Skulpt</h1>
        <div class="row">Interpreter Mode:</div>
        <div class="row">
            <div class="dropdown">
                <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Clientside (Python 2.7.10)</button>
                    <div class="dropdown-menu" id="dropdownSwitchEngine" aria-labelledby="dropdownMenuButton">
                        <a class="dropdown-item active" id="clientside" data-toggle="button">Clientside</a>
                        <a class="dropdown-item" id="serverside" data-toggle="button">Serverside</a>
                    </div>
            </div>
            <div class="dropdown" style="float: right;">
                <button class="btn btn-secondary dropdown-toggle" style="margin-left: 10px" type="button" id="sheetsdropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Python Worksheets</button>
                    <div class="dropdown-menu" id="dropdownSwitchCode" aria-labelledby="dropdownMenuButton">
                        <!-- <a class="dropdown-item active" id="clientside" data-toggle="button">Clientside</a>
                        <a class="dropdown-item" id="serverside" data-toggle="button">Serverside</a> -->
                    </div>
            </div>
        </div>
        <div class="row">
                <p>Enter your program code in the left area and execute your program.</p>
            </div>
        </div>
        <div class="row" style="margin-bottom: 10px">
            <div class="col-sm" style="position: relative; margin-left: 25px; margin-right: 10px">
                <div id="program-code"></div>
            </div>
            <div class="col-sm" style="position: relative; height: 500px; margin-right: 25px">
                <div id="program-output"></div>
            </div>
        </div>
        <div class="row" style="margin-left: 10px; margin-bottom: 10px;">
            <button class="btn btn-success" style="margin-right: 10px" type="button" id="butt">Execute</button>
            <button class="btn btn-info" type="button" id="clear">Clear Output</button>
        </div>
    </div>
</BODY>

</HTML>