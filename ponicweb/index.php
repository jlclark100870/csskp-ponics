<?php
// Get the contents of the JSON file 
$strJsonFileContents = file_get_contents("api/v1/machines/details.json");
// Convert to array 
$array = json_decode($strJsonFileContents, true);
date_default_timezone_set("America/Chicago");
?>
<!DOCTYPE html>
<html>
<head>

<meta http-equiv=“Expires” content=”-1″>

<meta http-equiv="refresh" content="10">
<style>
body { background-color:#555888; font-family:sans-serif; color:#fff; font-size:30px; text-align:center }
code { display:inline-block; max-width:600px;  padding:80px 0 0; line-height:1.5; font-family:monospace; color:#ccc }

.sc-gauge  { width:200px; height:200px; margin:200px auto; }
.sc-background { position:relative; height:100px; margin-bottom:10px; background-color:#fff; border-radius:150px 150px 0 0; overflow:hidden; text-align:center; }
.sc-mask { position:absolute; top:20px; right:20px; left:20px; height:80px; background-color:#555888; border-radius:150px 150px 0 0 }
.sc-percentage { position:absolute; top:100px; left:-200%; width:400%; height:400%; margin-left:100px; background-color:#00aeef; }
.sc-percentage { transform:rotate(158deg); transform-origin:top center; }
.sc-min { float:left; }
.sc-max { float:right; }
.sc-value { position:absolute; top:50%; left:0; width:100%;  font-size:48px; font-weight:700 }


/* css for ph gauge */

.sc-gaugeph  { width:200px; height:200px; margin:200px auto; }
.sc-maskph { position:absolute; top:20px; right:20px; left:20px; height:80px; background-color:#555888; border-radius:150px 150px 0 0 }

.sc-percentageph { position:absolute; top:100px; left:-200%; width:400%; height:400%; margin-left:100px; background-color:#00aeef; }
.sc-percentageph { transform:rotate(90deg); transform-origin:top center; }




/*end ph values*/

/* css for ph gauge */

.sc-gaugeph  { width:200px; height:200px; margin:200px auto; }
.sc-maskph { position:absolute; top:20px; right:20px; left:20px; height:80px; background-color:#555888; border-radius:150px 150px 0 0 }

.sc-percentageph { position:absolute; top:100px; left:-200%; width:400%; height:400%; margin-left:100px; background-color:#00aeef; }
.sc-percentageph { transform:rotate(90deg); transform-origin:top center; }


.rotateimg180 {
  -webkit-transform:rotate(180deg);
  -moz-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  -o-transform: rotate(180deg);
  transform: rotate(180deg);
}

/*end ph values*/


</style>
</head>
<body>
<h1>Porch Conditions page</h1>
<a href="jsontest.php">settings</a><br>
<p>

<?php

$timestamp = $array[time];

$water = ($array[water_temp]*1.8)+32;
$air = ($array[air_temp]*1.8)+32;

echo("Time: ");
echo(date('d M Y H:i:s',$timestamp));
echo("</br>");
echo("humidity: ");
echo($array[humidity]);
echo("</br>");
echo("Air Temp: ");
echo($air);
echo("</br>");
echo("Light Sensor: ");
echo($array[lightSensor]);
echo("</br>");
echo("Water Temp: ");
echo($water);
echo("</br>");
echo("PH: ");
echo($array[PH]);
echo("</br>");
echo("EC: ");
echo($array[EC]);
echo("</br>");
echo("grow light status :");

echo($array[grow_light]);


?>
<!--
<div class="sc-gauge">
water tempature
    <div class="sc-background">
      <div class="sc-percentage"></div>
      <div class="sc-mask"></div>
      <span class="sc-value"><?echo($water)?></span>
    </div>
    <span class="sc-min">0</span>
    <span class="sc-max">120</span>
</div>
<div class="sc-gauge">
air tempature
    <div class="sc-background">
      <div class="sc-percentage"></div>
      <div class="sc-mask"></div>
      <span class="sc-value"><?echo($air)?></span>
    </div>
    <span class="sc-min">0</span>
    <span class="sc-max">120</span>
</div>
<div class="sc-gauge">
EC
    <div class="sc-background">
      <div class="sc-percentage"></div>
      <div class="sc-mask"></div>
      <span class="sc-value"><?echo($array[EC]);?></span>
    </div>
    <span class="sc-min">0</span>
    <span class="sc-max">120</span>
</div>
<div class="sc-gaugeph">
PH
    <div class="sc-background">
      <div class="sc-percentageph"></div>
      <div class="sc-maskph"></div>
      <span class="sc-value"><?echo($array[PH]);?></span>
    </div>
    <span class="sc-min">0</span>
    <span class="sc-max">14</span>
</div>
-->
</p>


  
   
<img src="uploads/name.jpg" alt="hydroponic plant" width="300" height="300" class="rotateimg180">
</body>
</html>
