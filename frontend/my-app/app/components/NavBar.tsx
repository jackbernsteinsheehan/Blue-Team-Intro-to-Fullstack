/*import React from 'react';
// Removed: import Link from "next/link";
// We use standard <a> tags for navigation within this environment.

const Navbar = () => {
    return (
        // Main container: Increased height, professional deep blue background, subtle shadow, sticky top
        <nav className="w-full bg-green-800 shadow-xl sticky top-0 z-10">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
                
        
                <div className="flex-shrink-0">
              
                    <a href="/" className="text-2xl font-extrabold text-white tracking-wider">
                        OSC
                    </a>
                </div>

          
                <div className="hidden sm:block">
                    <ul className="flex items-baseline space-x-6">
                        
                       
                        <li> 
                         
                            <a href="/" className="text-white px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out hover:bg-green-600 hover:text-white">
                                Home
                            </a>
                        </li>

                      
                        <li>
                    
                            <a href="/test_api" className="text-white px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out hover:bg-green-600 hover:text-white">
                                Test_API Page
                            </a>
                        </li>
                        
                    </ul>
                </div>
            </div>
        </nav>
    );
}

*/

"use client";

export default function Header() {
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
        <a href="#" className="active">Home</a>
        <a href="#">About Us</a>
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
