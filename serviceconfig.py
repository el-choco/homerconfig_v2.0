import yaml
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

DEFAULT_PATH = '/mnt/seagate/seafileonlyoffice/homer_assets/config.yml'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homer Config Manager</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #2b2b2b; color: #f8f8f2; padding: 20px; }
        .container { max-width: 600px; margin: auto; background: #3c3f41; padding: 30px; border-radius: 10px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); }
        h2 { margin-top: 0; color: #ffffff; text-align: center; margin-bottom: 25px; }
        label { font-weight: 600; margin-top: 15px; display: block; color: #a9b7c6; }
        input[type="text"], select { width: 100%; padding: 12px; margin: 8px 0 20px; box-sizing: border-box; background: #2b2b2b; color: #f8f8f2; border: 1px solid #555; border-radius: 6px; font-size: 14px; }
        input[type="text"]:focus, select:focus { border-color: #4caf50; outline: none; }
        
        .button-group { display: flex; gap: 15px; margin-top: 10px; }
        input[type="submit"], input[type="reset"] { flex: 1; padding: 14px 20px; border: none; cursor: pointer; border-radius: 6px; font-size: 16px; font-weight: bold; transition: background 0.3s ease; }
        
        input[type="submit"] { background: #4caf50; color: white; }
        input[type="submit"]:hover { background: #45a049; }
        
        input[type="reset"] { background: #555555; color: white; }
        input[type="reset"]:hover { background: #666666; }
        
        select optgroup { background: #3c3f41; color: #a9b7c6; font-weight: bold; }
        select option { background: #2b2b2b; color: #f8f8f2; padding: 8px; }
        
        .success { color: #4caf50; font-weight: bold; text-align: center; padding: 12px; background: rgba(76, 175, 80, 0.1); border-radius: 6px; margin-bottom: 20px; border: 1px solid rgba(76, 175, 80, 0.3); }
        .error { color: #f44336; font-weight: bold; text-align: center; padding: 12px; background: rgba(244, 67, 54, 0.1); border-radius: 6px; margin-bottom: 20px; border: 1px solid rgba(244, 67, 54, 0.3); }
    </style>
    <script>
        function checkCustomIcon() {
            var select = document.getElementById("icon_select");
            var customInput = document.getElementById("icon_custom");
            if (select.value === "custom") {
                customInput.style.display = "block";
                customInput.required = true;
            } else {
                customInput.style.display = "none";
                customInput.required = false;
            }
        }

        // Verhindert das erneute Senden beim Neuladen der Seite
        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
        }
    </script>
</head>
<body>
    <div class="container">
        <h2><i class="fas fa-tools"></i> Homer Config Manager</h2>
        
        {% if message %}
            <div class="{{ status }}">{{ message }}</div>
        {% endif %}
        
        <form method="POST">
            <label>Path to config.yml:</label>
            <input type="text" name="config_path" value="{{ default_path }}" required>

            <label>Category Name (e.g., System Administration):</label>
            <input type="text" name="category_name" required>

            <label>Category Icon:</label>
            <select name="category_icon_select" id="icon_select" onchange="checkCustomIcon()">
                <optgroup label="Infrastruktur & System">
                    <option value="fas fa-server">Server / Hosting (fas fa-server)</option>
                    <option value="fas fa-network-wired">Netzwerk / Proxy (fas fa-network-wired)</option>
                    <option value="fab fa-docker">Docker / Container (fab fa-docker)</option>
                    <option value="fas fa-microchip">Hardware / System (fas fa-microchip)</option>
                    <option value="fas fa-hdd">Speicher / Disks (fas fa-hdd)</option>
                </optgroup>
                <optgroup label="Cloud & Daten">
                    <option value="fas fa-cloud" selected>Cloud / Seafile / Nextcloud (fas fa-cloud)</option>
                    <option value="fas fa-folder-open">Dateien / Files (fas fa-folder-open)</option>
                    <option value="fas fa-database">Datenbanken (fas fa-database)</option>
                </optgroup>
                <optgroup label="Kommunikation & Office">
                    <option value="fas fa-envelope">Mail / SOGo (fas fa-envelope)</option>
                    <option value="fas fa-briefcase">Produktivität / Office (fas fa-briefcase)</option>
                    <option value="fas fa-comments">Chat / Messenger (fas fa-comments)</option>
                </optgroup>
                <optgroup label="Sicherheit & VPN">
                    <option value="fas fa-key">VPN / Wireguard / Keys (fas fa-key)</option>
                    <option value="fas fa-shield-alt">Sicherheit / Firewall (fas fa-shield-alt)</option>
                    <option value="fas fa-lock">Passwörter / Tresor (fas fa-lock)</option>
                </optgroup>
                <optgroup label="Medien">
                    <option value="fas fa-camera">Fotos / Immich (fas fa-camera)</option>
                    <option value="fas fa-film">Filme / Video (fas fa-film)</option>
                    <option value="fas fa-music">Audio / Musik (fas fa-music)</option>
                </optgroup>
                <optgroup label="Manuell">
                    <option value="custom">--- Eigenes Icon eingeben ---</option>
                </optgroup>
            </select>
            <input type="text" name="category_icon_custom" id="icon_custom" placeholder="z.B. fas fa-cat" style="display:none;">

            <label>Service Name:</label>
            <input type="text" name="service_name" required>

            <label>Logo Path (e.g., assets/tools/logo.png):</label>
            <input type="text" name="logo">

            <label>Subtitle:</label>
            <input type="text" name="subtitle">

            <label>Tag (e.g., Admin, Hauptsystem):</label>
            <input type="text" name="tag">

            <label>Service URL:</label>
            <input type="text" name="url" required>

            <div class="button-group">
                <input type="submit" value="Add Service">
                <input type="reset" value="Clear Form">
            </div>
        </form>
    </div>
</body>
</html>
"""

def read_yaml_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def write_yaml_config(file_path, config):
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml_str = yaml.dump(
            config,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=float("inf")
        )
        
        yaml_str = yaml_str.replace('\n  - name:', '\n\n  - name:').replace('\n    - name:', '\n\n    - name:')
        file.write(yaml_str)

def find_or_create_category(config, category_name, category_icon):
    clean_name = category_name.strip()
    
    for category in config.get('services', []):
        if category.get("name", "").strip().lower() == clean_name.lower():
            return category
            
    new_category = {"name": clean_name, "icon": category_icon, "items": []}
    
    if 'services' not in config:
        config['services'] = []
        
    config['services'].append(new_category)
    return new_category

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    status = ""
    
    if request.method == 'POST':
        file_path = request.form.get('config_path')
        
        if not os.path.exists(file_path):
            message = f"Error: File not found ({file_path})"
            status = "error"
        else:
            try:
                category_name = request.form.get('category_name')
                
                icon_select = request.form.get('category_icon_select')
                if icon_select == 'custom':
                    category_icon = request.form.get('category_icon_custom')
                else:
                    category_icon = icon_select
                    
                if not category_icon:
                    category_icon = "fas fa-cloud"
                
                service_name = request.form.get('service_name')
                logo = request.form.get('logo') or ""
                subtitle = request.form.get('subtitle') or ""
                tag = request.form.get('tag') or ""
                url = request.form.get('url')

                config = read_yaml_config(file_path)
                category = find_or_create_category(config, category_name, category_icon)

                new_service = {
                    "name": service_name,
                    "logo": logo,
                    "subtitle": subtitle,
                    "tag": tag,
                    "url": url,
                    "target": "_blank"
                }

                category['items'].append(new_service)
                write_yaml_config(file_path, config)

                message = f"Success: '{service_name}' was added successfully!"
                status = "success"
                
            except Exception as e:
                message = f"Error: {str(e)}"
                status = "error"

    return render_template_string(HTML_TEMPLATE, default_path=DEFAULT_PATH, message=message, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
