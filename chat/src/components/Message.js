import React from "react";
 
const Message = ({ message }) => (
  <div className="message">
    <strong>{message.sender}:</strong> {message.content}
  </div>
);
 
export default Message;