from flask import Flask, send_file, request, Response, redirect, render_template, session
app = Flask(__name__)
import os
import re  # Import the re module for regular expressions
import json
from datetime import timedelta

app.secret_key = "lucario"
app.permanent_session_lifetime = timedelta(minutes=200)

def get_password():
    if os.path.isfile(fname)

def movies_info(file):
    with open(file+".json", 'r') as f:
        data = json.load(f)
    return data

def is_auth():
    if "authenticated" in session:
        return True
    else:
        return False

@app.route("/", methods=['GET', 'POST'])
def authenticate():
    if not(is_auth()):
        if request.method == "POST":
            password = request.form['password']
            set_password = get_password()
            if password == set_password:
                session.permanent = True
                session["authenticated"] = True
                return redirect("/library")


        return render_template("landing.html", auth = is_auth())

    else:
        return redirect("/library")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect("/")

@app.route('/library', methods=['GET', 'POST'])
def get_url():
    if is_auth():
        movies = movies_info("movies")
        directory_contents = os.listdir("Movies")
        return render_template('loader.html', movie_data=movies, auth = is_auth())

    else:
        return redirect("/")


@app.route('/movie/<name>', methods=['GET', 'POST'])
def movie(name):
    if is_auth():
        data = movies_info("movies")[name]
        print(data)
        return render_template('movie.html', movie_data=data, movie_name=name, auth = is_auth())

    else:
        return redirect("/")
    


@app.route('/video_load/<name>')
def get_video(name):
    if is_auth():

            path = f"Movies/{name}.mp4"  # Update this with the path to your MP4 file
            if not os.path.exists(path):
                return "<h1>Video not found.</h1>", 404

            range_header = request.headers.get('Range', None)
            if not range_header:
                return send_file(path, mimetype='video/mp4', conditional=True)

            try:
                size = os.path.getsize(path)
                byte1, byte2 = 0, None

                match = re.search(r'(\d+)-(\d*)', range_header)
                if match:
                    byte1, byte2 = match.groups()

                byte1 = int(byte1)
                if byte2:
                    byte2 = int(byte2)
                else:
                    byte2 = size - 1

                length = byte2 - byte1 + 1

                def stream_file(length):
                    with open(path, 'rb') as f:
                        f.seek(byte1)
                        while length > 0:
                            chunk = f.read(min(8192, length))
                            if not chunk:
                                break
                            length -= len(chunk)
                            yield chunk

                rv = Response(stream_file(length), 206, mimetype='video/mp4')
                rv.headers.add('Content-Range', f'bytes {byte1}-{byte2}/{size}')
                rv.headers.add('Accept-Ranges', 'bytes')
                return rv
            except Exception as e:
                app.logger.error(f"Error serving video: {e}")
                return "<h1>OwO Oppsessies woopsies there was a error :3 Sorry it was lucario fault. Never hug him btw UwU</h1>"

    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
