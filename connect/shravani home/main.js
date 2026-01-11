$(document).ready(function() {
    // When the hamburger icon is clicked
    $('.fa-bars').click(function() {
        $(this).toggleClass('fa-times'); // Toggle 'fa-times' on the hamburger icon
        $('.navbar').toggleClass('nav-toggle'); // Toggle the navbar visibility
    });

    // Handle scroll event to change header styles
    $(window).on('scroll load', function() {
        // Reset icon and navbar on scroll/load
        $('.fa-bars').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        // Add/remove 'header-active' class based on scroll position
        if ($(window).scrollTop() > 30) {
            $('header').addClass('header-active');
        } else {
            $('header').removeClass('header-active');
        }

        // Loop through each section and check if it's in the viewport
        $('section').each(function() {
            var scrollTop = $(window).scrollTop(); // Current scroll position
            var offset = $(this).offset().top - 200; // The section's offset from the top
            var height = $(this).height(); // The section's height

            // Check if the section is in the viewport
            if (scrollTop >= offset && scrollTop < (offset + height)) {
                // Remove 'active' from all nav items
                $('.navbar ul li a').removeClass('active');

                // Add 'active' to the current nav item
                var id = $(this).attr('id');
                $('.navbar ul li a[href="#' + id + '"]').addClass('active');
            }
        });

        document.getElementById("contactForm").addEventListener("submit", function(event) {
            event.preventDefault(); 
        
            let name = document.getElementById("fullName").value;
            let email = document.getElementById("email").value;
            let phone = document.getElementById("phone").value;
            let message = document.getElementById("message").value;
        
            if (name && email && phone && message) {
                alert("Message Sent Successfully!");
                document.getElementById("contactForm").reset();
            } else {
                alert("Please fill out all fields.");
            }
            $(document).ready(function() {
                // Handle scroll event to show the login page
                $(window).on('scroll', function() {
                    var scrollPosition = $(window).scrollTop();
                    
                    // Show login page when scrolling past a certain point
                    if (scrollPosition > 500) {
                        $('#login.html').fadeIn();
                    } else {
                        $('#login.html').fadeOut();
                    }
                });
            
                // Show login page when the login button is clicked
                $('#loginButton').click(function() {
                    $('#login.html').fadeIn();
                });
            });
            
        });
    });

});