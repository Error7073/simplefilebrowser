from flask import Flask, request, jsonify, send_file
import requests
import os

app = Flask(__name__)

def format_url(path: str):
    return f"Files/{path}"

def display_files(directory: str, base_path=""):
    curr_page = ""
    for index, file in enumerate(os.listdir(directory)):
        file_path = f"{base_path}/{file}" if base_path else file
        curr_page += f'''
            <h1>{index} - <a href="/Files/{file_path}">{file}</a></h1>
        '''
    return curr_page

    

@app.route("/", methods=["GET"])
def start_page():
    return display_files("/")

@app.route("/Files/<path:filename>", methods=["GET"])
def serve(filename):
    full_path = os.path.join("Files", filename)
    print(full_path)
    
    if os.path.isdir(full_path):
        return display_files(full_path, filename)
    else:
        return send_file(full_path)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
