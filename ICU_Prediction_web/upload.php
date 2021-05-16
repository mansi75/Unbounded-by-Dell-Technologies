<?php
   $target_dir = "/home/harish/ICU_Prediction_Python/files/";
   $target_file = $target_dir.$_FILES["fileToUpload"]["name"];
   $file_name = $_FILES["fileToUpload"]["name"];
   $flag = 0;
   if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
       echo "File has been uploaded";
       $flag = 1; 
   }
   else{
       echo "File not yet uploaded";
       echo move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);
   }
   //echo $_FILES["fileToUpload"]["tmp_name"];
   if($flag == 1){
     $pyex = exec("/home/harish/pyopcv/bin/python3 /home/harish/ICU_Prediction_Python/covid.py '$file_name'");
     echo $pyex;
     echo "Inside if";
   }
   /*else{
       echo "Error in reading file"; 
   }*/
?>
