import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

interface Message {
  role: 'user' | 'agent';
  content: string;
}

const App: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');

    try {
      const res = await axios.post('http://localhost:8000/chat', { message: userMsg.content, model: '' });
      const botMsg: Message = { role: 'agent', content: res.data.response };
      setMessages(prev => [...prev, botMsg]);
    } catch (e: any) {
      const botMsg: Message = { role: 'agent', content: 'Error: ' + e.message };
      setMessages(prev => [...prev, botMsg]);
    }
  };

  return (
    <div className="h-screen flex flex-col p-4">
      <div className="flex-1 overflow-y-auto space-y-2">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`p-3 rounded-md max-w-lg ${m.role === 'user' ? 'bg-blue-600 text-white self-end ml-auto' : 'bg-gray-200 text-gray-900 mr-auto'}`}
          >
            {m.content}
          </div>
        ))}
      </div>
      <div className="mt-4 flex">
        <textarea
          className="flex-1 border rounded-md p-2" rows={2}
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="ml-2 px-4 py-2 bg-blue-600 text-white rounded-md" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default App;
