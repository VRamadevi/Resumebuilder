$(document).ready(function(){
      var validate = $("#Projects_validate").validate({

        // Specify the validation rules
        rules: {   
	    M_title: "required",
	    M_duration: "required",
	    M_size:"required",
	    M_env:"required",
	    M_desc:"required",
	    Skill1:"required",


    	      
           
        },
        
        // Specify the validation error messages
        messages: {
	    M_title: "Please Enter Main Project Title",
            M_duration: "Please select duration of your Project",
	    M_size:"Please select the size of your Project",
	    M_env:"Plese enter the environment of your Project",
	    M_desc:"Please enter the description of your Project",
	    Skill1:"Please enter Skill"
	 
        },
        
        submitHandler: function(form) {
            form.submit();
        }
    });    
    $('#cancel').click(function(){
		validate.resetForm();
		$('#Projects_validate')[0].reset();

    });
})
