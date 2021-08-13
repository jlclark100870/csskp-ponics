<?php
 include("varibles.php"); 

//Modify the counter variable.
//$contentsDecoded['for_testing']=false;


?>

<!DOCTYPE html>
<html>
<head>
<title>Grow Box</title>
</head>
<body>
<h1>Grow Box</h1>
<img src="<?print_r($picture);?> ); ?>"><br>

<?print_r( $description); ?>

</body>
</html>
<?php
print_r($val['open_lock']);
print_r($val['updated_at']);
//Encode the array back into a JSON string.
$json = json_encode($var);
 
//Save the file.
//file_put_contents('get2.txt', $json);
//print_r($json)

?>