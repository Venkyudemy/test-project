// src/components/WorkflowForm.js

import React, { useState } from "react";
import "./WorkflowForm.css";

function WorkflowForm({ module = "Workflow" }) {
  const [type, setType] = useState("Apply Leave");
  const [details, setDetails] = useState("");

  const submitRequest = () => {
    alert(`Submitted: ${type} with details: ${details}`);
    setDetails("");
  };

  return (
    <div className="workflow-form">
      <h3>{module} - Workflow Trigger</h3>

      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option>Apply Leave</option>
        <option>Create PO</option>
        <option>Update Stock</option>
        <option>Add Vendor</option>
      </select>

      <textarea
        placeholder="Enter details"
        value={details}
        onChange={(e) => setDetails(e.target.value)}
      />

      <button onClick={submitRequest}>Submit</button>
    </div>
  );
}

export default WorkflowForm;