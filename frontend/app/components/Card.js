import Image from "next/image";

export default function Card({id, image_url, name, price}) {
    return (
        <div>
            <div className="rounded-xl bg-white border border-gray-300 w-[320px] h-full p-4">
                <div key={id}>
                    <Image
                        src={image_url}
                        width={400}
                        height={200}
                        alt="product-image"
                    />
                    <div className="mt-4">
                        <h4 className="text-3xl font-semibold">{name}</h4>
                        <p>Rp.{price}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}