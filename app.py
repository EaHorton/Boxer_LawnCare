from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
from flask import send_from_directory as flask_send_from_directory
import os

app = Flask(__name__, 
    static_url_path='/static',
    static_folder='static')
app.secret_key = 'your-secret-key-here'  # Required for flash messages
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for development

@app.route('/static/<path:filename>')
def serve_static(filename):
    try:
        print(f"Attempting to serve static file: {filename}")
        return flask_send_from_directory('static', filename)
    except Exception as e:
        print(f"Error serving static file {filename}: {str(e)}")
        return f"Error: {str(e)}", 404

def get_photos():
    photo_dir = "customer_photos"
    photos = []
    if os.path.exists(photo_dir):
        files = os.listdir(photo_dir)
        # First add all non-aeration photos
        for file in sorted(files):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')) and 'aeration' not in file.lower():
                photos.append(file)
        # Then add the aeration photo if it exists
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')) and 'aeration' in file.lower():
                photos.append(file)
    return photos

def get_testimonials():
    testimonials_dir = "customer_testimonials"
    testimonials = {
        'images': [],
        'texts': []
    }
    if os.path.exists(testimonials_dir):
        for file in os.listdir(testimonials_dir):
            file_path = os.path.join(testimonials_dir, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                testimonials['images'].append(file)
            elif file.lower().endswith('.txt'):
                with open(file_path, 'r') as f:
                    testimonials['texts'].append({
                        'title': file,
                        'content': f.read()
                    })
    return testimonials

def get_services():
    services_dir = "services"
    services = []
    if os.path.exists(services_dir):
        # Define the preferred order of services
        preferred_order = ['weed_control_fertilization.txt', 'core_aeration.txt']
        
        # First, get all service files
        service_files = os.listdir(services_dir)
        
        # Sort files according to preferred order
        sorted_files = sorted(service_files, 
                            key=lambda x: preferred_order.index(x) if x in preferred_order else len(preferred_order))
        
        for file in sorted_files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(services_dir, file)
                with open(file_path, 'r') as f:
                    content = f.read().strip()
                    # Split content into lines and remove the title
                    content_lines = content.split('\n')
                    # Skip the title and any blank lines after it
                    while content_lines and not content_lines[0].strip():
                        content_lines.pop(0)
                    if content_lines:  # Skip the title line
                        content_lines.pop(0)
                    while content_lines and not content_lines[0].strip():
                        content_lines.pop(0)
                    # Join the remaining content back together
                    content = '\n'.join(content_lines)
                    
                    # Add special formatting for titles
                    if 'weed_control_fertilization' in file.lower():
                        title = 'Weed Control & Fertilization'
                    elif 'core_aeration' in file.lower():
                        title = 'Core Aeration'
                    else:
                        title = file.replace('.txt', '').replace('_', ' ').title()
                    services.append({
                        'title': title,
                        'content': content
                    })
    return services

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    photos = get_photos()
    return render_template('gallery.html', photos=photos)

@app.route('/testimonials')
def testimonials():
    testimonials_data = get_testimonials()
    return render_template('testimonials.html', testimonials=testimonials_data)

@app.route('/services')
def services():
    services_data = get_services()
    return render_template('services.html', services=services_data)

@app.route('/customer_photos/<path:filename>')
def custom_static_photos(filename):
    return send_from_directory('customer_photos', filename)

@app.route('/customer_testimonials/<path:filename>')
def custom_static_testimonials(filename):
    return send_from_directory('customer_testimonials', filename)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        square_footage = request.form.get('square_footage')
        message = request.form.get('message')
        
        # Validate required fields
        if not all([name, email, phone, address]):
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('contact'))
        
        # Here you would typically handle the form submission
        # For example, send an email or save to a database
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)