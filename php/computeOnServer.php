<?php

// We want to create a python file with the content from the current
// call. Lets create a temporary directory to store that python file.
// After we run the file we delete the directory again. We only return
// the output of the python run.

function tempdir() {
    $tempfile=tempnam(sys_get_temp_dir(),'');
    // you might want to reconsider this line when using this snippet.
    // it "could" clash with an existing directory and this line will
    // try to delete the existing one. Handle with caution.
    if (file_exists($tempfile)) { unlink($tempfile); }
    mkdir($tempfile);
    if (is_dir($tempfile)) { 
        return $tempfile; 
    }
}

$tmpdir = tempdir();

$text = "";
if (isset($_POST['code'])) {
    // The text from the user is not evaluted, only stored in a text file
    // for python.
    $text = $_POST['code'];
}
file_put_contents($tmpdir . '/test_code.py', $text);

// now run the code locally on a docker images (for example)
$output = array();
$outputtest = array();

// custom image
//$ok = exec( 'docker run --rm -it -v /tmp/:/data python37 /bin/bash -c "/usr/bin/python3.7 /data/code.py"', $output);
// php image
// We run a docker per script evaluation and throw away the folder alterwards.
$ok = exec( 'docker run --rm -it -v '.$tmpdir.':/data python37test /bin/bash -c "TERM=dumb /usr/local/bin/pytest -v /data/test_code.py"', $outputtest);
$ok = exec( 'docker run --rm -it -v '.$tmpdir.':/data python37test /bin/bash -c "/usr/bin/python3 /data/test_code.py"', $output);

echo(json_encode(array( "output" => $output, "outputtest" => $outputtest )));

// delete the folder again (and all files inside)
function delTree($dir) { 
   $files = array_diff(scandir($dir), array('.','..')); 
    foreach ($files as $file) { 
      (is_dir("$dir/$file")) ? delTree("$dir/$file") : unlink("$dir/$file"); 
    } 
    return rmdir($dir); 
}

// only delete the temporary directory (server script, should be secure)
delTree($tmpdir);

?>
