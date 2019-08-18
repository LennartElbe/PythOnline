var editor; // for input
var editor2; // for output
var server;

function outf(text) {
    //var mypre = document.getElementById("program-output");
    // jQuery('#program-output').html(text);
    //jQuery('#program-output').setValue(text);
    //editor2.setValue(editor2.getValue() + "\n" + text);
    editor2.insert(text);
    //mypre.innerHTML = mypre.innerHTML + text;
}

function clear() {
    // clear the output
    editor2.setValue("");
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function clientDoIt() {
    console.log("clientdoit")
    console.log("This is a function");
    // get the content of the first textarea
    //var editor = ace.edit("program-code");
    var prog = editor.getValue();
    // var prog = document.getElementById("text").value;
    //var mypre = document.getElementById("output");
    var mypre = jQuery('#program-output');
    //mypre.innerHTML = '';
    //jQuery('#program-output').html(""); // sollte den Output leer darstellen
    Sk.pre = "output";
    Sk.configure({ output: outf, read: builtinRead });
    var myPromise = Sk.misceval.asyncToPromise(function() {
        // ich dachte das hier ist das - diese Stelle definiert einen call
        // der wird gesendet (an wen weiss ich noch nicht) und als ausgabe 
        // bekommst Du einen Promise (ein Versprechen das das auch ausgefuehrt wird, im Hintergrudn)
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    // hier warten wir dann auch den promise - das er erfuellt wird und 'dann' == then
    // wo genau steht denn: interpret("this python code")
    // ok die zeile ist das skulpt magic? Ja, ist in der Sk versteckt.
    // Es kann sein das es das Program an einen Rechner schickt - der dir nicht gehoert
    // skulpt ist 100% clientside interpretation and runnning also schickt es es an den client oder?
    myPromise.then(function(mod) {
            console.log('success');
            // ok, here we should  get the output of the program
            // kannst Du hier einen breakpoint setzen?

        },
        function(err) {
            console.log(err.toString());
        });
    console.log("program is: " + prog);
    console.log("attempting to execute program now");

    // python code interpreted (wo??)
    //    var editor2 = ace.edit("program-output");
    //    editor2.setValue(prog);
}

function serverDoIt() {
    console.log("serverdoit")
    var prog = editor.getValue();
    jQuery.getJSON('computeOnServer.php', { 'code': prog }, function(data) {
        // got a response from the server
        //editor2.setValue(editor2.getValue() + data['output']);
        editor2.insert(data['output'] + '\n');
    });
}

function doIt() {
    if (server) {
        serverDoIt();
    } else {
        clientDoIt();
    }
}

jQuery(document).ready(function() {
    console.log("This line is printed after the page is loaded.");
    jQuery('#serverside').click(function() {
        server = true;
        console.log("server is now true");
        // set the button to blue
        jQuery("#dropdownSwitchEngine").children().removeClass('active');
        jQuery(this).addClass('active');
        jQuery("#dropdownMenuButton").text('Serverside (Python 3.7.3)');
        editor2.insert("\n========== Now Interpreting in Python 3.7.3 ==========\n");
    });
    jQuery('#clientside').on('click', function() {
        server = false;
        console.log("server is now false");
        jQuery("#dropdownSwitchEngine").children().removeClass('active');
        jQuery(this).addClass('active');
        jQuery("#dropdownMenuButton").text('Clientside (Python 2.7.10)');
        editor2.insert("\n========== Now Interpreting in Python 2.7.10 ==========\n");
    });
    jQuery('#butt').click(doIt);
    jQuery('#clear').click(clear);

    // fill in the dropdowns
    //<a class="dropdown-item active" id="clientside" data-toggle="button">Clientside</a>
    jQuery.getJSON('getScripts.php', function(data) {
        var ar = [];
        var paths = [];
        for (var i = 0; i < data.length; i++) {
            var text = data[i].split("/");
            var prog = "Aufgabe: " + text[text.length - 2].replace("sheet", "") + " " + text[text.length - 1].replace(".py", "");
            ar.push(prog);
            paths.push(text);
        }
        // ar.sort(function(a, b) { return a - b; });
        for (var i = 0; i < ar.length; i++) {
            var prog = ar[i];
            jQuery('#dropdownSwitchCode').append("<a class=\"dropdown-item\" data-toggle=\"button\" value=\"" + paths[i].join("/") + "\"> " + prog + "</a>");
        }
    });
    jQuery('#dropdownSwitchCode').on('click', 'a', function() {
        console.log("click on item " + jQuery(this).text());
        var p = jQuery(this).attr('value');
        jQuery.get(p, function(data) {
            editor.setValue(data);
        });
        jQuery('#sheetsdropdown').text(jQuery(this).text());
    });

    editor = ace.edit("program-code");
    //editor.setTheme("ace/theme/monokai");
    editor.setTheme("ace/theme/github");
    editor.session.setMode("ace/mode/python");
    editor.insert("# Add your python code here\n");

    editor2 = ace.edit("program-output");
    //editor.setTheme("ace/theme/monokai");
    editor2.setTheme("ace/theme/terminal");
    editor2.session.setMode("ace/mode/curly");
    editor2.setReadOnly(true);
    editor2.insert("# The output will appear here.\n");
    editor2.insert("========== Now Interpreting in Python 2.7.10 ==========\n");
});