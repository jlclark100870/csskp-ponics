<?php 
//Load the file
$contents = file_get_contents('details.json');
 
//Decode the JSON data into a PHP array.
$contentsDecoded = json_decode($contents,TRUE);
 

print_r($contentsDecoded);
?>