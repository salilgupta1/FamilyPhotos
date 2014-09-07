var FileManager = (function($){
	var setToMultipleFiles = function(){
		$("#id_photos").attr("multiple",true)
	},
	init = function(){
		setToMultipleFiles();
	};
	return {
		init:init,
	};
}(jQuery));