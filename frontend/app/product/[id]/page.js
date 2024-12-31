import Navbar from "@/app/comps/Navbar";
import { Button } from "@/components/ui/button";


export default async function Page({params}) {
    const {id} = params
    const res = await fetch(`http://localhost:8000/v1/products/${id}`)

    if (!res.ok) {
        throw new Error("failed to fetch product data")
    }
    const product = await res.json()
    return (
        <>
        <Navbar/>

        <div className="flex justify-center">
            <div className="bg-white w-11/12 h-[630px] mt-5 grid grid-rows-2 p-4 rounded-lg">
                    <div className="w-full flex justify-center">
                        <img src={product.image_url} alt="product-image" className="w-8/12 object-contain"/>
                    </div>

                    <div className="mt-4 w-full">
                        <div>
                            <p className="text-5xl font-bold">{product.name}</p>
                            <div className="mt-4">
                                <p className="text-xl">${product.price}</p>
                                <div className="mt-5">
                                    <p className="text-3xl font-semibold">Description</p>
                                    <p className="">{product.description}</p>
                                </div>
                                
                            </div>
                        </div>

                        <div className="gap-y-3 grid mt-4">
                            <Button className="w-full" variant="secondary">Add to cart</Button>
                            <Button className="w-full">Checkout</Button>
                        </div>
                    </div>

                    
            </div>
        </div>
        </>
    )
}

async function FetchReview() {
    const res = await fetch()
    const reviews = res.json()


}