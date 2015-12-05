$(document).ready(function(){
      var validate = $("#Contact_validate").validate({

        // Specify the validation rules
        rules: {            
            Email: {
                required: true,
                email: true
		
            },
	    Mobile:{
                required: true,
		digits:true,
		maxlength:10,
		minlength:10,
	    },
            Name: {
		required:true,
		lettersonly: true


	    },
	    Headline: "required",
           
        },
        
        // Specify the validation error messages
        messages: {
	    Email: "Please enter a valid email address",
            Mobile: "Please Enter 10 digits valid Mobile Number",
            Name: "Please enter your  Name",
            Headline: "Please enter your Resume Headline",
        },
        
        submitHandler: function(form) {
            form.submit();
        }
    });    

jQuery.validator.addMethod("lettersonly", function(value, element) 
{
return this.optional(element) || /^[a-z," ","."]+$/i.test(value);
}, "Letters and spaces only please"); 


   $('#cancel').click(function(){
		validate.resetForm();
		$('#Contact_validate')[0].reset();

    });

})
function Email_info(){
var Email=$("input[name=Email]").val();
	$.ajax({
	   			url:'/Email_info/',
	   			type:'POST',
	   			data:{'Email':Email},
	   			success:function(result){
				    if(result.success){
				       $("input[name=Mobile]").val(result.Phone)
				       $("input[name=Name]").val(result.Name)
				       $("#Headline").val(result.Headline)
					
				    }		
				}, 
	})

 }
