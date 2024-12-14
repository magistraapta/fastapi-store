export default function CartSidebar ({isOpen, onClose}) {
    return (
        <div
            className={`fixed top-0 right-0 h-full w-80 bg-white shadow-lg transition-transform transform ${
                isOpen ? "translate-x-0" : "translate-x-full"
            }`}
            style={{ zIndex: 1000 }}
            >
            <button
                onClick={onClose}
                className="absolute top-2 left-2 text-xl font-bold"
            >
                ×
            </button>

            <div className="p-5 mt-4">
                <h2 className="text-lg font-bold mb-4">Your Cart</h2>
                <ul>
                <li className="flex justify-between mb-2">
                    <p>Item 1</p>
                    <p>$10</p>
                </li>
                <li className="flex justify-between mb-2">
                    <p>Item 2</p>
                    <p>$15</p>
                </li>
                </ul>
                <div className="mt-4">
                <button className="bg-black text-white px-4 py-2 rounded w-full">
                    Checkout
                </button>
                </div>
            </div>
        </div>
    )
}