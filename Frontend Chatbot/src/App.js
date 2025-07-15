import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SideNav from "./components/SideNav";
import ChatBox from "./components/ChatBox";
import WorkflowForm from "./components/WorkflowForm";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="app-layout">
        <SideNav />
        <div className="main-content">
          <Routes>
            <Route path="/" element={<ChatBox />} />
            <Route path="/hr" element={<WorkflowForm module="HR" />} />
            <Route path="/procurement" element={<WorkflowForm module="Procurement" />} />
            <Route path="/inventory" element={<WorkflowForm module="Inventory" />} />
            <Route path="/vendor" element={<WorkflowForm module="Vendor Management" />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
