var FileManager = (function($){
	var setFileInputAttr = function(){
		// accept multiple file upload
		$("#id_photos").attr("multiple",true);
		$("#id_photos").attr("accept","image/*");
	},
	previewImages = function(){
		// set up the images for preview before uploading
		$("#id_photos").change(function(event){
			// empty out div that held old images
			$("ul.rig").empty();
			$("#imagePreview").css("background-color","gray");
			$("#imagePreview").css("opacity","0.1");
			// get file input
			var input = $(event.currentTarget);
			var files = input[0].files;
			var reader = new FileReader();

			function readFile(index){
				// use recursions to read one file at a time

				var file = files[index];
				reader.onload = function(e){
					var image = e.target.result;
					$("ul.rig").append("<li><img  src='"+image+"'/></li>");
					
					// recur
					if(index+1 < files.length){
						readFile(index+1);
					}
					else{
						// base case
						$("#imagePreview").css("background-color","");
						$("#imagePreview").css("opacity","");
						return;
					}
				}
				reader.readAsDataURL(file);
			}
			readFile(0);	
			$("#createAlbum").show();
		});
	},
	init = function(){
		setFileInputAttr();
		previewImages();
	};
	return {
		init:init
	};
}(jQuery));