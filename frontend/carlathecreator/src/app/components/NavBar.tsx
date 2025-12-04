"use client";

import React from "react";

export default function Navbar() {
  return (
    <header>
      {/* Green header with blue box */}
      <div className="header">
        <div className="header-box">
          <h1>The Blue Team</h1>
        </div>
        <h2>OSC</h2>
        <p>Oregon Software Consulting Onboarding Project</p>
      </div>

      {/* Navbar */}
      <nav className="navbar">
        <a href="#">Home</a>
        <a href="#" className="active">About Us</a>
        <a href="#">Data</a>
        <a href="#" className="right">Contact</a>
      </nav>

      {/* Styles */}
      <style jsx>{`
        .header {
          background-color: #0b462e; /* dark green */
          text-align: center;
          padding: 20px;
          font-weight: bold;
        }

        .header-box {
          display: inline-block;
          background-color: #abcbff; /* light blue */
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.2);
          padding: 20px 40px;
          margin-bottom: 10px;
        }

        h1 { margin: 0; font-size: 40px; color: black; }
        h2 { margin: 0; font-size: 30px; color: #1fbe5c; }
        p { margin: 5px 0 0; font-size: 15px; color: #1fbe5c; }

        .navbar {
          overflow: hidden;
          background-color: #1d2c24;
          margin-top: 10px;
        }

        .navbar a {
          float: left;
          display: block;
          color: white;
          text-align: center;
          padding: 14px 16px;
          text-decoration: none;
        }

        .navbar a.right { float: right; }
        .navbar a.active { background-color: #1fbe5c; color: black; }
      `}</style>
    </header>
  );
}