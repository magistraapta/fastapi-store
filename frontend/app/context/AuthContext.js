"use client"

import { redirect } from "next/dist/server/api-utils";

const { useContext, useState, useEffect, createContext } = require("react");

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    const [error, setError] = useState('')

    const fetchUserData = async (token) => {
        try {
            const response = await fetch(`http://localhost:8000/auth/users/me`, {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })

            if (!response.ok) {
                throw new Error('Failed to fetch user')
            }

            const userData = await response.json()

            localStorage.setItem('userData', JSON.stringify(userData))
            setUser(userData)
            return userData
        } catch (error) {
            console.error('failed to fetch user', error)
            throw error
        }
    }

    const checkAuthStatus = () => {
        try {
            const token = localStorage.getItem("token");
            if (token) {
                const userData = JSON.parse(localStorage.getItem("userData"));
                setUser(userData);
            }
        } catch (error) {
            console.error("Auth status check failed:", error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        checkAuthStatus();
    }, []);

    const login = async (data) => {
        setLoading(true);
        try {
            const response = await fetch("http://localhost:8000/auth/login", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const res = await response.json();

            if (!response.ok) {
                throw new Error(res.message || "Invalid username or password")
            }

            localStorage.setItem("token", res.access_token);
            localStorage.setItem("userData", JSON.stringify(res.user)); // Save user data in localStorage
            setUser(res.user);
        } catch (error) {
            setError("An unexpected error occurred. Please try again."); // Handle unexpected errors
        } finally {
            setLoading(false);
        }
    };


    const logout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("userData");
        setUser(null);
    };
    

    return (
        <AuthContext.Provider value={{ user, loading, login, logout}}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);

    if (!context) {
        throw new Error("useAuth must be used within an AuthProvider.");
    }

    return context;
}
