
import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/api/transcribe", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>🎧 EarGPT - AI Meeting Notes</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload & Transcribe</button>

      {result && (
        <div>
          <h2>📝 Transcript</h2>
          <p>{result.transcript}</p>
          <h2>📋 Summary</h2>
          <p>{result.summary}</p>
          <h2>💡 Highlights</h2>
          <ul>
            {result.highlights.map((item, index) => <li key={index}>{item}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
