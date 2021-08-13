<?php
$json = file_get_contents('get2.txt', true);

var_dump(json_decode($json, true));

?>