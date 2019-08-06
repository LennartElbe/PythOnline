var editor; // for input
var editor2; // for output
var server;

function outf(text) {
    //var mypre = document.getElementById("program-output");
    // jQuery('#program-output').html(text);
    //jQuery('#program-output').setValue(text);
    editor2.setValue(editor2.getValue() + "\n" + text);
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
        editor2.setValue(editor2.getValue() + "\n" + data['output']);
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
    console.log("This line is printed after the page is loaded");
    jQuery('#serverside').click(function() {
        server = true;
        console.log("server is now true")
            // set the button to blue
    });
    jQuery('#clientside').click(function() {
        server = false;
        console.log("server is now false")
            // set button clientside to blue
    });
    jQuery('#butt').click(doIt);
    jQuery('#clear').click(clear);


    editor = ace.edit("program-code");
    //editor.setTheme("ace/theme/monokai");
    editor.setTheme("ace/theme/github");
    editor.session.setMode("ace/mode/python");
    editor.setValue("# Add your python code here\n");


    editor2 = ace.edit("program-output");
    //editor.setTheme("ace/theme/monokai");
    editor2.setTheme("ace/theme/terminal");
    editor2.session.setMode("ace/mode/curly");
    editor2.setValue("# The output will appear here\n");
});