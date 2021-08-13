<?php
$strJsonFileContents = file_get_contents("details.json");

$string = explode( '&', $strJsonFileContents );

foreach( $string as $val ){
  $tmp = explode( '=', $val );
  $finalArray[ $tmp[0] ] = $tmp[1];
}


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
            <div class=headersub> 
            <?php
  
            print_r (urldecode($json->updated_at));
            echo "</br>";
            echo "</br>";
             echo "Grow Day";
              echo "</br>";
             echo $finalArray['day'];
            echo "</br>";
  
            ?>
            </div>
            </div>
       
<div class="flex-container">
            <div class="infobox">
                <?php
  echo "PH Level";
  echo "</br>";
  echo $finalArray['ph'];
  echo "</br>";
  ?>
            </div>
            <div class="infobox2">
                <?php
  echo "Water Temp";
  echo "</br>";
  echo $finalArray['water_temp'];
  echo "</br>";
  
  ?>
            </div>
            <div class="infobox3">
                <?php
                print_r("EC Level");
  
  print_r("<br>");
  print_r($finalArray['ec']);
  
  ?>
            </div>
            <div class="status">
                <?php
  echo "Status";
  echo "</br>";
  echo $finalArray['status'];
  echo "</br>";
  ?>
            
        </div>
    </div>
</body>

</html>