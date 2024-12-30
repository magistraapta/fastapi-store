import Link from "next/link"
import { Button } from "@/components/ui/button"

export default function Navbar() {
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
                <div className="flex gap-5 justify-end">
                <Link href="/login">
                <Button>Login</Button>
                </Link>
            </div>
        </nav>
        </>
    )
}