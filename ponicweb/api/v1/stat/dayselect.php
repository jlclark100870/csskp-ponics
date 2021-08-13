<?php


    //Load the file
 $contents = file_get_contents('get2.txt');
 
//Decode the JSON data into a PHP array.
 $val = json_decode($contents, true);

    
 $day = $val['last_stat']['day'];
$picture = $val['grow']['recipe']['tasks'][10]['picture']['file']['original'];
 $description = $val['grow']['recipe']['tasks'][10]['description'];


?>