$(document).ready(function(){
    $('#registrationForm').submit(function(event){
        event.preventDefault(); // Prevent form submission

        // Gather form data
        var formData = {
            'firstName': $('#firstName').val(),
            'lastName': $('#lastName').val(),
            'fatherName': $('#fatherName').val(),
            'class': $('#class').val(),
            'dob': $('#dob').val(),
            'phoneNumber': $('#phoneNumber').val(),
            'ids': $('#ids').val()
        };

        // AJAX request to submit form data to backend
        $.ajax({
            type: 'POST',
            url: '/submit_registration', // Correct endpoint URL
            data: JSON.stringify(formData),
            contentType: 'application/json',
            success: function(response) {
                // Show registration result
                $('#registrationResult').removeClass('d-none');
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
                // Handle error
            }
        });
    });
});
