$(document).ready(function(){


      var validate = $("#Personal_validate").validate({

        // Specify the validation rules
        rules: {   
	    dob: {
		required: true,
		date:true

	    },
	    address: "required",
	    hobbies:"required",
	    profile_pic:{
    		required: true,
		/* accept:"image/*" */
           },

      
       
           
        },
        
        // Specify the validation error messages
        messages: {
	    dob: "Please Enter your Date Of Birth",
            address: "Please Enter Address",
	    hobbies:"Please enter Hobbies",
	    profile_pic:"Plese upload your profile pic",
	
        },
        
        submitHandler: function(form) {
            form.submit();
        }
    });   

    $('#cancel').click(function(){
		validate.resetForm();
		$('#Personal_validate')[0].reset();

    });
})
