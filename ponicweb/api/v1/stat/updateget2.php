<?php

header('x-machine-update-time:'.date("m/d/y"));
include("varibles.php"); 
//$file = file_get_contents('php://input');
$myobj = "";

foreach($val as $key => $val) {

    if (is_numeric($val)){
    
    $myjson ='"'.$key.'":'.$val.',';
}
    else
    {
        $myjson ='"'.$key.'":"'.$val.'",';

    }
    
    $myobj = $myobj.$myjson;
    

}
//$myobj = substr_replace($myobj ,"",-1);
//$grow = '"updated_at":"'.$updated_at.'","open_lock":'.true.',"reset_fw":'.false.',"started_at":"'.$started_at.'"';
//$myobj = $myobj.$grow;
//$myobj=json_decode($myobj,true);

/*
$myJSON = json_encode($myobj, JSON_NUMERIC_CHECK);
file_put_contents('../machine/details.json', $myJSON,FILE_APPEND );
*/
//file_put_contents('../machine/details.json',"{". $myobj ."}");

//echo '{ "success": true }';
print_r($val); 
?>