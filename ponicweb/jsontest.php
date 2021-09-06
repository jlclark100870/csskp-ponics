<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $EC = test_input($_POST["EC"]);
    $PH = test_input($_POST["PH"]);
    $phdosing = test_input($_POST["phdosing"]);
    $ecdosing = test_input($_POST["ecdosing"]);
    $daylength = test_input($_POST["daylength"]);
    $fan_temp_on = test_input($_POST["fan_temp_on"]);
    $fan_temp_off = test_input($_POST["fan_temp_off"]);
    $daycycle = test_input($_POST["daycycle"]);
    $ph_test_time = test_input($_POST["ph_test_time"]);

    $myObj->EC =(float) $EC;
    $myObj->PH =(float) $PH;
    $myObj->phdosing =(float) $phdosing;
    $myObj->ecdosing =(float) $ecdosing;
    $myObj->daylength= $daylength;
    $myObj->fan_temp_on=(int) $fan_temp_on;
    $myObj->fan_temp_off= (int)$fan_temp_off;
    $myObj->daycycle=$daycycle;
    $myObj->ph_test_time=(float)$ph_test_time;
  
    $myJSON = json_encode($myObj);
  
    $bytes = file_put_contents("api/v1/machines/setting.json", $myJSON); 
  
    echo $myJSON;
  
    }

        $strJsonFileContents = file_get_contents("api/v1/machines/setting.json");
        $array = json_decode($strJsonFileContents, true);
  


  function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
  }



  
  // Get the contents of the JSON file with php



?>
<!DOCTYPE html>
<html>
<head>
<meta>
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
<a href="index.php">Dash Board</a><br>
<form method="post" action="<?php echo htmlspecialchars($_SERVER[" PHP_SELF "]);?>">


<label for="EC">EC:</label><br>
<input type="text" id="EC" name="EC" value=<?echo($array[EC]);?>><br>


<label for="PH">PH:</label><br>
<input type="text" id="PH" name="PH" value=<?echo($array[PH]);?>><br>


<label for="phdosing">PH Dosing:</label><br>
<input type="text" id="phdosing" name="phdosing" value=<?echo($array[phdosing]);?>><br>

<label for="ecdosing">EC Dosing:</label><br>
<input type="text" id="ecdosing" name="ecdosing" value=<?echo($array[ecdosing]);?>><br>

<label for="fan_temp_on">fan_temp_on Celsius:</label><br>
<input type="text" id="fan_temp_on" name="fan_temp_on" value=<?echo($array[fan_temp_on]);?>><br>


<label for="fan_temp_off">fan_temp_off Celsius:</label><br>
<input type="text" id="fan_temp_off" name="fan_temp_off" value=<?echo($array[fan_temp_off]);?>><br>


<label for="daylength">day start:</label><br>
<input type="text" id="daylength" name="daylength" value=<?echo($array[daylength]);?>><br>


<label for="daylength">day end:</label><br>
<input type="text" id="daycycle" name="daycycle" value=<?echo(date($array[daycycle]));?>><br>


<label for="ph_test_time">ph_test_time:</label><br>
<input type="text" id="ph_test_time" name="ph_test_time" value=<?echo($array[ph_test_time]);?>><br>


<input type="submit" value="Submit">
</form>
<div class="row">
  <div class="column" <?php echo $style; ?> >This is div</div>
  <div class="column">PH Pump down</div>
  <div class="column">fan</div>
</div>
</body>
</html>