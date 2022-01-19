// Customising google sign in button
function onSuccess(googleUser) {
	console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
}
function onFailure(error) {
	console.log(error);
}
function renderButton() {
	gapi.signin2.render('my-signin2', {
		'scope': 'profile email',
		'width': 320,
		'font-size': 16,
		'height': 50,
		'longtitle': true,
		'theme': 'dark',
		'onsuccess': onSuccess,
		'onfailure': onFailure
	});
}

alerts = document.getElementsByClassName("close-alert");
for (let i of alerts){
	i.addEventListener("click", close_alert);
}
function close_alert(e){
	console.log(e.target.parentElement)
	e.target.parentElement.remove();
}

// Sign in page end
// Main Page Start
// Gallery viewer 
var images = document.querySelectorAll('#gallery .img-fluid');
var gallery = document.querySelector("#gallery")

for (let i of images) {
	i.addEventListener("click", view_image);
}

var clicked_image;

function view_image(e) {
	clicked_image = e.target;
	display_img(clicked_image);
}

function display_img(img) {
	document.body.style.overflowY = "hidden";
	let img_viewer = document.getElementById("image-viewer");
	img_viewer.style.display = "block"
	let file_name = img.src.split("images/")[1];
	let file_text = document.querySelector("#image-viewer p").childNodes[0];
	file_text.nodeValue = file_name;
	let desc = img.nextElementSibling.innerHTML;
	document.getElementById("img-desc").textContent = desc;
	document.getElementById("view_img").src = img.src;
}


function next_img() {
	if (clicked_image.parentNode.nextElementSibling !== null) {
		clicked_image = clicked_image.parentNode.nextElementSibling.firstElementChild;
		display_img(clicked_image);
	}
}

function prev_img() {
	if (clicked_image.parentNode.previousElementSibling !== null) {
		clicked_image = clicked_image.parentNode.previousElementSibling.firstElementChild;
		display_img(clicked_image);
	}
}

function img_back() {
	document.body.style.overflowY = "auto";
	document.getElementById("image-viewer").style.display = "none";
}


// Main Page End
	

// Start of Dashboard
let search = document.getElementById('srch-ppl');
let list = document.getElementById('ppl');
search.addEventListener('keyup', searchItem);
search.addEventListener('focus', searchItem);
function searchItem(e) {
	let seacrhValue = search.value.toLowerCase();
	let childItems = list.children;
	for (let child of childItems) {
		if (child.textContent.toLowerCase().indexOf(seacrhValue) === -1) {
			child.style.display = "none";
		} else {
			child.style.display = "block";
		}
	}
}

// End of find people section



// Start of ADD MEDIA section



// Start of ADD ARICLES section

// Brings the HTML set up for adding articles
function add_article() {
	let box = document.getElementById("add-article");
	box.classList.remove("recent-med");
	box.firstElementChild.classList.add("hide");
	box.classList.add("add-med-1");
	document.getElementById("med-artcl-btn").classList.add("hide");
	document.getElementById("add-med-artcl").classList.remove("hide");
}

// Goes back to recent section and cancels the articles
function cancel_article(e) {
	e.preventDefault();
	let yn = confirm("Are you sure you want to cancel? Your article won't be saved as draft.");
	if (yn) {
		let form = document.getElementById("form-article");
		form.classList.remove("was-validated");
		document.getElementById("artcl-heading").value="";
		document.getElementById("artcl").value="";
		let box = document.getElementById("add-article");
		box.classList.add("recent-med");
		box.firstElementChild.classList.remove("hide");
		box.classList.remove("add-med-1");
		document.getElementById("med-artcl-btn").classList.remove("hide");
		document.getElementById("add-med-artcl").classList.add("hide");
	}
}

// Submits the article
document.getElementById("form-article").addEventListener("submit", submit_article);
function submit_article(e) {
	e.preventDefault();
	if(is_validated2) {
		let form = document.getElementById("form-article");
		form.classList.remove("was-validated");
		// Getting the input
		let article_h = document.getElementById("artcl-heading").value;
		let article = document.getElementById("artcl").value;
		console.log(article_h);
		console.log(article);

		// Putting back to normal setup
		document.getElementById("artcl-heading").value="";
		document.getElementById("artcl").value="";
		let box = document.getElementById("add-article");
		box.classList.add("recent-med");
		box.firstElementChild.classList.remove("hide");
		box.classList.remove("add-med-1");
		document.getElementById("med-artcl-btn").classList.remove("hide");
		document.getElementById("add-med-artcl").classList.add("hide");

	}

}

