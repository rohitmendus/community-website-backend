// Start of Dashboard

$(document).ready(function(){
  try {
      if (tab == "register"){
          $('#register-tab').tab('show');
      }
  } catch(e){
      console.log()
  }

  $("#messsage-modal").modal('show');

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

  $('.like-form').submit(function(e){
    e.preventDefault()
    $(this).hide()
    if ($(this).attr('id') === "like1") {
      $('#like0').show()
      like_type = $('#like1 input[name="like"]').val()
    } else{
      $('#like1').show()
      like_type = $('#like0 input[name="like"]').val()
    }

    const url = $(this).attr('action')
    const csrf_token = $('#like1 input[name="csrfmiddlewaretoken"]').val()

    $.ajax({
        url: url,
        type: 'POST',
        data: {'like': like_type, 'csrfmiddlewaretoken': csrf_token},
        dataType: "json",
        success: function(response){
          $('#no-of-likes').text(response.no_of_likes)
          if (response.liked){
            $('#like0').show();
            $('#like1').hide();
          } else{
            $('#like1').show();
            $('#like0').hide();
          }
        },
    });
  });

  $('#comments button').click(function(){
    $('#comments-box').slideToggle(200);
    if ($(this).attr('id') == "comment-btn") {
      $(this).attr('id', 'comment-btn-open')
    } else {
      $(this).attr('id', 'comment-btn')
    }
  });

  $('#comment-cancel-btn').click(function(){
    $(this).closest('form').find("textarea").val("");
  })

  $('#comments-form form').submit(function(e) {
    e.preventDefault()
    const url = $(this).attr('action')
    const comment = $('#comment-text').val()
    const csrf_token = $('#comments-form form input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
      url: url,
      type: 'POST',
      data: {'comment': comment, 'csrfmiddlewaretoken': csrf_token},
      dataType: 'json',
      success: function(response){
        $("#no-of-comments").text(response.no_of_comments)
        $('#empty-comments').hide()
        $('#comments-form form textarea').val("")
        $('#comments-div>div').remove()
        for (let comment of response.comments) {
          if (comment.commenter_profile_pic.length !== 0) {
            var img = '<img src="'+media_folder+comment.commenter_profile_pic+'" alt="" class="rounded-circle" width="40" height="40">';
          } else {
            var img = '<img src="'+media_folder+'pics/profile.jpg" alt="" class="rounded-circle" width="40" height="40">';
          }
          let comment_div = $('<div class="comment mt-4 text-justify float-left">'+img+'<h5>'+comment.posted_by+'</h5><span>- '+comment.date_posted+'</span><br><p>'+comment.comment+'</p></div>');
          // posted_by = $('').text(comment.posted_by);
          // date = $('<span></span>').text("- "+comment.date_posted);
          // comment = $('<p></p>').text(comment.comment);
          // comment_div.append(img);
          // comment_div.append(posted_by);
          // comment_div.append(date);
          // comment_div.append($('<br>'));
          // comment_div.append(comment);
          $('#comments-div').append(comment_div);
        }
      }
    });
    
  });

  var carousels = $('#carouselExampleControls, #carouselCRUD-Images')

  for (let multipleCardCarousel of carousels) {
    if (window.matchMedia("(min-width: 768px)").matches) {
      var carousel = new bootstrap.Carousel(multipleCardCarousel, {
        interval: false,
      });
      var carouselWidth = $("#friend-requests .carousel-inner")[0].scrollWidth;
      var cardWidth = $("#friend-requests .carousel-item").width();
      var scrollPosition = 0;
      $("#carouselExampleControls .carousel-control-next").on("click", function () {
        if (scrollPosition < carouselWidth - cardWidth * 4) {
          scrollPosition += cardWidth;
          $("#carouselExampleControls .carousel-inner").animate(
            { scrollLeft: scrollPosition },
            600
          );
        }
      });
      $("#carouselExampleControls .carousel-control-prev").on("click", function () {
        if (scrollPosition > 0) {
          scrollPosition -= cardWidth;
          $("#carouselExampleControls .carousel-inner").animate(
            { scrollLeft: scrollPosition },
            600
          );
        }
      });
    } else {
      $(multipleCardCarousel).addClass("slide");
    }
  }
  // var multipleCardCarousel = document.querySelector(
  //   "#carouselExampleControls"
  // );
});

// End of Dashboard