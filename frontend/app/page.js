import Navbar from "./components/Navbar";
import Card from "./components/Card";

export default async function Home() {
  const res = await fetch('http://localhost:8000/v1/products')
  const data = await res.json()
  return (
    <div>
      <Navbar/>
      <div className="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 mt-4 gap-x-4 gap-y-4 w-full">
        {data.map((product) => (
          <Card
            key={product.id}
            id={product.id}
            name={product.name}
            price={product.price}
            image_url={product.image_url}
          />
        ))}
      </div>

    </div>
  );
}
