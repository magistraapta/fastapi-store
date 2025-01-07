"use client"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { useAuth } from "../context/AuthContext"
import { useRouter } from "next/navigation"
import { UserDropdown } from "./UserDropdown"

export default function Navbar() {
    const {user, logout} = useAuth()
    const router = useRouter()
    const handleLogout = () => {
        try {
            logout()
            router.push("/")
            router.refresh()
        } catch (error) {
            console.error("error logout" || error)
        }
    }
    return (
        <>
        <nav className="grid grid-cols-2 p-4 bg-white shadow-md items-center">
            <div className="flex items-center gap-3">
                <Link href="/">
                <h1 className=" text-3xl font-bold">FastStore</h1>
                </Link>
                <div className="flex gap-5 text-gray-500">
                    <p>Electronics</p>
                    <p>Clothing</p>
                    <p>Shoes</p>
                </div>
            </div>

            <div className="flex gap-5 justify-end items-center">
                {user ? (
                    <>
                        <div>
                            <UserDropdown username={user.username}/>

                        </div>
                        <Button onClick={handleLogout} variant="destructive">
                            Logout
                        </Button>
                    </>
                ) : (
                    <>
                        <Link href="/login">
                            <Button>Login</Button>
                        </Link>
                    </>
                )}
            </div>
        </nav>
        </>
    )
}