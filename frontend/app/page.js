import Navbar from "./components/Navbar";
import Card from "./components/Card";

export default async function Home() {
  const res = await fetch('http://localhost:8000/v1/products')
  const data = await res.json()
  return (
    <div>
      <Navbar/>
      <div className="grid grid-cols-4 max-lg:grid-cols-2 mt-4 gap-y-4">
        {data.map((product) => (
          <Card id={product.id} name={product.name} price={product.price} image_url={product.image_url}/>
        ))}
      </div>
    </div>
  );
}
