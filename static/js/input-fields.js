document.addEventListener('DOMContentLoaded', function () {
    var inputs = document.querySelectorAll('.form-group input');

    inputs.forEach(function (input) {
        var placeholder = input.nextElementSibling;
        
        if (input.value !== '') {
            placeholder.classList.add('active');
        }
        
        input.addEventListener('focus', function () {
            placeholder.classList.add('active');
        });

        input.addEventListener('blur', function () {
            if (this.value === '') {
                placeholder.classList.remove('active');
            }
        });
    });
});
