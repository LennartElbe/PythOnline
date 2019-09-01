<?php

$text = "";
if (isset($_GET['code'])){
    $text = $_GET['code'];
}
file_put_contents('/tmp/code.py', $text);

// now run the code locally on a docker images (for example)
$output = array();
$ok = exec( 'docker run --rm -it -v /tmp/:/data python37 /bin/bash -c "/usr/bin/python3.7 /data/code.py"', $output);
//$ok = exec( 'docker run --rm -it -v /tmp/:/data 2b48ede56357 /bin/bash -c "/usr/bin/python3.7 /data/code.py"', $output);

echo(json_encode(array( "output" => $output )));
?>
