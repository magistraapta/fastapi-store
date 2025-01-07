import Link from "next/link"
import Navbar from "./comps/Navbar";

export default async function Home() {
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
    const data = await res.json()
    const products = data.products


    return (
      <div className="mt-4 p-4 grid grid-cols-4 gap-5">
        {products.map((product) => (
          <Link href={`product/${product.id}`} key={product.id}>
            <div className="p-4 w-[300px] border border-gray-100 hover:border-gray-300 bg-white rounded-md">
              <img 
                src={`http://localhost:8000${product.image_url}`} 
                className="object-contain" 
                alt={product.name} 
              />
              <div className="mt-4">
                <p>{product.name}</p>
                <p className="">${product.price}</p>
              </div>
            </div>
          </Link>
        ))}
      </div>
    )

  } catch (error) {
    return (
      <div className="flex justify-center">
        <p className="">Products not found: {error.message}</p>
      </div>
    )
  }
}