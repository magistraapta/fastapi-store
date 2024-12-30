import { Button } from "@/components/ui/button";
import Link from "next/link"
import Navbar from "./comps/Navbar";

export default async function Home() {

  const res = await fetch("http://localhost:8000/v1/products")
  const products = await res.json()

  return (
    <div>
      <Navbar/>
      <FetchProducts/>
    </div>
  );
}

async function FetchProducts() {
  try {
    const res = await fetch("http://localhost:8000/v1/products")
    const products = await res.json()

    return (
      <div className="mt-4 p-4 grid grid-cols-4 gap-5">
        {products.map((product) => (
          <Link href={`product/${product.id}`}>
          <div key={product.id} className="p-4 w-[300px] border border-gray-100 hover:border-gray-300 bg-white rounded-md">
            <img src={`http://localhost:8000${product.image_url}`} className=" object-contain" alt="product-image" />
            <div className="mt-4">
              <p>{product.name}</p>
              <p>{product.description}</p>
              <p>${product.price}</p>
            </div>
            
          </div>
          </Link>
          
        ))}
      </div>
    )

  } catch (error) {
    return (
      <div className="flex justify-center">
        <p className="">Products not found: {error}</p>
      </div>
    )
  }
}