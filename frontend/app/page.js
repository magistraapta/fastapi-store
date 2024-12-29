import { Button } from "@/components/ui/button";
import Image from "next/image";

export default async function Home() {

  const res = await fetch("http://localhost:8000/v1/products")
  const products = await res.json()
  console.log(products)
  return (
    <div>
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

      <div className="mt-4 p-4 grid grid-cols-4 gap-5">
        {products.map((product) => (
          <div key={product.id} className="p-4 w-[300px] border border-gray-100 hover:border-gray-300 bg-white rounded-md">
            <img src="static/images/not-found.png" className=" object-contain" alt="product-image" />
            <div className="mt-4">
              <p>{product.name}</p>
              <p>{product.description}</p>
              <p>{product.price}</p>
            </div>
            
          </div>
        ))}
      </div>
    </div>
  );
}


