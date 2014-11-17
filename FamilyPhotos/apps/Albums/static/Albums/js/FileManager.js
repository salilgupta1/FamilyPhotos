var FileManager = (function($){
	var $imageContainer = $("#imagePreview"),
	setFileInputAttr = function(){
		// accept multiple file upload
		$("#id_photos").attr("multiple",true);
		$("#id_photos").attr("accept","image/*");
	},
	previewImages = function(){
		// set up the images for preview before uploading
		$("#id_photos").change(function(event){
			$imageContainer.empty();
			var input = $(event.currentTarget);
			var files = input[0].files;
			var reader;
			for(var i = 0;i<files.length;i++){
				reader = new FileReader();
				reader.onload = function(e){
					var image = e.target.result;
					$imageContainer.append("<div><img class='photo' src='"+image+"'/></div>");
				};
				reader.readAsDataURL(files[i]);
			}
		});
	},
	createAlbum = function(){
		$("createAlbum").click(function(e){
			$("#createAlbumForm").hide();
			$imageContainer.empty();
			$imageContainer.append("<img src='{% static 'img/loading.gif' %}'/>");
			e.preventDefault();
			e.unbind();
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
	};
	return {
		init:init,
		setUpIsotope:setUpIsotope,
		createAlbum:createAlbum,
	};
}(jQuery));