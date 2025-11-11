import Rectangle from "./components/rectangle";

const HomePage = () => {
    return (
        <div className="flex w-full min-h-screen justify-center bg-white">
            <div className="flex flex-col w-full items-center">
                <h1 className="text-[50px] text-center text-black">
                    HELLO
                </h1>
                <Rectangle />
            </div>
        </div>
    );
}

export default HomePage;
