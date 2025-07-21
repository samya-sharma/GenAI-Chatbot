import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState([]);
  const [file, setFile] = useState(null);

  const sendPrompt = async () => {
    const formData = new FormData();
    formData.append("prompt", prompt);
    const res = await axios.post("http://localhost:8000/chat", formData);
    setMessages([...messages, { role: 'user', text: prompt }, { role: 'bot', text: res.data.response }]);
    setPrompt('');
  };

  const uploadPDF = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post("http://localhost:8000/upload_pdf", formData);
    alert("PDF Uploaded!");
  };

  const reset = async () => {
    await axios.get("http://localhost:8000/reset");
    setMessages([]);
    alert("Chat reset");
  };

  return (
    <div className="App" style={{ padding: '2rem' }}>
      <h2>📚 GenAI Chatbot with PDF</h2>

      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={uploadPDF}>Upload PDF</button>
      <button onClick={reset} style={{ marginLeft: '1rem' }}>Reset</button>

      <div style={{ marginTop: '1rem', height: '300px', overflowY: 'scroll', border: '1px solid #ccc', padding: '1rem' }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ marginBottom: '1rem' }}>
            <strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.text}
          </div>
        ))}
      </div>

      <input
        style={{ width: '70%', marginTop: '1rem' }}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Type your prompt..."
      />
      <button onClick={sendPrompt}>Send</button>
    </div>
  );
}

export default App;