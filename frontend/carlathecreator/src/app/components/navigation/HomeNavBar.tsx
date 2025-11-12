import Link from "next/link";
import React from 'react';
const NavBar2 = () => {
    return (
        <div className="w-full h-[100px] border border-black border-[1px] bg-gray-700">
            <ul className="flex items-center space-x-8 text-black">
                {/* Button One - Home Page */}
                <li>
                    <Link
                        href="/"
                        className="hover:text-white transition duration-300 lexend-text pl-[20px]"
                    >
                        Home
                    </Link>
                </li> 

                {/* Button Two - About Us Page */}
                <li>
                    <Link
                        href="/aboutus"
                        className="hover:text-white transition duration-300 lexend-text pl-[20px]"
                    >
                        About Us
                    </Link>
                </li>

                {/* Add more buttons here */}
            </ul>
        </div>
    );
}

export default NavBar2;