// End of ADD ARTICLES section



// Start of ADD BOOK REVIEWS section

// Brings the HTML for adding book review.
function add_book_review() {
	let box = document.getElementById("add-book");
	box.classList.remove("recent-med");
	box.firstElementChild.classList.add("hide");
	box.classList.add("add-med-2");
	document.getElementById("med-book-btn").classList.add("hide");
	document.getElementById("add-med-book").classList.remove("hide");
}

// Goes back to recent section and cancels the book review
function cancel_book_review(e) {
	e.preventDefault();
	let yn = confirm("Are you sure you want to cancel? Your book review won't be saved as draft.");
	if (yn) {
		let form = document.getElementById("form-book");
		form.classList.remove("was-validated");
		document.getElementById("book_name").value="";
		document.getElementById("imageBook").value="";
		document.getElementById("review").value="";
		document.getElementById("bookShopUrl").value="";
		let box = document.getElementById("add-book");
		box.classList.add("recent-med");
		box.firstElementChild.classList.remove("hide");
		box.classList.remove("add-med-2");
		document.getElementById("med-book-btn").classList.remove("hide");
		document.getElementById("add-med-book").classList.add("hide");
	}
}


// Submits the book review
document.getElementById("form-book").addEventListener("submit", submit_book_review);
function submit_book_review(e) {
	e.preventDefault();
	if(is_validated2) {
		let form = document.getElementById("form-book");
		form.classList.remove("was-validated");
		// Getting the input
		let name = document.getElementById("book_name").value;
		let image = document.getElementById("imageBook").value;
		let review = document.getElementById("review").value;
		let url = document.getElementById("bookShopUrl").value;
		console.log(name);
		console.log(image);
		console.log(review);
		console.log(url);

		// Putting back to normal setup
		document.getElementById("book_name").value="";
		document.getElementById("imageBook").value="";
		document.getElementById("review").value="";
		document.getElementById("bookShopUrl").value="";
		let box = document.getElementById("add-book");
		box.classList.add("recent-med");
		box.firstElementChild.classList.remove("hide");
		box.classList.remove("add-med-2");
		document.getElementById("med-book-btn").classList.remove("hide");
		document.getElementById("add-med-book").classList.add("hide");

	}
}

// End of ADD BOOK REVIEWS section


// Start of ADD IMAGE section

// Brings the HTML for adding book review.
function add_image() {
	let box = document.getElementById("add-image");
	box.classList.remove("recent-med");
	box.firstElementChild.classList.add("hide");
	box.classList.add("add-med-3");
	document.getElementById("med-img-btn").classList.add("hide");
	document.getElementById("add-med-img").classList.remove("hide");
}

// Goes back to recent section and cancels the image.
function cancel_image(e) {
	e.preventDefault();
	let yn = confirm("Are you sure you want to cancel? Your image won't be saved as draft.");
	if (yn) {
		let form = document.getElementById("form-image");
		form.classList.remove("was-validated");
		document.getElementById("imageGallery").value="";
		document.getElementById("imgCaption").value="";
		let box = document.getElementById("add-image");
		box.classList.add("recent-med");
		box.firstElementChild.classList.remove("hide");
		box.classList.remove("add-med-3");
		document.getElementById("med-img-btn").classList.remove("hide");
		document.getElementById("add-med-img").classList.add("hide");
	}
}

// Submits the book review
document.getElementById("form-image").addEventListener("submit", submit_image);
function submit_image(e) {
	e.preventDefault();
	if(is_validated2) {
		let form = document.getElementById("form-image");
		form.classList.remove("was-validated");
		// Getting the input
		let image = document.getElementById("imageGallery").value;
		let caption = document.getElementById("imgCaption").value;
		console.log(image);
		console.log(caption);

		// Putting back to normal setup
		document.getElementById("imageGallery").value="";
		document.getElementById("imgCaption").value="";
		let box = document.getElementById("add-image");
		box.classList.add("recent-med");
		box.firstElementChild.classList.remove("hide");
		box.classList.remove("add-med-3");
		document.getElementById("med-img-btn").classList.remove("hide");
		document.getElementById("add-med-img").classList.add("hide");

	}
}

// End of ADD IMAGE section

// End of ADD MEDIA section



// Start of SETTINGS section

// Changes image 
function s_change_img(e) {
	let filePath = URL.createObjectURL(event.target.files[0]); 
	document.getElementById("profile-pic-img").src = filePath;
}


// Shows password
function s_show_pwd(e) {
	document.getElementById("pwd-visibility-show").classList.add("d-none");
	document.getElementById("s-pwd").type = "text";
	document.getElementById("pwd-visibility-hide").classList.remove("d-none");
}

