<?php



  /* Deleting all files in the uploads folder. */
    if(isset($_FILES['fileToUpload']))
    {
    	$files = glob('uploads/*'); // get all file names
    	foreach($files as $file)
    	{
        	// iterate files
    	  if(is_file($file))
          {
            unlink($file); // delete file
          }
    	}
    }

    /* Creating an array called errors. */
    $errors= array();
    /* Getting the name of the file. */
    $file_name = $_FILES['fileToUpload']['name'];
    /* Getting the size of the file. */
    $file_size = $_FILES['fileToUpload']['size'];
    /* Getting the temporary name of the file. */
    $file_tmp = $_FILES['fileToUpload']['tmp_name'];
    /* Getting the type of the file. */
    $file_type = $_FILES['fileToUpload']['type'];
    /* Getting the file extension. */
    $file_ext=strtolower(end(explode('.',$_FILES['fileToUpload']['name'])));

    /* Checking the file extension. */
    $expensions= array("hex");


  /* Checking if the file extension is not in the array. */
    if(in_array($file_ext,$expensions)=== false)
    {
      $errors[]="extension not allowed, please choose a HEX file.<br>";
    }

  /* Checking if the file size is greater than 500kb. */
    if($file_size > 500000)
    {
      $errors[]='File size must be excately 500kb';
    }

/*  Checking if there are any errors. If there are no errors, it will move the file to the uploads
    folder. It will then echo "Success" and echo "The file " + $fileName +  "  has been uploaded."
    if it has been uploaded.". It will then redirect the user to the done_upload.html page. 
    
    if there are any errors it will echo "Sorry, there was an error uploading your file."
    and then prints the error
    */
    if(empty($errors)==true)
    {
      move_uploaded_file($file_tmp,"uploads/".$file_name);
      echo "Success";
      echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";;

    header ("Location: done_upload.html" );
    }
    else
    {
      echo "Sorry, there was an error uploading your file.";
      echo "<br>";
      print_r($errors);
    /* Closing the if statement. */
    }
?>
