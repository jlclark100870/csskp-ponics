<?php
$strJsonFileContents = file_get_contents("api/v1/machines/details.json");
//echo $strJsonFileContents;
// Convert to array 
//print_r (explode(",",$strJsonFileContents));
//$strJsonFileContents = str_replace("+","_",$strJsonFileContents);
//$val= (explode(",",$strJsonFileContents));


$myArray = explode(',', $strJsonFileContents);
//print_r($myArray);
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
  
            print_r (urldecode($myArray[45])."  UTC");
            echo "</br>";
            echo "</br>";
             echo $myArray[38];
              echo "</br>";
             echo $myArray[39];
            echo "</br>";
  
            ?>
            </div>
            </div>
       
        <div class=dashbox>
            <div class="infobox">
                <?php
  echo $myArray[6];
  echo "</br>";
  echo $myArray[7];
  echo "</br>";
  ?>
            </div>
            <div class="infobox2">
                <?php
  echo $myArray[8];
  echo "</br>";
  echo $myArray[9];
  echo "</br>";
  
  ?>
            </div>
            <div class="infobox3">
                <?php
  print_r($myArray[10]);
  print_r("<br>");
  print_r($myArray[11]);
  
  ?>
            </div>
            <div class="status">
                <?php
  echo $myArray[42];
  echo "</br>";
  echo $myArray[43];
  echo "</br>";
  ?>
            
        </div>
    </div>
</body>

</html>