<?php
header('x-machine-update-time:'.date("m/d/y"));
$file = file_get_contents('../machine/details.json');
$myJson = explode('&',$file);
foreach( $myJson as $val ){
    $tmp = explode( '=', $val );
    $myJson[ $tmp[0] ] = $tmp[1];
  }

  $newjason['identifier'] = $myJson[identifier];
  $newjason['key'] = $myJson[key];
  $newjason['samplePeriod'] = $myJson[samplePeriod];
  $newjason['water_temp'] = $myJson[water_temp];
  $newjason['ph'] = $myJson[ph];
  $newjason['ec'] = $myJson[ec];
  $newjason['level'] = $myJson[level];
  $newjason['light_status'] = $myJson[light_status];
  $newjason['state_extract'] = $myJson[state_extract];
  $newjason['state_light'] = $myJson[state_light];
  $newjason['level_min_nw'] = $myJson[level_min_nw];
  $newjason['level_med_nw'] = $myJson[level_med_nw];
  $newjason['level_max_nw'] = $myJson[level_max_nw];
  $newjason['level_min_cw'] = $myJson[level_min_cw];
  $newjason['ec_cw'] = $myJson[ec_cw];
  $newjason['ec_goal'] = $myJson[ec_goal];
  $newjason['day'] = $myJson[day];
  $newjason['light_schedule'] = $myJson[light_schedule];
  $newjason['status'] = $myJson[status];
  $newjason['stat_time'] = $myJson[stat_time];
  $newjason['nutrient_1_level'] = $myJson[nutrient_1_level];
  $newjason['nutrient_2_level'] = $myJson[nutrient_2_level];
  $newjason['nutrient_3_level'] = $myJson[nutrient_3_level];
  $newjason['ph_pos_level'] = $myJson[ph_pos_level];
  $newjason['ph_neg_level'] = $myJson[ph_neg_level];
  $newjason['updated_at'] = $myJson[updated_at];
  $newjason['open_lock'] = $myJson[open_lock];
  $newjason['reset_fw'] = $myJson[reset_fw];


  //print_r( $finalArray );
//$myJson = json_encode($myJson, JSON_NUMERIC_CHECK);
//print_r($myJson);

$newjason = json_encode($newjason, JSON_NUMERIC_CHECK);


file_put_contents('../machine/get1.json', $newjason);





 ?>