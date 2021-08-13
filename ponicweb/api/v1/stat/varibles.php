<?php


    //Load the file
 $contents = file_get_contents('r.json');
 
//Decode the JSON data into a PHP array.
 $val = json_decode($contents, true);




$recipe_name = $val['grow']['recipe_name'];
$version = $val['version'];
$firmware_version = $val['firmware_version'];   
$for_testing = $val['for_testing'] ;
$calibrating_sensor =$val['calibrating_sensor'];
$water_tank_size=$val['water_tank_size'];
$day = $val['last_stat']['day'];
$picture = $val['grow']['recipe']['tasks'][10]['picture']['file']['original'];
$description = $val['grow']['recipe']['tasks'][10]['description'];
$updated_at = $val['updated_at'];
$open_lock = $val['open_lock'];
$reset_fw = $val['reset_fw'];
$started_at =$val['grow']['started_at'];




?>