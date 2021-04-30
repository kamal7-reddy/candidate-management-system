function checkButton() {  
            if(document.getElementById('male').checked) { 
                return true;
            } 
            else if(document.getElementById('female').checked) { 
                return true;
            } 
            else if(document.getElementById('other').checked) { 
                return true; 
            }
            else { 
                document.getElementById("error").innerHTML 
                    = "Gender Not Selected";
                return false; 

            } 
        } 