// Hides password
function s_hide_pwd(e) {
	document.getElementById("pwd-visibility-hide").classList.add("d-none");
	document.getElementById("s-pwd").type = "password";
	document.getElementById("pwd-visibility-show").classList.remove("d-none");
}

var s_info_values = [];
// Changes to editing mode for profile info
function edit_profile_info(e) {
	e.preventDefault();
	document.getElementById("edit-info-btn").classList.add("d-none");
	document.getElementById("save-info-btn").classList.remove("d-none");
	document.getElementById("cancel-info-btn").classList.remove("d-none");

	let elem = document.querySelectorAll("#profile-info-form > .mb-3 > input, #profile-info-form > .mb-3 > textarea");
	for (let i of elem) {
		s_info_values.push(i.value);
		i.disabled = false;
	}

	document.getElementById("profile-info-form").addEventListener("submit", save_profile_info);
}

// Cancels the edit on profile info
function cancel_profile_info(e) {
	e.preventDefault();
	let yn = confirm("Are you sure you want to cancel? Your edits won't be saved!");
	if (yn) {
		document.getElementById("edit-info-btn").classList.remove("d-none");
		document.getElementById("save-info-btn").classList.add("d-none");
		document.getElementById("cancel-info-btn").classList.add("d-none");
		document.getElementById("profile-info-form").classList.remove("was-validated");

		let elem = document.querySelectorAll("#profile-info-form > .mb-3 > input, #profile-info-form > .mb-3 > textarea");
		let c = 0
		for (let i of elem) {
			i.value = s_info_values[c];
			i.disabled = true;
			c++;
		}
		s_info_values = [];
		document.getElementById("profile-info-form").removeEventListener("submit", save_profile_info);
	}
}


// Saves profile info changes 
function save_profile_info(e) {
	e.preventDefault();
	if (is_validated2) {
		document.getElementById("edit-info-btn").classList.remove("d-none");
		document.getElementById("save-info-btn").classList.add("d-none");
		document.getElementById("cancel-info-btn").classList.add("d-none");
		document.getElementById("profile-info-form").classList.remove("was-validated");

		let elem = document.querySelectorAll("#profile-info-form > .mb-3 > input, #profile-info-form > .mb-3 > textarea");
		for (let i of elem) {
			i.disabled = true;
		}

		s_info_values = [];			
		document.getElementById("profile-info-form").removeEventListener("submit", save_profile_info);
	}
}



var s_url_values = [];
// Changes to editing mode for social media links
function edit_urls(e) {
	e.preventDefault();
	document.getElementById("edit-urls-btn").classList.add("d-none");
	document.getElementById("save-urls-btn").classList.remove("d-none");
	document.getElementById("cancel-urls-btn").classList.remove("d-none");

	let elem = document.querySelectorAll("#urls-form > .mb-3 > input");
	for (let i of elem) {
		s_url_values.push(i.value);
		i.disabled = false;
	}

	document.getElementById("urls-form").addEventListener("submit", save_urls);
}

// Cancels the edit on social media urls
function cancel_urls(e) {
	e.preventDefault();
	let yn = confirm("Are you sure you want to cancel? Your edits won't be saved!");
	if (yn) {
		document.getElementById("edit-urls-btn").classList.remove("d-none");
		document.getElementById("save-urls-btn").classList.add("d-none");
		document.getElementById("cancel-urls-btn").classList.add("d-none");
		document.getElementById("urls-form").classList.remove("was-validated");

		let elem = document.querySelectorAll("#urls-form > .mb-3 > input");
		let c = 0;
		for (let i of elem) {
			i.value = s_url_values[c];
			i.disabled = true;
			c++;
		}

		s_url_values = [];
		document.getElementById("urls-form").removeEventListener("submit", save_urls);
	}
}

// Saves social media url changes 
function save_urls(e) {
	e.preventDefault();
	if (is_validated2) {
		document.getElementById("edit-urls-btn").classList.remove("d-none");
		document.getElementById("save-urls-btn").classList.add("d-none");
		document.getElementById("cancel-urls-btn").classList.add("d-none");
		document.getElementById("urls-form").classList.remove("was-validated");

		let elem = document.querySelectorAll("#urls-form > .mb-3 > input");
		for (let i of elem) {
			i.disabled = true;
		}

		s_url_values = [];			
		document.getElementById("urls-form").removeEventListener("submit", save_urls);
	}
} 

// End of SETTINGS section

// End of dashboard