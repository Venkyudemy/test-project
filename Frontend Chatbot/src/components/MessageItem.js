import React from "react";
import "./MessageItem.css";

function MessageItem({ sender, text, timestamp }) {
  return (
    <div className={`message-item ${sender === "User" ? "user" : "ai"}`}>
      <div className="message-header">
        <strong>{sender}</strong>
        <span className="timestamp">{timestamp}</span>
      </div>
      <div className="message-text">{text}</div>
    </div>
  );
}

export default MessageItem;