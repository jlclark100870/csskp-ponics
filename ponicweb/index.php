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
<meta http-equiv="refresh" content="10">
<style>
body {
  background-color: lightblue;
}

h1 {
  color: white;
  text-align: center;
}
a {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 40px;
}
.column {
  background-color: blue;
  float: left;
  width: 33.33%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
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



</p>
<?php
        if(array_key_exists('button1', $_POST)) {
            button1();
        }
        else if(array_key_exists('button2', $_POST)) {
            button2();
        }
        function button1() {
            echo "This is Button1 that is selected";
        }
        function button2() {
            echo "This is Button2 that is selected";
        }
    ?>
  
    <form method="post">
        <input type="submit" name="button1"
                class="button" value="PH UP" />
          
        <input type="submit" name="button2"
                class="button" value="PH DOWN" />
    </form>
<div class="row">
  <div class="column" <?php echo $style; ?> >This is div</div>
  <div class="column">PH Pump down</div>
  <div class="column">fan</div>
</div>
<img src="uploads/name.jpg" alt="hydroponic plant" width="500" height="600">
</body>
</html>
