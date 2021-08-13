<?php

header("Content-Type: application/json; charset=UTF-8");
header('x-machine-update-time:'.date("m/d/y"));


$updated_at=$_POST['updated_at'];
$nutrient_1_level= $_POST['nutrient_1_level'];
$nutrient_2_level= $_POST['nutrient_2_level'];
$nutrient_3_level= $_POST['nutrient_3_level'];
$ph = $_POST['ph'];
$ec = $_POST['ec'];
$air_temp = $_POST['air_temp'];
$water_temp = $_POST['water_temp'];
$light_status=$_POST['light_status'];
$state_light=$_POST['state_light'];
$day=$_POST['day'];
$light_schedule=$_POST['light_schedule'];
$status = $_POST['status'];
$ec_cw = $_POST['ec_cw'];
$mac="64694e7e5f68";
$ph_pos_level =$_POST['ph_pos_level'];
$ph_neg_level =$_POST['ph_neg_level'];
$contents = file_get_contents('../json/r.json');
$val = json_decode($contents,TRUE);

//$val['open_lock']=false;
$val['last_stat']['status']=$status;
$val['last_stat']['ph']=$ph;
$val['last_stat']['ec_cw']=$ec_cw;
$val['last_stat']['ec']=$ec;
$val['last_stat']['water_temp']=$water_temp;
$val['last_stat']['light_status']=true;
$val['last_stat']['state_light']=$state_light;
$val['last_stat']['day']=$day;
$val['last_stat']['light_schedule']=$light_schedule;
$val['updated_at']=$updated_at;
$val['last_stat']['stat_time']=date(DATE_ATOM);
$val['last_stat']['nutrient_1_level'] = $nutrient_1_level;
$val['last_stat']['nutrient_2_level'] = $nutrient_2_level;
$val['last_stat']['nutrient_3_level'] = $nutrient_3_level;
$val['last_stat']['ph_pos_level']= $ph_pos_level;
$val['last_stat']['ph_neg_level']= $ph_neg_level;
$val['last_stat']['air_temp']= $air_temp;


$val1 = json_encode($val);



file_put_contents('../machines/details.json',$val1 );



?>