const SomeSquare = ({color, text} : {color:string; text:string}) => {
    return (
        <>
        <div style={{ backgroundColor: color, width: '500px', height: '500px'}}>
            <h1 className="text-auto text-center">
                sup
            </h1>
        </div>
        </>
    )
}

export default SomeSquare;