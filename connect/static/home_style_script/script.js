// $(document).ready(function(){

// 	$('.fa-bars').click(function(){
// 		$(this).toggleClass('fa-times'); // shows "x" of humberger icon
// 		$('.navbar').toggleClass('nav-toggle'); // opens the navabar 
// 	});


// 	// detecting scroll and page load events 

// 	 $(window).on('scroll load',function(){   // when the page loads or  user scroll run the function 
// 	 	$('.fa-bars').removeClass('fa-times');
// 	 	$('.navbar').removeClass('nav-toggle');
         
//          // making the header active on scroll 

// 	 	if($(window).scrollTop() > 30)  
// 	 	{
// 	 		$('header').addClass('header-active');
// 	 	}
// 	 	else{
// 	 		$('header').removeClass('header-active');
// 	 	}


//              // highlighting the active section in teh navbar
// 				    $('section').each(function () {
// 				        var scrollTop = $(window).scrollTop();  // Current scroll position
// 				        console.log("current scroll position ",scrollTop);
// 				        var id = $(this).attr('id');  // retrives id of current section 
// 				        console.log("current id  is ",id);
// 				        var height = $(this).height();  // get the height of Section
// 				        console.log("height of current section",height)
// 				        var offset = $(this).offset().top - 1300;  // Position of section from top, adjusted for better visibility
// 				        console.log("position of ",scrollTop ," from top is", offset);
// 				        // Check if the section is in the viewport
// 				        if ( (scrollTop >= offset) && (scrollTop < height + offset )) {
// 				            $('.navbar ul li a').removeClass('active');  // Remove active class from all links
// 				            $('.navbar').find('[href="#' + id + '"]').addClass('active');  // Add active class to the matching link
// 				        }
// 				    });
				











// 	 });
// });














$(document).ready(function () {

	console.log("jquery loaded");


    $('.fa-bars').click(function () {
    	console.log("fabars clicked");
        $(this).toggleClass('fa-times'); // Show "X" on clicking
        $('.navbar').toggleClass('nav-toggle'); // Toggle navbar visibility
    });

    // Detect scroll and page load events
    $(window).on('scroll load', function () {
        $('.fa-bars').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        // Add active class to header when scrolling past 30px
        if ($(window).scrollTop() > 30) {
            $('header').addClass('header-active');
        } else {
            $('header').removeClass('header-active');
        }

        // Highlight the active section in the navbar
        $('section').each(function () {
            var scrollTop = $(window).scrollTop(); // Current scroll position
            var id = $(this).attr('id'); // Get section ID
            var height = $(this).outerHeight(); // Get full height of section
            var offset = $(this).offset().top - 150; // Adjust for navbar height

            // Check if the section is in the viewport
            if (scrollTop >= offset && scrollTop < offset + height) {
                $('.navbar ul li a').removeClass('active'); // Remove active from all links
                $('.navbar').find('[href="#' + id + '"]').addClass('active'); // Highlight the correct link
            }
        });
    });
});