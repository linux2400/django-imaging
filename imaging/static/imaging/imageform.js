(function($) {
	$('#id_avatar > li:gt(0)').hide();
	$('.inplaceeditform').show();
	$('#id_avatar select').prop('selectedIndex',0);
	$('#id_avatar select').change(function() {
		var idx = $('#id_avatar select').prop('selectedIndex');
		if(idx==0) {
			$('#id_avatar > li:gt(0)').hide();
		} else {
			$('#id_avatar > li:gt(0)').hide();
			$('#id_avatar > li').eq(idx).show();
		}
	});
	function getValue(form, field_id) {
		// return serialized form data
		form_data = form2js('id_avatar','.',false);
		form_data = form_data['avatar'];
		for (var n in form_data) {
			if(n != 'type' && n != $('#id_avatar select').val())
			{
				form_data[n] = '';
			} else if(n != 'type'){
				var dataArray = new Array;
				for(var o in form_data[n]) {
				    dataArray.push(form_data[n][o]);
				}
				form_data[n] = dataArray
			}
		} 
		var dataArray = new Array;
		for(var o in form_data) {
		    dataArray.push(form_data[o]);
		}
		return dataArray;	
	}
	$('.apply').data("getValue",getValue);
	
})(jQuery);