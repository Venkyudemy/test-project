import React, { useState } from "react";
import "./ChatBox.css";

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;
    const newMessage = { sender: "User", text: input, type: "user" };
    setMessages((prev) => [...prev, newMessage]);
    setInput("");
  };

  return (
    <div className="chatbox-wrapper">
      <div className="chatbox-container">
        <div className="chat-header">Priacc Chat Assistant</div>

        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.type}`}>
              {msg.text}
            </div>
          ))}
        </div>

        <div className="workflow-buttons">
          <button>Apply Leave</button>
          <button>Create PO</button>
          <button>View Inventory</button>
          <button>Add Vendor</button>
        </div>

        <div className="chat-input">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default ChatBox;
