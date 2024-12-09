import Navbar from "./components/Navbar";

export default async function Home() {
  const res = await fetch('http://localhost:8000/v1/products')
  const data = await res.json()
  return (
    <div>
      <Navbar/>
      <div className="grid grid-cols-4 mt-4 gap-y-4">
        {data.map((product) => (
          <div className="border rounded-xl shadow-md w-[200px]">
            <p key={product.id}>{product.name}</p>
            <p>{product.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
