from flask import Flask, request, jsonify
from flask_cors import CORS
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
CORS(app)

# Load AI model
print("Loading AI model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("AI model loaded successfully!")


@app.route("/")
def home():
    return "AI Resume Analyzer Backend is Running!"


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description")

    if not resume:
        return jsonify({
            "message": "Please upload a resume."
        }), 400

    if not job_description:
        return jsonify({
            "message": "Please enter a job description."
        }), 400

    # -----------------------------
    # Extract resume text
    # -----------------------------

    try:

        reader = PdfReader(resume)

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    except Exception as e:

        print("PDF extraction error:", e)

        return jsonify({
            "message": "Could not read the PDF."
        }), 500

    if not resume_text.strip():

        return jsonify({
            "message": "Could not extract text from the PDF."
        }), 400

    # -----------------------------
    # AI semantic similarity
    # -----------------------------

    try:

        resume_embedding = model.encode(
            resume_text,
            convert_to_tensor=True
        )

        job_embedding = model.encode(
            job_description,
            convert_to_tensor=True
        )

        similarity = util.cos_sim(
            resume_embedding,
            job_embedding
        ).item()

        score = round(similarity * 100, 2)

        # Keep score between 0 and 100
        score = max(0, min(score, 100))

    except Exception as e:

        print("AI analysis error:", e)

        return jsonify({
            "message": "AI analysis failed."
        }), 500

    print("\n==============================")
    print("Resume:", resume.filename)
    print("AI Match Score:", score)
    print("==============================\n")

    return jsonify({
        "message": "Resume analyzed successfully!",
        "score": score,
        "resume_text": resume_text
    })


if __name__ == "__main__":
    app.run(debug=True)