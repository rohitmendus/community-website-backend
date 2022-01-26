// Start of Dashboard

$(document).ready(function(){
	$('#profile-info-form').submit(function(){
		var url = $('#profile-info-form').attr('action');
		var first_name = $('#s-first-name').val();
		var last_name = $('#s-last-name').val();
		var email = $('#s-email').val();
		var bio = $('#s-bio').val();
		$form = $(this)
        var formData = new FormData(this);
        formData.append('f_name', first_name);
        formData.append('l_name', last_name);
        formData.append('email', email);
        formData.append('bio', bio);
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            processData: false,
    		contentType: false,
        });
	});

	$('#urls-form').submit(function(){
		var url = $('#urls-form').attr('action');
		var twitter = $('#s-twitter').val();
		var facebook = $('#s-fb ').val();
		var instagram = $('#s-insta').val();
		var linkedin = $('#s-linkedin').val();
		$form = $(this)
        var formData = new FormData(this);
        formData.append('twitter', twitter);
        formData.append('facebook', facebook);
        formData.append('instagram', instagram);
        formData.append('linkedin', linkedin);
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            processData: false,
    		contentType: false,
        });
	});
});

// End of Dashboard