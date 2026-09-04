import { useState } from "react";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");

  const handleResumeChange = (event) => {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      setResume(selectedFile);
    }
  };

  const handleAnalyze = async () => {
  try {
    const response = await fetch(
      "http://127.0.0.1:5000/api/health"
    );

    const data = await response.json();

    alert(data.message);
  } catch (error) {
    console.error(error);
    alert("Backend connection failed");
  }
};

  return (
    <div className="app">

      <div className="header">
        <h1>Resume, Reimagined.</h1>

        <p>
          Upload your resume and discover how well it matches
          your dream job.
        </p>
      </div>

      <div className="card">

        <div className="section">
          <label>Upload Your Resume</label>

          <div className="upload-box">
            <p>
              Upload your resume in PDF format
            </p>

            <input
              className="file-input"
              type="file"
              accept=".pdf"
              onChange={handleResumeChange}
            />

            {resume && (
              <p className="file-name">
                ✓ {resume.name}
              </p>
            )}
          </div>
        </div>

        <div className="section">
          <label>Job Description</label>

          <textarea
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(event) =>
              setJobDescription(event.target.value)
            }
          />
        </div>

        <button
          className="analyze-button"
          onClick={handleAnalyze}
        >
          Analyze Resume
        </button>

      </div>

    </div>
  );
}

export default App;
