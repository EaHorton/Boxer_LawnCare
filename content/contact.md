---
title: Contact
type: contact
menu:
  main:
    weight: 5
---

<div class="row">
    <div class="col-md-6 mx-auto">
        <form name="contact" method="POST" data-netlify="true" action="/thank-you/" class="needs-validation" netlify-honeypot="bot-field" novalidate>
            <input type="hidden" name="form-name" value="contact">
            <p class="d-none">
                <label>Don't fill this out if you're human: <input name="bot-field" /></label>
            </p>
            <div class="mb-3">
                <label for="name" class="form-label">Name (required)</label>
                <input type="text" class="form-control" id="name" name="name" required>
                <div class="invalid-feedback">
                    Please provide your name.
                </div>
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">Phone Number (required)</label>
                <input type="tel" class="form-control" id="phone" name="phone" required>
                <div class="invalid-feedback">
                    Please provide a valid phone number.
                </div>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email (required)</label>
                <input type="email" class="form-control" id="email" name="email" required>
                <div class="invalid-feedback">
                    Please provide a valid email address.
                </div>
            </div>
            <div class="mb-3">
                <label for="address" class="form-label">Address (required)</label>
                <input type="text" class="form-control" id="address" name="address" required>
                <div class="invalid-feedback">
                    Please provide your address.
                </div>
            </div>
            <div class="mb-3">
                <label for="square_footage" class="form-label">Square Footage (A Basketball Court is 5k sqft)</label>
                <input type="number" class="form-control" id="square_footage" name="square_footage" 
                       placeholder="Enter approximate square footage">
                <small class="text-muted">Please provide an estimate of your lawn's square footage</small>
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" id="message" name="message" rows="5" 
                        placeholder="Additional details or questions..."></textarea>
            </div>
            <button type="submit" class="btn btn-primary custom-button">Send Message</button>
        </form>
    </div>
    <div class="col-md-6">
        <div class="contact-info-card">
            <div class="card h-100 shadow">
                <div class="card-body">
                    <h4 class="card-title mb-4" style="color: #8B0000;">Contact Information</h4>
                    <div class="d-flex align-items-center mb-3">
                        <i class="fas fa-phone me-3" style="color: #8B0000;"></i>
                        <p class="mb-0">Phone: (864) 501-3815</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <i class="fas fa-map-marker-alt me-3" style="color: #8B0000;"></i>
                        <p class="mb-0">Serving Upstate South Carolina</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();
</script>