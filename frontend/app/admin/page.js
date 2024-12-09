"use client"

import { useRouter } from "next/navigation"
import { useEffect } from "react"


export default function Admin() {
    const router = useRouter()

    useEffect(() => {
        const token = localStorage.getItem('accessToken')
        if (!token){
            router.push('/login')
        }
    }, [router])

    return (
        <div>
            <h1>admin page</h1>
        </div>
    )
}