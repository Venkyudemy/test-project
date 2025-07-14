import React from "react";
import ChatBox from "./components/ChatBox";
import Sidebar from "./components/Sidebar";
 
function App() {
  return (
    <div className="app">
      <Sidebar />
      <ChatBox />
    </div>
  );
}
 
export default App;