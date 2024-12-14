import Image from "next/image";

export default function Card({id, image_url, name, price}) {
    return (
        <div>
            <div className="border rounded-xl shadow-md w-[300px] p-4">
                <div key={id}>
                    <Image
                        src={image_url}
                        width={400}
                        height={200}
                        alt="product-image"
                    />
                    <div>
                    <h4 className="text-3xl font-semibold">{name}</h4>
                    <p>Rp.{price}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}