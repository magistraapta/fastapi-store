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

    

    return (
        <nav className="grid grid-cols-2">
            <div>
                <h1 className="font-bold text-4xl">
                    FastStore
                </h1>
            </div>
            <div className="flex justify-end space-x-4 items-center">
                {isLoggedIn ? (
                    <>
                        <a href="/admin" className="text-blue-500 hover:underline">
                            Admin
                        </a>
                        <button
                            onClick={handleLogout}
                            className="text-red-500 hover:underline"
                        >
                            Logout
                        </button>
                    </>
                ) : (
                    <a href="/login" className="text-blue-500 hover:underline">
                        Login
                    </a>
                )}
            </div>
        </nav>
    );
}
