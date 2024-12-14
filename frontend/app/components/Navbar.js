"use client";

import { useState, useEffect } from "react";
import CartSidebar from "./CartSidebar";

export default function Navbar() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [isCartOpen, setCartOpen] = useState(false);

    const toggleCart = () => {
        setCartOpen((prev) => !prev)
    }

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
                        <p className=" text-gray-500 text-sm" key={index}>{item}</p>
                    ))}
                </div>
            </div>
            
            <div>
                <input type="text" placeholder="input for search" className="border border-gray-200 rounded-lg py-2 px-4 w-full" />
            </div>

            <div className="flex justify-end">
                <button onClick={toggleCart} className="relative bg-white border border-gray-200 p-2 rounded-lg">
                    🛒
                    <span className="absolute -top-1 -right-2 bg-red-500 text-white text-xs rounded-full px-2">
                    3
                    </span>
                </button>
            </div>
            <CartSidebar isOpen={isCartOpen} onClose={toggleCart}/>
        </nav>
    );
}
