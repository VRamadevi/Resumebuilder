$(document).ready(function(){
      var validate = $("#Education_validate").validate({

        // Specify the validation rules
        rules: {   
	    Xboard: "required",
	    Xschool: "required",
	    Xyear:"required",
	    Xmarks:{
                required: true,
		digits:true,
		maxlength:2,
		minlength:2
	    },
	   Xcertificate:{
    		required: true,
		/* accept:"image/*" */
           },
	    X2board: "required",
	    X2school: "required",
	    X2year:"required",
	    X2marks:{
                required: true,
		digits:true,
		maxlength:2,
		minlength:2
	    },
	   X2certificate:{
    		required: true,
           },
	   UGcourse: "required",
	   UGspec: "required",
	   UGuniv: "required",
	   UGyear:"required",
	   UGmarks:{
                required: true,
		digits:true,
		maxlength:2,
		minlength:2
	    },
	   UGcertf:{
    		required: true,
           },
	   Certification1:"required"	
      
       
           
        },
        
        // Specify the validation error messages
        messages: {
	    Xboard: "Please select X board",
            Xschool: "Please select X school",
	    Xyear:"Please select the year",
	    Xmarks:"Plese enter your X marks in percentage only",
	    Xcertificate:"Please upload your  X ceertificate",
	    X2board: "Please select Intermediate board",
            X2school: "Please select Intermediate school",
	    X2year:"Please select the year",
	    X2marks:"Plese enter your Intermediate marks in percentage only",
	    X2certificate:"Please upload your Intermediate ceertificate ",
	    UGcourse:"Please select your UG course",
	    UGspec:"Please select your UG  specialistion",
	    UGuniv:"Please select your UG  University",
	    UGyear:"Please select the year"	,
   	    UGmarks:"Plese enter your UG marks in percentage only",
	    UGcertf:"Please upload your UG ceertificate ",
            Certification1:"Please Enter any one Certification Course"
        },

        submitHandler: function(form) {
            form.submit();
        }
    });    
    $('#cancel').click(function(){
		validate.resetForm();
		$('#Education_validate')[0].reset();

    });
})
