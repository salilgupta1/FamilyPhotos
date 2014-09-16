var FileManager = (function($){
	var setFileInputAttr = function(){
		// accept multiple file upload
		$("#id_photos").attr("multiple",true);
		$("#id_photos").attr("accept","image/*");
	},
	previewImages = function(){
		// set up the images for preview before uploading
		$("#id_photos").change(function(event){
			$("#imagePreview").empty();
			// add loading gif here
			var input = $(event.currentTarget);
			var files = input[0].files;
			var reader;
			for(var i = 0;i<files.length;i++)
			{
				reader = new FileReader();
				reader.onload = function(e){
					var image = e.target.result;
					$("#imagePreview").append("<img class='photo' src='"+image+"'/>");
					$("#createAlbum").show();
				};
				reader.readAsDataURL(files[i]);
			}
		});
	},
	setUpIsotope = function(container){
		// set up Isotope
		container.isotope({
			itemSelector:'.photo',
			layoutMode:'cellsByRow',
			cellsByRow: {
				columnWidth: 150,
			}
		});
	},
	init = function(){
		setFileInputAttr();
		previewImages();
		setUpIsotope($("imagePreview"));
	};
	return {
		init:init,
	};
}(jQuery));