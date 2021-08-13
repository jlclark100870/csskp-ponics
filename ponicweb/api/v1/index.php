<?php

$strJsonFileContents = file_get_contents("machines/details.json");
$strrecipeFileContents = file_get_contents("json/get2.json");
$strrjsonFileContents = file_get_contents("json/r.json");

$val = json_decode($strJsonFileContents,TRUE);
$recipe = json_decode($strrecipeFileContents,TRUE);
$rjson = json_decode($strrjsonFileContents,TRUE);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
$openlock = $_POST['openlock'];
if ($openlock  == "true"){

  //$val['open_lock'] =

$rjson['open_lock'] = true;


}else{

  $rjson['open_lock'] = false;
}
$val1 = json_encode($rjson);
file_put_contents("json/r.json",$val1);
//$val = json_decode($strJsonFileContents,TRUE);
}

$day = $val['last_stat']['day'];
?>


<html>

<head>
    <meta http-equiv="refresh" content="30">
    <link rel="stylesheet" href="dashboard.css">
    <title>Grow Box DashBoard </title>
</head>

<body>


    
        <div class="header">
            Grow Box DashBoard<br>
            <div class="headersub"> 
            <?php

            echo "Last Updated";
            echo"<br>";
            print_r (urldecode($val['last_stat']['stat_time']));
            echo"<br>";
            echo"<br>";
            
            

            switch (true) {
              case $day >3 and $day <9:
               $task = 0;
                break;
              case $day >10 and $day <21:
                $task = 1;
                break;
              case $day >21 and $day <22:
                $task = 2;
                break;
                case $day >22 and $day <25:
                  $task = 4;
                  break;
                  case $day >25 and $day <27:
                    $task = 5;
                    break;
                    case $day >27 and $day <30:
                      $task = 6;
                      break;
              default:
                echo "Your favorite color is neither red, blue, nor green!";
            }
$title = $recipe['grow']['recipe']['tasks'][intval($task)]['title'];

$description = $recipe['grow']['recipe']['tasks'][intval($task)]['description'];
$picture = $recipe['grow']['recipe']['tasks'][intval($task)]['picture']['file']['original'];
$picturealt = $recipe['grow']['recipe']['tasks'][intval($task)]['picture']['name'];




?>
           
            <?php

            print_r($title);
            echo"<br>";
            
            print_r($description);
            
            echo "</br>";
            echo "</br>";
             echo "Grow Day";
              echo "</br>";
             echo $day;
            echo "</br>";
  
            ?>
            </div>
            </div>
       
<div class="flex-container">
            <div class="infobox">
                <?php
  echo "PH Level";
  echo "</br>";
  echo $val['last_stat']['ph'] ;
 
  ?>
            </div>
            <div class="infobox">
                <?php
  echo "Water Temp";
  echo "</br>";
  echo $val['last_stat']['water_temp'];
  
  
  ?>
            </div>
            <div class="infobox">
                <?php
                print_r("EC Level");
  
  print_r("<br>");
  print_r($val['last_stat']['ec']);
  
  ?>
            </div>
            <div class="status">
                <?php
  echo "Status";
  echo "</br>";
  echo $val['last_stat']['status'];
 
  ?>
            
        </div>
    </div>
    <?php


if ($rjson['open_lock'] == false){
echo'<form action="index.php" method="post">';
echo'<input type="hidden" id="openlock" name="openlock" value="true">';
echo'<input type="submit" value="Open lock">';
echo'</form>';
}else{
echo'<form action="index.php" method="post">';
echo'<input type="hidden" id="openlock" name="openlock" value="false">';
echo'<input type="submit" value="close lock">';
echo'</form>';
}
?>
<img src="<?echo $picture?>" alt="<?echo $picturealt?>" style="width:200px;">  


</body>

</html>