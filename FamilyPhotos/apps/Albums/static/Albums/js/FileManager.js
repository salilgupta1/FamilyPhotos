var FileManager = (function($){
	var setToMultipleFiles = function(){
		$("#id_photos").attr("multiple",true)
	},
	previewImages = function(){
		$("#id_photos").change(function(event){
			$(".imagePreview").empty();
			var input = $(event.currentTarget);
			var files = input[0].files;
			var reader;
			for(var i = 0;i<files.length;i++)
			{
				reader = new FileReader();
				reader.onload = function(e){
					image = e.target.result;
					$(".imagePreview").append("<img src='"+image+"'/>");
				};
				reader.readAsDataURL(files[i]);
			}
		});
	},
	init = function(){
		setToMultipleFiles();
		previewImages();
	};
	return {
		init:init,
	};
}(jQuery));