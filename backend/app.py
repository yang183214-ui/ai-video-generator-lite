from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="../static")

def generate_script(text):
    return [
        f"主题：{text}",
        "AI正在生成视频",
        "自动短视频已完成"
    ]

@app.route("/api/generate", methods=["POST"])
def generate():
    text = request.json["text"]

    script = generate_script(text)

    os.system("ffmpeg -y -i static/bg.mp4 -i static/audio.mp3 -shortest static/output.mp4")

    return jsonify({
        "script": script,
        "video_url": "/static/output.mp4"
    })

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)
