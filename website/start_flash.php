
<?php
/*This is the code that is executed when the user sends a request to the web page. 
  if it doesn't contain the file to does nothing
  if the file exists it is going to open a file called "lengthPtr.txt" and writing a 0 to it. */
	if ($_SERVER['REQUEST_METHOD'] === 'POST')
	{
	  if( $_POST['flash'] == 'no_file')
	  {

	  }
	  else if ( $_POST['flash'] == 'ok')
	  {
	      /* Open the file */
	      $myfile = fopen("lengthPtr.txt","w");
	      fwrite($myfile,'0');
	      /* Close the file */
	      fclose($myfile);
	      $_POST['flash'] = 'done';
	      header ("Location: index.html");
	      //echo "start";
	  }

	}

  /* Getting all the files names in the uploads folder. */
  $files = glob('uploads/*'); 

/*This is the code that is executed when there is a file in the uploads folder. It is going to open
  the file lengthPtr.txt and read the first line of it. If the config is set to ok, it is going to
  return the first line of the file. If the config is set to none, it is going to return the last line
  of the file. If the config is set to doneBurn, it is going to delete the file and return DONE
  UPLOAD. If the config is set to allfile, it is going to return all the lines of the file. If the
  config is set to filelength, it is going to return the length of the file. If the config is not set,
  it is going to open the file lengthPtr.txt and write a 0 to it. */
  if (is_file($files[0]))
  {
      /* Getting the first file in the uploads folder and reading it into an array. */
      $path = $files[0];
      $mydata = file($path); //read file in array
      $length = count($mydata);

      /* Checking if the config is set. If it is set, it is going to open the file lengthPtr.txt and read the
      first line of it. */
      if ( isset( $_GET['config'] ) )
      {
        /* Opening a file called lengthPtr.txt and reading the first line of it. */
        $myfile = fopen("lengthPtr.txt","r");
        $ptr =  fgets($myfile);
        fclose($myfile);

/* This is the code that is executed when the config is set to ok. It is going to return the first line
of the file. */
        if (( $_GET['config'] == 'ok') && ($ptr < $length) && ($ptr >= 0))
        {
            echo $mydata[$ptr];
            $ptr++ ;
            $myfile = fopen("lengthPtr.txt","w");
            fwrite($myfile,$ptr);
            fclose($myfile);
            //header ("Location: test.php?config=none");
        }
        /* Returning the last line of the file. */
        elseif ( $_GET['config'] == 'none' && ($ptr < $length) && ($ptr >= 0))
        {
            //echo ($ptr-1);
            echo $mydata[$ptr-1];

        }
/* This is the code that is executed when the config is set to doneBurn. It is going to delete the file
and return DONE UPLOAD. */
        elseif (($ptr == $length) || ($_GET['config'] == 'doneBurn'))
        {
            echo "DONE UPLOAD ";
            /* Open the file */
            $myfile = fopen("lengthPtr.txt","w");
            fwrite($myfile,'-1');
            /* Close the file */
            fclose($myfile);

        /* Deleting the file after it is done uploading. */
            if(is_file($files[0]))
            {
              unlink($files[0]); // delete file
            }
	    			header ("Location: Finish.html");
        }
				elseif ( $_GET['config'] == 'allfile')
				{
					foreach($mydata as $line)
					{
						echo $line ."%";
					}
				}

      /* Returning the length of the file. */
				elseif ( $_GET['config'] == 'filelength')
				{
					echo $length ;
				}

      }
      /*  Checking if the config is set. If it is not set, it is going to open the file lengthPtr.txt and
          write a 0 to it. */
			else
			{
				// config Not set...
				$myfile = fopen("lengthPtr.txt","w");
				fwrite($myfile,'0');
				/* Close the file */
				fclose($myfile);
			}
  }
/* This is the code that is executed when there is no file in the uploads folder. */
  else
  {
      /* No files Found */
      if ( isset( $_GET['config'] ) )
      {
          if ($_GET['config'] == 'ok')
          {
              echo "NO FILE FOUND "."%";
          }
          elseif ( $_GET['config'] == 'none')
          {
              echo "NO FILE FOUND "."%";
          }
      }

  }


?>
