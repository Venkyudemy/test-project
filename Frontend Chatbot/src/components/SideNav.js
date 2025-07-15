// src/components/SideNav.js

import React from "react";
import { NavLink } from "react-router-dom";
import "./SideNav.css";

function SideNav() {
  return (
    <div className="sidenav">
      <h2 className="logo">Priacc</h2>
      <ul>
        <li>
          <NavLink to="/" end activeClassName="active"># Chat</NavLink>
        </li>
        <li>
          <NavLink to="/hr" activeClassName="active"># HR</NavLink>
        </li>
        <li>
          <NavLink to="/procurement" activeClassName="active"># Procurement</NavLink>
        </li>
        <li>
          <NavLink to="/inventory" activeClassName="active"># Inventory</NavLink>
        </li>
        <li>
          <NavLink to="/vendor" activeClassName="active"># Vendor Management</NavLink>
        </li>
      </ul>
    </div>
  );
}

export default SideNav;
