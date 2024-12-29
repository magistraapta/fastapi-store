import { Button } from "@/components/ui/button";

export default function Navbar(){
    <>
        <nav className=" grid grid-cols-2 p-4 bg-white shadow-md items-center">
            <div className="flex items-center gap-3">
            <h1 className=" text-3xl font-bold">Fast Store</h1>
            <div className="flex gap-5 text-gray-500">
                <p>Electronics</p>
                <p>Clothing</p>
                <p>Shoes</p>
            </div>
            </div>
            <div className="flex gap-5 justify-end">
            <Button>
                Login
            </Button>
            </div>
        </nav>
    </>
    
}