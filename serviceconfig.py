import yaml
import os
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "pacos_secret_key_12345" 

DEFAULT_PATH = '/mnt/seagate/seafileonlyoffice/homer_assets/config.yml'

def read_yaml_config(file_path):
    if not os.path.exists(file_path):
        return {"services": []}
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file) or {"services": []}

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

# --- ROUTE: HAUPTSEITE ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_path = request.form.get('config_path')
        if not os.path.exists(file_path):
            flash(f"Error: File not found ({file_path})", "error")
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

                flash(f"Success: '{service_name}' was added successfully!", "success")
                
            except Exception as e:
                flash(f"Error: {str(e)}", "error")
                
        return redirect(url_for('index', config_path=file_path))

    file_path = request.args.get('config_path', DEFAULT_PATH)
    config_data = read_yaml_config(file_path) if os.path.exists(file_path) else {"services": []}
    
    return render_template('index.html', default_path=file_path, config=config_data)

# --- ROUTE: DIENST VERSCHIEBEN ---
@app.route('/move', methods=['POST'])
def move_service():
    file_path = request.form.get('config_path')
    category_name = request.form.get('category_name')
    service_name = request.form.get('service_name')
    direction = request.form.get('direction')
    
    if os.path.exists(file_path):
        try:
            config = read_yaml_config(file_path)
            for category in config.get('services', []):
                if category.get('name') == category_name:
                    items = category.get('items', [])
                    
                    # Finde die Position (Index) des aktuellen Services
                    idx = next((i for i, item in enumerate(items) if item.get('name') == service_name), None)
                    
                    if idx is not None:
                        if direction == 'up' and idx > 0:
                            # Tausche mit dem Element darüber
                            items[idx - 1], items[idx] = items[idx], items[idx - 1]
                        elif direction == 'down' and idx < len(items) - 1:
                            # Tausche mit dem Element darunter
                            items[idx + 1], items[idx] = items[idx], items[idx + 1]
                            
                        write_yaml_config(file_path, config)
                        # flash(f"'{service_name}' wurde verschoben!", "success") # Optional: Auskommentiert, damit es nicht nervt
                    break
        except Exception as e:
            flash(f"Error beim Verschieben: {str(e)}", "error")
            
    return redirect(url_for('index', config_path=file_path))

# --- ROUTE: DIENST LÖSCHEN ---
@app.route('/delete', methods=['POST'])
def delete_service():
    file_path = request.form.get('config_path')
    category_name = request.form.get('category_name')
    service_name = request.form.get('service_name')
    
    if os.path.exists(file_path):
        try:
            config = read_yaml_config(file_path)
            for category in config.get('services', []):
                if category.get('name') == category_name:
                    category['items'] = [item for item in category.get('items', []) if item.get('name') != service_name]
                    if not category['items']:
                        config['services'].remove(category)
                    break
            write_yaml_config(file_path, config)
            flash(f"Success: '{service_name}' wurde gelöscht!", "success")
        except Exception as e:
            flash(f"Error beim Löschen: {str(e)}", "error")
            
    return redirect(url_for('index', config_path=file_path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)