$(document).ready(function(){
	

  	for(i=1900;i<=2020;i++){
  			$("#Xyear").append("<option value='"+i+"'>"+i+"</option>");
  			$("#X2year").append("<option value='"+i+"'>"+i+"</option>");
  			$("#UGyear").append("<option value='"+i+"'>"+i+"</option>");
  			$("#PGyear").append("<option value='"+i+"'>"+i+"</option>");
  	}
	for(i=1;i<=12;i++){
  			$("#M_duration,#mn_duration,#A_duration").append("<option value='"+i+"'>"+i+"</option>");
  			$("#A_size,#mn_size,#M_size").append("<option value='"+i+"'>"+i+"</option>");
  	}

	$.ajax({
	   			url:'/UG_courses/',
	   			type:'POST',
	   			data:{},
	   			success:function(result){	
				    if(result.success){
				        for(i=0;i<result.UG_courses.length;i++){
					$("#UGcourse").append("<option value='"+result.UG_courses[i]+"'>"+result.UG_courses[i]+"</option>");
				        }
				    }		
				}, 
	})
	$.ajax({
	   			url:'/PG_courses/',
	   			type:'POST',
	   			data:{},
	   			success:function(result){	
				    if(result.success){
				        for(i=0;i<result.PG_courses.length;i++){
					$("#PGcourse").append("<option value='"+result.PG_courses[i]+"'>"+result.PG_courses[i]+"</option>");
				        }
				    }		
				}, 
	})

	$.ajax({
	   			url:'/Universities/',
	   			type:'POST',
	   			data:{},
	   			success:function(result){	
				    if(result.success){
				        for(i=0;i<result.Universities.length;i++){
					$(".University").append("<option value='"+result.Universities[i]+"'>"+result.Universities[i]+"</option>");
				        }
				    }		
				}, 
	})


	$("#UGcourse").change(function() {

			UGcourse=$("#UGcourse").val();
			   $.ajax({
	   			url:'/UG_specialisations/',
	   			type:'POST',
	   			data:{'UGcourse':UGcourse},
	   			success:function(result){	
				    if(result.success){
					$("#UGspec").empty();
					$("#UGspec").append("<option value =''>-- Select --</option>");
				        for(i=0;i<result.UG_specialisations.length;i++){
					   $("#UGspec").append("<option value='"+result.UG_specialisations[i]+"'>"+result.UG_specialisations[i]+"</option>");
				        }
				    }		
				}, 
			    })		
	})
       $("#PGcourse").change(function() {
			PGcourse=$("#PGcourse").val();
			   $.ajax({
	   			url:'/PG_specialisations/',
	   			type:'POST',
	   			data:{'PGcourse':PGcourse},
	   			success:function(result){	
				    if(result.success){
					$("#PGspec").empty();
					$("#PGspec").append("<option value =''>-- Select --</option>");
				        for(i=0;i<result.PG_specialisations.length;i++){
					   $("#PGspec").append("<option value='"+result.PG_specialisations[i]+"'>"+result.PG_specialisations[i]+"</option>");
				        }
				    }		
				}, 
			    })		
	})
/**************** add certification ******************************/
		$("#certification_link").click(function(){
			var certification_id= $('#certification input').last().attr('id');
			c_id=parseInt(certification_id[certification_id.length-1])+1;
			c_name='Certification'+c_id
			$("#certification").append("<input type='text' class='form-control tb' name='"+c_name+"' id='"+c_name+"'/>");

		})



/**************** add    languages******************************/ 
		$("#other_lang").click(function(){
			var lang_id= $('#languages input').last().attr('id');
			l_id=parseInt(lang_id[4])+1;
			l_name='lang'+l_id
			$("#languages").append("<input type='text' class='form-control tb' name='"+l_name+"' id='"+l_name+"'/><br>");
		})
/**************** add   Achievements ******************************/ 
		$("#other_achievement").click(function(){
			var achievement_id= $('#achievement input').last().attr('id');
			a_id=parseInt(achievement_id[achievement_id.length-1])+1;
			a_name='achievement'+a_id
			$("#achievement").append("<input type='text' class='form-control tb' name='"+a_name+"' id='"+a_name+"'/><br>");

		})

/**************** add   Skills ******************************/ 
		$("#other_skill").click(function(){
			var Skill_id= $('#Skills input').last().attr('id');
			s_id=parseInt(Skill_id[Skill_id.length-1])+1;
			s_name='Skill'+s_id
			$("#Skills").append("<input type='text' class='form-control tb Skills '  name='"+s_name+"' id='"+s_name+"'  data-toggle='tooltip' title='Please enter only one IT Skill per box'/>");
			$(".Skills" ).autocomplete({
            			source: availableTags
        		})
		})


})
		
