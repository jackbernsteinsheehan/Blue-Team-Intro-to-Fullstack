import React from 'react';
// Removed: import Link from "next/link";
// We use standard <a> tags for navigation within this environment.

const Navbar = () => {
    return (
        // Main container: Increased height, professional deep blue background, subtle shadow, sticky top
        <nav className="w-full bg-green-800 shadow-xl sticky top-0 z-10">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
                
                {/* 1. Brand/Logo Section */}
                <div className="flex-shrink-0">
                    {/* Placeholder for a logo or brand name */}
                    {/* Replaced Link with <a> */}
                    <a href="/" className="text-2xl font-extrabold text-white tracking-wider">
                        OSC
                    </a>
                </div>

                {/* 2. Navigation Links */}
                <div className="hidden sm:block">
                    <ul className="flex items-baseline space-x-6">
                        
                        {/* Button 1 - Home page */}
                        <li> 
                            {/* Replaced Link with <a> */}
                            <a href="/about" className="text-white px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out hover:bg-green-600 hover:text-white">
                                AboutUs
                            </a>
                        </li>

                        {/* Button 2 - Stock Page */} 
                        <li>
                            {/* Replaced Link with <a> */}
                            <a href="/stock_ex" className="text-white px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out hover:bg-green-600 hover:text-white">
                                Stocks Dashboard
                            </a>
                        </li>

                        {/* Button 3 - Test API */}
                        <li> 
                            <a href="/test_api" className="text-white px-3 py-2 rounded-md text-sm font-medium transition duration-150 ease-in-out hover:bg-green-600 hover:text-white">
                                API TEST
                            </a>

                        </li>
                        
                    </ul>
                </div>
            </div>
        </nav>
    );
}

export default Navbar