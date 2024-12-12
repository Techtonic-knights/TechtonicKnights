import openai
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

openai.api_key = "<your-openai-api-key>"


def get_question_or_options(line):
    if line.endswith("?"):
        return line, 'q'
    return line, 'a'


@app.route("/generate-quiz")
def generate_quiz():
    video_id = request.args.get('video_id')

    if not video_id:
        return jsonify({'error': 'Missing required parameter: video_id'}), 400

    text = ""
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    for transcript in transcript_list:
        transcript_txt = transcript.translate('en').fetch()
        text += transcript_txt[0]["text"].split(",")[0]

    prompt = f"Generate quiz questions based on the following text:\n\n{text}\n\nQuestions with multiple choice answers."

    try:
        response = openai.Completion.create(
            engine = "gpt-3.5-turbo-instruct",
            prompt = prompt,
            max_tokens = 1000,
            temperature = 0.7,
            n = 1,
            stop = None
        )

        quix_text = response.choices[0].text.strip()
        lines = quix_text.split("\n")
        quiz_questions = []

        for line in lines:
            line = line.strip()
            text, val = get_question_or_options(line)
            if not text :
                continue

            if val == 'q':
                question_id = uuid.uuid4()
                quiz_questions.append({
                    "id" : str(question_id),
                    "question": text,
                    "options": []
                })
            else:
                quiz_questions[-1]["options"].append(text)
        return jsonify({"quiz": quiz_questions})

    except Exception as e:
        print(f"An error occurred:{e}")
        return jsonify()

if __name__ == '__main__':
    app.run(debug= True, port= 8000)