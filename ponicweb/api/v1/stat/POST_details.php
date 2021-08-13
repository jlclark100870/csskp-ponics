<?php
header('x-machine-update-time:'.date("m/d/y"));



//if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // collect value of input field
  
  
  foreach( $_POST as $stuff => $val ) {
    if( is_array( $stuff ) ) {
        foreach( $stuff as $thing) {
          file_put_contents('details.json', $stuff."=>".$val.",");
        }
    } else {
      file_put_contents('details.json', "did not work");
    }
}
//}
?>


 