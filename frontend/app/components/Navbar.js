"use client";

import { useState, useEffect } from "react";

export default function Navbar() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        // Check if the access token is stored
        const token = localStorage.getItem("accessToken");
        setIsLoggedIn(!!token);
    }, []);

    const handleLogout = () => {
        // Clear the token and update state
        localStorage.removeItem("accessToken");
        setIsLoggedIn(false);
    };

    const navbarList = ["All", "Gadget", "Shoes"]
    return (
        <nav className="grid grid-cols-3 items-center">
            <div className=" flex w-30 items-center gap-4">

                <p className=" text-sm font-bold">FastStore</p>

                <div className="max-lg:hidden flex gap-4">
                    {navbarList.map((item, index) => (
                        <p className=" text-gray-600 text-sm" key={index}>{item}</p>
                    ))}
                </div>
            </div>
            
            <div>
                <input type="text" placeholder="input for search" className="border border-gray-300 rounded-lg py-2 px-4 w-full" />
            </div>

            <div className="flex justify-end">
                <button className="text-gray-600 text-sm border border-blue-600 rounded-lg p-2">Cart</button>
            </div>
        </nav>
    );
}
