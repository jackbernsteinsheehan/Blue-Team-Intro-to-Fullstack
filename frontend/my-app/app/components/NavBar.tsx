import Link from "next/link";

const NavBar = () => {
    return (
        <div className="w-full h-[100px] border border-black border-[1px] bg-gray-700">
            <ul className="flex items-center space-x-8 text-black">
                <li> {/* Button One - Home Page */}
                    <Link
                    href="/"
                    className="hover:text-white transition duration-300 lexend-text pl-[20px]"
                    >
                        Home
                    </Link>
                </li>
                <li> {/* Button Two - About Us Page*/}
                    <Link
                    href="/aboutus"
                    className="hover:text-white transition duration-300 lexend-text pl-[20px]"
                    >
                        About Us
                    </Link>
                </li>
                {/* ... other list items ... */}
            </ul>
        </div>
    );
}

export default NavBar