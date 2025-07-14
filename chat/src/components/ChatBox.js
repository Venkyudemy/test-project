import React, { useState } from 'react';
import './ChatBox.css';
 
const ChatBox = () => {
  const [messages, setMessages] = useState([
    { text: "Hi, I'm your assistant! How can I help you?", sender: "bot" },
  ]);
  const [input, setInput] = useState("");
 
  const handleSend = () => {
    if (!input.trim()) return;
 
    const newMessage = { text: input, sender: "user" };
    const reply = { text: `You said: "${input}"`, sender: "bot" };
 
    setMessages([...messages, newMessage, reply]);
    setInput("");
  };
 
  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender === "bot" ? "bot" : "user"}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};
 
export default ChatBox;