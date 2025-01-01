"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { AlertCircle } from "lucide-react";
import { redirect, useRouter } from "next/navigation";
import { useAuth } from "../context/AuthContext";

export default function Login() {
    const {login} = useAuth()
    const router = useRouter()
    const [formData, setFormData] = useState({
        username: '',
        password: ''
    })
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()
        setError('')
        setLoading(true)
    
        try {
            await login(formData)
            router.push("/")
        } catch (error) {
            setError(error.message || 'An error occurred during login')
        } finally {
            setLoading(false)
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
          ...prev,
          [name]: value
        }));
    };
    
    return (
        <>
            <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
            <Card className="w-full max-w-md">
                <CardHeader className="space-y-1">
                <CardTitle className="text-2xl font-bold">Login</CardTitle>
                <CardDescription>
                    Enter your email and password to access your account
                </CardDescription>
                </CardHeader>
                <CardContent>
                <form onSubmit={handleSubmit}>
                    <div className="space-y-4">
                    <div className="space-y-2">
                        <Label htmlFor="email">Username</Label>
                        <Input
                        id="username"
                        name="username"
                        type="text"
                        placeholder="Enter your username"
                        required
                        value={formData.username}
                        onChange={handleChange}
                        />
                    </div>
                    <div className="space-y-2">
                        <Label htmlFor="password">Password</Label>
                        <Input
                        id="password"
                        name="password"
                        type="password"
                        placeholder="Enter your password"
                        required
                        value={formData.password}
                        onChange={handleChange}
                        />
                    </div>

                    {error && (
                        <Alert variant="destructive">
                        <AlertCircle className="h-4 w-4" />
                        <AlertDescription>{error}</AlertDescription>
                        </Alert>
                    )}

                    <Button 
                        type="submit" 
                        className="w-full"
                        disabled={loading}
                    >
                        {loading ? 'Signing in...' : 'Sign in'}
                    </Button>
                    </div>
                </form>
                </CardContent>
                <CardFooter>
                <div className="text-sm text-gray-500 text-center w-full">
                    Don't have an account?{' '}
                    <a 
                    href="/signup" 
                    className="text-primary hover:underline font-medium"
                    >
                    Sign up
                    </a>
                </div>
                </CardFooter>
            </Card>
            </div>
        </>
    )
}
