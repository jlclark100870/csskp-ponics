<?php
header('x-machine-update-time:'.date("m/d/y"));
$file = file_get_contents('php://input');

//$data = json_encode($file);

file_put_contents('details.json', $file);





 ?>